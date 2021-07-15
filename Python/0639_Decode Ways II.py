class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        #Set up base Case for dynamic Programming
        dp = [1] * (len(s) + 1)
        if s[0] == "*":
            dp[1] = 9
        elif s[0] == "0":
            dp[1] = 0
        else:
            dp[1] = 1

        for i in range(1, len(s)):
            if s[i] == "*": #if its a *
                dp[i + 1] = (dp[i] * 9) % MOD #Regular Single number (AB)
                #For J(10) and above, dp[i-1] is from the previous alphabet count
                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % MOD

                elif s[i - 1] == "2":
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % MOD

                elif s[i - 1] == "*":
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % MOD

            else: #if its a number
                if s[i] != "0": #if the number is 0, set dp to the previous ways
                    dp[i + 1] = dp[i]
                else:
                    dp[i + 1] = 0

                if s[i - 1] == "1":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD

                elif s[i - 1] == "2" and s[i] <= "6":
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD

                elif s[i - 1] == "*":
                    if s[i] <= "6":
                        dp[i + 1] = (dp[i + 1] + 2 * dp[i - 1]) % MOD
                    else:
                        dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
        return dp[-1]
