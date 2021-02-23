class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            if not self.isRowValid(board[i]):
                return False
            
            if not self.isColValid(board, i):
                return False
        
        for r in range(0,len(board),3):            #0, 3, 6
            for c in range(0, len(board[0]), 3):   #0, 3, 6
                if not self.isSquareValid(board, r, c):
                    return False
                
        return True
        
    def isRowValid(self, row = []):
        seen = set()
        
        for col in range(9):
            if row[col] == ".":
                continue
            
            if row[col] in seen:
                return False
            
            seen.add(row[col])
        return True
    
    
    def isColValid(self, board, col):
        seen = set()
        
        for row in range(9):
            if board[row][col] == ".":
                continue
            
            if board[row][col] in seen:
                return False
             
            seen.add(board[row][col])
        return True
    
    def isSquareValid(self, board, row, col):
        seen = set()
        
        for r in range(row, row+3):     #0-2, 3-5, 6-8
            for c in range(col, col+3): #0-2, 3-5, 6-8
                if board[r][c] == ".":
                    continue
                    
                if board[r][c] in seen:
                    return False
                
                seen.add(board[r][c])
        return True
