class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.finder(board, i, j, word):
                    return True
        return False
    
    def finder(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or j < 0 or len(board) <= i or len(board[0]) <= j or board[i][j] != word[0]:
            return False
        
        temp = board[i][j]
        board[i][j] = 1
        ret = self.finder(board, i+1, j, word[1:]) or self.finder(board, i-1, j, word[1:]) or self.finder(board, i, j+1, word[1:]) or self.finder(board, i, j-1, word[1:])
        board[i][j] = temp
        return ret
