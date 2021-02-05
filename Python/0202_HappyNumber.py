class Solution:
    def isHappy(self, n: int) -> bool:
        def nextNumber(num):
            s = 0
            while num:
                s += (num%10) ** 2
                num = num // 10
            return s
            
        seen = []
        while n != 1:
            if n in seen:
                return False
            seen.append(n)
            n = nextNumber(n)
        return True
