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
