#Top-Down DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount <= 0:
            return 0
        memo = {}
        result = self.dfs(coins, amount, memo)
        if result == float('inf'):
            return -1
        return result
        
    def dfs(self, coins, amount, memo):
        if amount < 0:
            return float('inf')
        if amount == 0:
            return 0
        if amount in memo:
            return memo[amount]
        
        for i in range(len(coins)):
            used_coin = 1 + self.dfs(coins, amount - coins[i], memo)
            if amount not in memo:
                memo[amount] = used_coin
            else:
                memo[amount] = min(memo[amount], used_coin)
        return memo[amount]

#Bottom-Up DP
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 