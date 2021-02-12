class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = mx = 0
        for i, e in enumerate(arr):
            mx = max(mx, arr[i])
            if i == mx:
                res += 1
        return res
