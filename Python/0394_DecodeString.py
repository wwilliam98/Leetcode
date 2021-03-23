class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currstring = ""
        currnum = 0
        
        for c in s:
            if c == "[":
                stack.append(currnum)
                stack.append(currstring)
                currnum = 0
                currstring = ""
            elif c == "]": #DFS = stack.pop
                string = stack.pop()
                num = stack.pop()
                currstring = string + currstring * num
            elif c.isnumeric():
                currnum = currnum * 10 + int(c)
            else:
                currstring += c
        return currstring
