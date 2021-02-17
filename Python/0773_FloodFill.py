class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        color = image[sr][sc]
        if color == newColor:
            return image
        
        self.dfs(image, sr, sc, newColor, color)
        return image
                    
    def dfs(self, img, i, j, new, color):
        if i < 0 or j < 0 or len(img) <= i or len(img[0]) <= j or img[i][j] != color:
            return
        
        img[i][j] = new
        self.dfs(img, i+1, j, new, color)
        self.dfs(img, i-1, j, new, color)
        self.dfs(img, i, j+1, new, color)
        self.dfs(img, i, j-1, new, color)
