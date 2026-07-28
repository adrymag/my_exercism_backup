BLACK = 'B'
WHITE = 'W'
NONE = ''


class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.height = len(board)
        self.width = len(board[0]) if board else 0

    def _in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def territory(self, x, y):
        if not self._in_bounds(x, y):
            raise ValueError('Invalid coordinate')

        if self.board[y][x] != ' ':
            return (NONE, set())

        region = set()
        queue = [(x, y)]
        while queue:
            cx, cy = queue.pop()
            if (cx, cy) in region:
                continue
            region.add((cx, cy))
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                nx, ny = cx + dx, cy + dy
                if (self._in_bounds(nx, ny)
                        and self.board[ny][nx] == ' '
                        and (nx, ny) not in region):
                    queue.append((nx, ny))

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
        result = {BLACK: set(), WHITE: set(), NONE: set()}
        visited = set()

        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == ' ' and (x, y) not in visited:
                    owner, region = self.territory(x, y)
                    result[owner].update(region)
                    visited.update(region)

        return result