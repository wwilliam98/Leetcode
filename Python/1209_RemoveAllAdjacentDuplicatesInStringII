class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        count = []
        stack = ""
        for i in range(len(s)):
            if i == 0 or not stack or s[i] != stack[-1]: #if not adjacent duplicates, put everything in stack
                count.append(1)
                stack = stack + s[i]

            else:
                recount = count.pop() + 1 #if adjacent, add count by 1
                if recount == k:
                    stack = stack[:len(stack)-1]
                    
                else:
                    count.append(recount)
        
        return "".join(map(lambda x, y: x * y, count, stack)) #multiply count and string and join them together
