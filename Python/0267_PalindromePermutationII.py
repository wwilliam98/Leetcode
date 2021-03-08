class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        d = collections.Counter(s)
        mid = [k for k, v in d.items() if v % 2 == 1]
        if len(mid) > 1:
            return []
        mid = '' if not mid else mid[0] #the only one letter (which can only be placed in the middle)
        halfS = ''.join([k * (v//2) for k, v in d.items()]) #Strings of letter that is more than 2
        halfS = [letter for letter in halfS]
        visited = [False] * len(halfS)
        
        def backtracking(s, temp):
            if len(halfS) == len(temp):
                res.append(temp + mid + temp[::-1])
                return

            for i in range(len(s)):
                if visited[i] or (i > 0 and halfS[i] == halfS[i-1] and not visited[i-1]): #halfS[i] == halfS[i-1] and not visited[i-1] means so that there is no repeatation after the second recursion
                    continue
                    
                visited[i] = True
                backtracking(s, temp + s[i])
                visited[i] = False
        
        res = []
        backtracking(halfS, "")
        return res
