class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        prev = float('-inf')
        ans = []
        for i, e in enumerate(s):
            if e == c:
                prev = i
            ans.append(i-prev)
            
        prev = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i], prev-i)
        
        return ans
