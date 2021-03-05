class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.max = 0
        self.backtrack(arr, "")
        return self.max
        
    def backtrack(self, arr, s):
        if len(s) == len(set(s)):
            self.max = max(self.max, len(s))
        else:
            return
        
        for i in range(len(arr)):
            self.backtrack(arr[i+1:], s + arr[i])
