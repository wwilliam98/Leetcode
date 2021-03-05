#more intuitive way to do it (slower though)
class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        self.backtrack(n, 1, [])
        return self.count
        
    def backtrack(self, N, idx, temp):
        if len(temp) == N:
            self.count += 1
            return
        
        for i in range(1, N+1):
            if i not in temp and (i % idx == 0 or idx % i == 0):
                temp.append(i)
                self.backtrack(N, idx+1, temp)
                temp.pop()

#using hashmap (visited)
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
