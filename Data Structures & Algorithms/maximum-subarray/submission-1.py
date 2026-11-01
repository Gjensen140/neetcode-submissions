class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sub = [nums[0]] * n

        # sub[i] = maximum subarray up to i (including i)

        for i in range(1, n):
            sub[i] = max(sub[i - 1] + nums[i], nums[i])

        return max(sub)