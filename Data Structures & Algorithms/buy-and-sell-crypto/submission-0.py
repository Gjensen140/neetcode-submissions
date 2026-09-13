class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        if n <= 1:
            return 0
        
        output = 0
        l = 0
        r = 1

        while r < n:
            profit = prices[r] - prices[l]
            if profit < 0:
                l += 1
                r = l + 1
            elif profit > output:
                output = profit
                r += 1
            else:
                r += 1 

        return output