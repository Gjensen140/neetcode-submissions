class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        l = 0
        output = 0

        for r in range(n):
            while prices[r] < prices[l]:
                l += 1
            else:
                diff = prices[r] - prices[l]
                output = max(output, diff)

        return output
