class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        cur = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                
                if coin > i:
                    continue
                
                count = 1 + dp[i - coin]
                dp[i] = min(dp[i], count)
        
        if dp[amount] == float('inf'):
            return -1

        return dp[amount]
        