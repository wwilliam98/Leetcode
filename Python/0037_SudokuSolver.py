class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def valid_num(board, position, num):
            r, c = position
            #check row
            for i in range(len(board[0])):
                if board[i][c] == num and i != r:
                    return False

            #check col
            for i in range(len(board)):
                if board[r][i] == num and i != c:
                    return False

            #check grid
            box_x = c // 3
            box_y = r // 3

            for i in range(box_y*3, box_y*3 + 3):
                for j in range(box_x*3, box_x*3 + 3):
                    if board[i][j] == num and (i, j) != (r, c):
                        return False

            return True

        def find_empty(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == ".":
                        return (i, j) #return (row, col)
            return False
        
        #Starting Recursion
        find = find_empty(board)
        if not find: #If everything is already filled
            return True
        
        row, col = find
        for n in range(1, 10):
            if valid_num(board,(row, col), str(n)):
                board[row][col] = str(n)
                
                if self.solveSudoku(board): #when everything is already filled, return the board
                    return board
                
                board[row][col] = "."
