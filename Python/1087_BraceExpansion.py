class Solution:
    def expand(self, s: str) -> List[str]:
        self.res = []
        self.perm(s, "")
        self.res.sort()
        return self.res
        
    def perm(self, s, word):
        if not s:
            self.res.append(word)
            
        else:
            if s[0] == "{":
                i = s.find("}")
                for letter in s[1:i].split(","):
                    self.perm(s[i+1:], word + letter)
        
            else:
                self.perm(s[1:], word + s[0])
