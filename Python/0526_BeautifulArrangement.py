class Solution:
    def countArrangement(self, n: int) -> int:
        self.visited = [False] * (n+1)
        self.count = 0
        self.backtrack(n, 1)
        return self.count
        
    def backtrack(self, N, idx):
        if idx > N:
            self.count += 1
            return
            
        for i in range(1, N+1):
            if not self.visited[i] and idx % i == 0 or i % idx == 0:
                self.visited[i] = True
                self.backtrack(N, idx + 1)
                self.visited[i] = False
