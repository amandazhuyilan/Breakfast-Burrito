# Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

#A region is captured by flipping all 'O''s into 'X''s in that surrounded region.

def surroundedRegions(self, board):
    # write your code here
    for i in range(len(board)):             #rows
        for j in range(len(board[0])):      #columns
            if board[0][j] == 'O':
                board[0][j] = 'D'

            if board[i][0] == 'O':
                board[i][0] = 'D'
                
            if board[i][len(board[0])-1] == 'O':
                board[i][len(board[0])-1] = 'D'
                
            if board[len(board)-1][j] == 'O':
                board[len(board)-1][j] = 'D'
                
    for i in range(1,len(board)-1):             #rows
        for j in range(1,len(board[0])-1):      #column
            if board[i][j] == 'O':
                if board[i+1][j] == 'D' or board[i][j+1] == 'D' or board[i-1][j] == 'D' or board[i][j-1] == 'D':
                    board[i][j] = 'D'

    for i in range(len(board)):             #rows
        for j in range(len(board[0])):      #columns
            if board[i][j] == 'O':
                board[i][j] = 'X'

            if board[i][j] == 'D':
                board[i][j] = 'O'

                
                    
            
           
