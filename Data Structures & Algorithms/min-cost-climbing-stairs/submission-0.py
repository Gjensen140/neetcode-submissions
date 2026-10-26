class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        opt = [0] * n
        opt[0] = 0
        opt[1] = 0

        for i in range(2, n):
            opt[i] = min(opt[i-1] + cost[i - 1], opt[i - 2] + cost[i - 2])

        return min(opt[-2] + cost[-2], opt[-1] + cost[-1])