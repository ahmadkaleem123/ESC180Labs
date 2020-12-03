'''
 X | O | X
---+---+---
 O | O | X    
---+---+---
   | X | 
'''

import random 


def print_board_and_legend(board):
    for i in range(3):
        line1 = " " +  board[i][0] + " | " + board[i][1] + " | " +  board[i][2]
        line2 = "  " + str(3*i+1)  + " | " + str(3*i+2)  + " | " +  str(3*i+3) 
        print(line1 + " "*5 + line2)
        if i < 2:
            print("---+---+---" + " "*5 + "---+---+---")
        
    
    
def make_empty_board():
    board = []
    for i in range(3):
        board.append([" "]*3)
    return board

def findcoord(square_num):
    coord = []
    row = ((square_num-1)//3)
    col = square_num - 3*row - 1
    coord.append(row)
    coord.append(col)
    return coord

def put_in_board(board,mark,square_num):
    coord = findcoord(square_num)
    board[coord[0]][coord[1]] = mark

def get_free_squares(board):
    empty = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(board[i][j] == " "):
                empty.append([i,j])
    return empty

def make_random_move(board,mark):
    empty = get_free_squares(board)
    r = int(len(empty) * random.random())
    board[empty[r][0]][empty[r][1]] = mark
    
def is_row_all_marks(board, row_i, mark):
    if(board[row_i][0] == mark and board[row_i][1] == mark and board[row_i][2] == mark):
        return True
    else:
        return False

def is_col_all_marks(board, col_i, mark):
    is_all_mark = True
    for i in range(3):
        if board[i][col_i] != mark:
            is_all_mark = False

    return is_all_mark

def is_diag_all_marks(board, mark):
    if(board[0][0] == mark and board[1][1] == mark and board[2][2] == mark):
        return True
    elif (board[0][2] == mark and board[1][1] == mark and board[2][0] ==mark):
        return True
    else:
        return False
    
def is_win(board, mark):
    win = False
    for i in range(3):
        if(is_row_all_marks(board, i, mark) == True):
            win = True
        if(is_col_all_marks(board, i, mark) == True):
            win = True
    if(is_diag_all_marks(board, mark) == True):
        win = True    

    return win
def smartcheck_not_lose(board, mark):
    empty = get_free_squares(board)
    for i in range(len(empty)):
        board[empty[i][0]][empty[i][1]] = mark
        if is_win(board, mark) == False:
            board[empty[i][0]][empty[i][1]] = " "
        else:
            if(mark == "X"):
                board[empty[i][0]][empty[i][1]] = "O"
            else:
                board[empty[i][0]][empty[i][1]] = "X"
            return True
    return False

def smartcheck(board, mark):
    empty = get_free_squares(board)
    for i in range(len(empty)):
        board[empty[i][0]][empty[i][1]] = mark
        if is_win(board, mark) == False:
            board[empty[i][0]][empty[i][1]] = " "
        else:
            return True
    return False
            
    #r = int(len(empty) * random.random())
    board[empty[r][0]][empty[r][1]] = mark
def main():
    gameover = False
    count = 0
    winner = "tie"
    while(gameover == False and count<9):
        if count % 2 == 0:
            a = int(input("Enter the coordinate for X: "))
            # a = int(a)
            put_in_board(board, "X", a)
            gameover = is_win(board, "X")
            if(gameover == True):
                winner = "X"
                
        else:
            #a = int(input("Enter the coordinate for O: "))
            #a = int(a)
            
            move = smartcheck(board, "O")
            if move == False:
                move2 = smartcheck_not_lose(board, "X")
                if move2 == False:
                    make_random_move(board, "O")
            
            #put_in_board(board, "O", a)
            gameover = is_win(board, "O")
            if gameover == True:
                winner = "O"
        
        print_board_and_legend(board)
        if winner == "X":
            print("X wins!")
        elif winner == "O":
            print("O wins!")
        count += 1
    if (winner == "tie"):
        print("Tie!")
if __name__ == '__main__':
    board = make_empty_board()
    print_board_and_legend(board)    
    
    print("\n\n")
    
    """ board = [["O", "X", "X"],
             [" ", "X", " "],
             [" ", "O", " "]]
    
    put_in_board(board, "X", 7)
    print_board_and_legend(board)  
    print(get_free_squares(board)) """
   
    main()    

            

