class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        output = 0

        while r < n:
            diff = prices[r] - prices[l]

            if diff > 0:
                r += 1
                output = max(diff, output)
            elif diff < 0:
                l += 1
            else:
                r += 1

        return output 

