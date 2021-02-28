class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        arr = []
        curr = ""
        d = {}
        for i in paragraph:
            if i.isalpha():
                curr += i.lower()
            else:
                if curr:
                    arr.append(curr)
                curr = ""
        if curr:
            arr.append(curr)
                
        for i in arr:
            if i in banned:
                continue
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
                
        res = ""  
        mx = 0
        for k, v in d.items():
            if v > mx:
                res = k
                mx = v
        return res
