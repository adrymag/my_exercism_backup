def wonByX(board):
    winsByX = []

    wonRows = [row for row in range(3) if set(board[row]) == {'X'}]
    
    if len(wonRows) > 0:
        winsByX = winsByX + [[True, 'byRow', wonRows]]

    wonColumns = [column for column in range(3) if set([board[0][column], board[1][column], board[2][column]]) == {'X'}]
        
    if len(wonColumns) > 0:
        winsByX = winsByX + [[True, 'byColumn', wonColumns]]

    wonFirstDiag = [[True, 'byDiag', 'First']]
    wonSecondDiag = [[True, 'byDiag', 'Second']]

    if len([row for row in range(3) if board[row][row] == 'X']) == 3:
        winsByX = winsByX + wonFirstDiag

    if len([row for row in range(3) if board[row][2-row] == 'X']) == 3:
            winsByX = winsByX + wonSecondDiag

    # if len(winsByX) == 0:
    #     return [False, '', []]

    return winsByX

def wonByO(board):
    winsByO = []

    wonRows = [row for row in range(3) if set(board[row]) == {'O'}]
    
    if len(wonRows) > 0:
        winsByO = winsByO + [[True, 'byRow', wonRows]]

    wonColumns = [column for column in range(3) if set([board[0][column], board[1][column], board[2][column]]) == {'O'}]
        
    if len(wonColumns) > 0:
        winsByO = winsByO + [[True, 'byColumn', wonColumns]]

    wonFirstDiag = [[True, 'byDiag', 'First']]
    wonSecondDiag = [[True, 'byDiag', 'Second']]

    if len([row for row in range(3) if board[row][row] == 'O']) == 3:
        winsByO = winsByO + wonFirstDiag

    if len([row for row in range(3) if board[row][2-row] == 'O']) == 3:
            winsByO = winsByO + wonSecondDiag

    # if len(winsByO) == 0:
    #         return [False, '', []]
    
    return winsByO


def isFull(board):
    if len([(x,y) for x in range(3) for y in range(3) if board[x][y] in {'X','O'}]) == 9:
        return True

    return False

def gamestate(board):
    if len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'O']) == 1 and len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'X']) == 0:
        # Example when player O goes before player X.
        raise ValueError("Wrong turn order: O started")

    if len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'O']) > len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'X']):
        raise ValueError("Wrong turn order: O started") #  or played multiple times and now has more pieces on the board than X

    if len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'X']) > 1 + len([(x,y) for x in range(3) for y in range(3) if board[x][y] == 'O']):
        # Example when player X goes twice.
        raise ValueError("Wrong turn order: X went twice")

    winsByX = wonByX(board)
    winsByO = wonByO(board)
    # [isWonByX, howXwon, XwinIDs]
    # [isWonByO, howOwon, OwinIDs]

    if len(winsByX) > 0 and len(winsByO) > 0: # len(winsByX) + len(winsByO) > 1:
        # Example when player X wins AND player O wins.
        raise ValueError("Impossible board: game should have ended after the game was won")

    if len(winsByX) > 0 or len(winsByO) > 0: # len(winsByX) + len(winsByO) == 1
        return "win"

    if isFull(board):
        return "draw"

    return "ongoing"