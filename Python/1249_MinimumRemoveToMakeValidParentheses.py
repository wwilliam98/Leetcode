#store string as list
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_par = []
        s = list(s)
        
        for idc, char in enumerate(s):
            if char == '(':
                open_par.append(idc)
            elif char == ')':
                if open_par:
                    open_par.pop()
                else:
                    s[idc] = ""
                    
            
        while open_par:
            s[open_par.pop()] = ""
            
        return "".join(s)

#Two Pass solution
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ""
        temp = ""
        stack = []
        for l in s:
            if l == "(":
                stack.append("(")
                temp += "("
            elif l == ")":
                if stack:
                    stack.pop()
                    temp += ")"
            else:
                temp += l
        
        stack = []
        for l in temp[::-1]:
            if l == ")":
                stack.append(")")
                res = ")" + res
            elif l == "(":
                if stack:
                    stack.pop()
                    res = "(" + res
            else:
                res = l + res
                
        return res
