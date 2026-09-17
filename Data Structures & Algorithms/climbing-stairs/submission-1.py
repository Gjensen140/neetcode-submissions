class Solution:
    def climbStairs(self, n: int) -> int:
        # Base Cases

        nums = [1, 1]
        i = 2

        while i <= n:
            temp = nums[1]
            nums[1] = temp + nums[0]
            nums[0] = temp
            i += 1
            
        
        return nums[1]