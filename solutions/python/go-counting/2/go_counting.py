"""
Go Counting — Exercism Python Track

This module implements territory counting for the game of Go (Baduk/Weiqi).

In Go, a player's territory consists of empty board intersections that are
completely surrounded by that player's stones (horizontally and vertically).
If an empty region borders stones of both players (or the board edge with
no enclosing stones), it is neutral territory (belongs to neither player).

Stones themselves are never part of any territory.

The board is represented as a list of strings, where:
    ' ' = empty intersection
    'B' = black stone
    'W' = white stone

Module-level constants define the possible territory owners:
    BLACK  -- territory owned by Black player  ('B')
    WHITE  -- territory owned by White player  ('W')
    NONE   -- neutral territory (no single owner)  ('')
"""

# ---------------------------------------------------------------------------
# Module-level constants
# ---------------------------------------------------------------------------
# These are exported so that test code (and any consumer) can refer to
# owners symbolically instead of hard-coding single-character strings.
BLACK = 'B'
WHITE = 'W'
NONE = ''


class Board:
    """Count territories of each player in a Go game.

    Args:
        board (list[str]): A two-dimensional Go board. Each string is a row;
            each character is an intersection (' ', 'B', or 'W').

    Attributes:
        board (list[str]): The raw board data passed to the constructor.
        height (int): Number of rows on the board.
        width (int): Number of columns on the board (derived from the first row).
    """

    def __init__(self, board):
        """Store the board and pre-compute its dimensions for quick lookup."""
        self.board = board
        self.height = len(board)
        # Guard against an empty board; otherwise take the length of the first row.
        self.width = len(board[0]) if board else 0

    def _in_bounds(self, x, y):
        """Return True if coordinate (x, y) lies inside the board.

        Coordinates are zero-based: x is the column, y is the row.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def territory(self, x, y):
        """Find the owner and the territory region that contains (x, y).

        The algorithm works in two phases:

        1. Flood-fill (BFS) over the four cardinal neighbours to discover
           the entire connected empty region that contains (x, y).
           Only horizontal and vertical adjacency counts; diagonals do not.

        2. Inspect every cell that borders the discovered region.  If ALL
           bordering stones are the same colour, that colour owns the region.
           If the region borders stones of both colours (or no stones at all),
           the region is neutral (NONE).

        Args:
            x (int): Column on the board.
            y (int): Row on the board.

        Returns:
            tuple(str, set): (owner, region) where owner is one of BLACK,
            WHITE, or NONE, and region is a set of (x, y) coordinates.

        Raises:
            ValueError: If (x, y) is outside the board boundaries.
        """
        # -------------------------------------------------------------------
        # Validate coordinates first — the exercise requires a ValueError
        # with the exact message "Invalid coordinate" for out-of-bounds access.
        # -------------------------------------------------------------------
        if not self._in_bounds(x, y):
            raise ValueError('Invalid coordinate')

        # -------------------------------------------------------------------
        # A stone is never part of a territory.  Return immediately with an
        # empty set so that the caller knows there is no territory here.
        # -------------------------------------------------------------------
        if self.board[y][x] != ' ':
            return (NONE, set())

        # -------------------------------------------------------------------
        # Phase 1 — Breadth-first search (BFS) over empty intersections.
        #
        # We start from (x, y) and explore north, south, east, west.
        # Every reachable empty cell becomes part of the same territory
        # region.  Using a list as a stack gives us DFS, but the order
        # does not matter for correctness; any graph traversal works.
        # -------------------------------------------------------------------
        region = set()          # all empty cells belonging to this territory
        queue = [(x, y)]        # cells waiting to be explored

        while queue:
            cx, cy = queue.pop()

            # Skip if we have already visited this cell (can happen when a
            # cell is enqueued from two different neighbours).
            if (cx, cy) in region:
                continue

            region.add((cx, cy))

            # Explore the four cardinal directions.
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = cx + dx, cy + dy

                # A neighbour belongs to the same territory iff it is:
                #   • inside the board, AND
                #   • an empty intersection (' '), AND
                #   • not yet visited.
                if (self._in_bounds(nx, ny)
                        and self.board[ny][nx] == ' '
                        and (nx, ny) not in region):
                    queue.append((nx, ny))

        # -------------------------------------------------------------------
        # Phase 2 — Determine the owner by inspecting border stones.
        #
        # For every cell in the region we look at its four neighbours.
        # Any neighbour that is a stone ('B' or 'W') is recorded in the
        # `borders` set.  After the loop:
        #   • borders == {'B'}  →  owner is BLACK
        #   • borders == {'W'}  →  owner is WHITE
        #   • borders has 0 or 2+ colours  →  owner is NONE (neutral)
        # -------------------------------------------------------------------
        borders = set()
        for cx, cy in region:
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = cx + dx, cy + dy
                if self._in_bounds(nx, ny) and self.board[ny][nx] != ' ':
                    borders.add(self.board[ny][nx])

        if len(borders) == 1:
            owner = borders.pop()
        else:
            owner = NONE

        return (owner, region)

    def territories(self):
        """Find every territory on the board and group them by owner.

        We iterate over every board cell.  When we encounter an empty cell
        that has not yet been assigned to a territory, we call `self.territory`
        to discover the whole connected region.  That region is then added
        to the result dictionary under the appropriate owner key and marked
        as visited so that we never process the same region twice.

        Returns:
            dict(str, set): Mapping from owner (BLACK, WHITE, NONE) to the
            union of all territory coordinates owned by that player.
        """
        # Pre-populate the result so that every owner key always exists,
        # even if its value is an empty set (makes test assertions simpler).
        result = {BLACK: set(), WHITE: set(), NONE: set()}

        # Keep track of which empty cells have already been assigned to a
        # territory region so that we do not re-process them.
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                # Only empty cells that have not yet been visited can start
                # a new territory region.
                if self.board[y][x] == ' ' and (x, y) not in visited:
                    owner, region = self.territory(x, y)
                    result[owner].update(region)
                    visited.update(region)

        return result