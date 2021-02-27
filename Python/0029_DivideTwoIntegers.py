class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31
        HALF_MIN_INT = -1073741824  # MIN_INT // 2

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        negatives = 2
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor

        doubles = []
        powersOfTwo = []

        powerOfTwo = 1
        while divisor >= dividend:
            doubles.append(divisor)
            powersOfTwo.append(powerOfTwo)
            if divisor < HALF_MIN_INT:
                break
            divisor += divisor # Double divisor
            powerOfTwo += powerOfTwo

        quotient = 0
        for i in range(len(doubles)-1, -1, -1):
            if doubles[i] >= dividend:
                quotient += powersOfTwo[i]
                dividend -= doubles[i]
        
        if negatives != 1:
            return quotient
        else:
            return -quotient
