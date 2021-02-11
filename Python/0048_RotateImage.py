class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])): #Diagonal of the matrix
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        #reverse the matrix
        for i in range(len(matrix[0])):
            matrix[i].reverse()
