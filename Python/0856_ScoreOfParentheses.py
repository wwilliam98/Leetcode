class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = [0]
        
        for i in S:
            if i == "(":
                stack.append(0)
            elif i == ")":
                last = stack.pop()
                secondLast = stack.pop()
                stack.append(secondLast + max(2*last, 1))
        
        return stack.pop(0)
