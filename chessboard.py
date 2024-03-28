import numpy as np

chrs = {
    'b_checker': '\u25FB',
    'b_pawn': '\u265F',
    'b_rook': '\u265C',
    'b_knight': '\u265E',
    'b_bishop': '\u265D',
    'b_king': '\u265A',
    'b_queen': '\u265B',
    'w_checker': '\u25FC',
    'w_pawn': '\u2659',
    'w_rook': '\u2656',
    'w_knight': '\u2658',
    'w_bishop': '\u2657',
    'w_king': '\u2654',
    'w_queen': '\u2655'
}


def get_checkers():
    bw_row = [chrs['w_checker']]*8
    bw_checkers = []

    for i in range(8):
        bw_checkers.append(bw_row if i % 2 == 0 else bw_row[::-1])

    bw_checkers = np.array(bw_checkers)
    wb_checkers = bw_checkers[::-1]
    return {'W': wb_checkers, 'B': bw_checkers}


def get_board():

    def get_army(user):
        u = user.lower()
        guard = [chrs[u+'_rook'], chrs[u+'_knight'], chrs[u+'_bishop']]
        rear = guard + [chrs[u+'_king'], chrs[u+'_queen']] + guard[::-1]
        front = [chrs[u+'_pawn']]*8

        if user == 'B':
            return [rear, front]
        else:  # since white moves first
            return [front, rear]

    board = [squad for squad in get_army('B')]

    for _ in range(4):
        board.append(['0']*8)

    board += get_army('W')

    return np.array(board)


def print_board(board, checkers, user):
    chks = checkers[user]
    temp = board.copy() if user == 'W' else board.copy()[::-1]

    for i, row in enumerate(temp):
        for j, c in enumerate(row):
            print('', chks[i][j] if c == '0' else c, end='', flush=True)
        print()


if __name__ == "__main__":
    checkers = get_checkers()
    print(' '.join(checkers['W'][0]))
    board = get_board()
    user = 'B'
    print_board(board, checkers, user)