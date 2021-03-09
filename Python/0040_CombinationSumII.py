class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        self.res = []
        self.backtracking(candidates, target, [], 0)
        return self.res
        
    def backtracking(self, arr, target, temp, idx):
        if target == 0:
            self.res.append(temp.copy())
            return
        
        for i in range(idx, len(arr)): #not the same as backtrack(arr[i+1]) because it removed the duplicated number, this doesnt
            if i > idx and (arr[i] == arr[i-1]): #To remove duplicates
                continue
                
            if target - arr[i] < 0: #Optimization, if remaining is already less than 0, no need to continue because arr is sorted
                break
                
            self.backtracking(arr, target-arr[i], temp + [arr[i]], i + 1)
