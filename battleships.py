"""
    Battleships in python
"""

import numpy as np

BLACK_SQUARE = '\u2B1B'
WHITE_SQUARE = '\u2B1C'

def create_board(size=10):
    """
    creates board for battleship

    Args:
        size (int, optional): Size of board = size x size Defaults to 10.
    """
    row = [BLACK_SQUARE]*size
    board = []
    for _ in range(size):
        board.append(row)
    
    board = np.array(board)        
    return board

def print_board(board):
    """
    prints out battleship board
    
    Args:
        board (list of lists): represents battleship board
                               each character represents a square on the board
                               and can either be empty or contain a ship
    """
    for row in board:
        print(''.join(row))
            
def add_ship(board, x=0,y=0, size=2, orientation='E'):
    """
    adds a ship to the battleship board
    
    Args:
        board (_type_): battleship board
        x (int, optional): x position of ship on board. Defaults to 0.
        y (int, optional): y position of ship on board. Defaults to 0.
        size (int, optional): size of ship. Defaults to 2.
        orientation (str, optional): orientation of ship. Defaults to 'E'.
    """
    if x<0 or y<0 or x>len(board)-1 or y>len(board)-1:
        print(f'({x}, {y}) is an invalid position for a ship')
        return
       
    x_finish = x
    y_finish = y
    
    # calculate finish position of ship
    if orientation=='E':
        y_finish +=size
    elif orientation == 'S':
        x_finish +=size
    
    # check ship will fit on board
    if x_finish>len(board)-1 or y_finish>len(board)-1:
        print(f'A ship of size {size} won\'t fit in that position.')
        return

    if np.isin(board[x:x_finish+1, y:y_finish+1],WHITE_SQUARE).any():
        print('There is already a ship there')
        return
    
    # add ship    
    print(x, x_finish)
    print(y, y_finish)
    
    if orientation == 'E':
        board[x, y:y_finish] = WHITE_SQUARE
    elif orientation == 'S':
        board[x:x_finish, y] = WHITE_SQUARE
    
    return board

new_board = create_board()


add_ship(new_board, 2, 2, 4, 'E')
add_ship(new_board, 5, 3, 4, 'S')
print_board(new_board)
