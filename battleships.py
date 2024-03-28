
def print_grid():
    print("   a b c d e f g h i j")
    row = [u'\u2B1C']*10
    board = []
    for i in range(10):
        board.append([u'\u2B1B']*10)
    board[0][0] = u'\u2B1C'
    board[0][1] = u'\u2B1C'
    board[0][2] = u'\u2B1C'
    board[0][3] = u'\u2B1C'
    
    for row in board:
        print(''.join(row))

print_grid()
