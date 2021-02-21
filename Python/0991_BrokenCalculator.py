class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        count = 0
        while Y > X:
            print(Y, X, count)
            count += 1
            if Y % 2 == 1:
                Y += 1
            else:
                Y //= 2
        return count + X-Y
