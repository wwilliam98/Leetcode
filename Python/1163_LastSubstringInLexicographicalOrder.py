def lastSubstring(self, s: str) -> str:
        if len(s) == 1:
            return s
        
        prev = s
        for i in range(1, len(s)):
            if s[i:] > prev:
                prev = s[i:]
        return prev
