"""
    Battleships in python
"""

def print_grid():
    """
    Creates board for Battleships
    """
    print("a b c d e f g h i j")
    row = ['\u2B1C']*10
    board = []
    for _ in range(10):
        board.append(['\u2B1B']*10)
    board[0][0] = '\u2B1C'
    board[0][1] = '\u2B1C'
    board[0][2] = '\u2B1C'
    board[0][3] = '\u2B1C'

    for row in board:
        print(''.join(row))


print_grid()
