class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        # Only one house to rob
        if n == 1:
            return nums[0]
         
        opt = [nums[0]] * n

        opt[1] = max(nums[1], opt[0])

        for i in range (2, n):
            temp = opt[i - 2] + nums[i]
            opt[i] = max(opt[i - 1], temp)

        return opt[n-1]
