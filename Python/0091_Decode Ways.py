class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s) + 1)

        if s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(1, len(s)):
            if s[i] == "0":
                dp[i+1] = 0
            else:
                dp[i+1] = dp[i]

            if s[i-1] == "1":
                dp[i+1] = dp[i+1] + dp[i-1]

            elif s[i-1] == "2" and s[i] <= "6":
                dp[i+1] = dp[i+1] + (dp[i-1])

        return dp[-1]
