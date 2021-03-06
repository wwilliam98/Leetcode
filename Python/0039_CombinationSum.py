class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(candidates, 0, target, [])
        return self.res
        
    def backtrack(self, arr, s, t, temp):
        if s == t:
            self.res.append(temp.copy())
        if s > t:
            return
        
        for i in range(len(arr)):
            self.backtrack(arr[i:], s + arr[i], t, temp + [arr[i]])
