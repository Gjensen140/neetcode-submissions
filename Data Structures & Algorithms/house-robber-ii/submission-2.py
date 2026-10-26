class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n < 4:
            return max(nums)

        first = self.help(nums[:-1])
        last = self.help(nums[1:])
        return max(first, last)
    
    def help(self, nums):
        n = len(nums)
        rob1 = nums[0]
        rob2 = max(nums[0], nums[1])

        for i in range(2, n):
            cur = max(nums[i] + rob1, rob2)
            rob1 = rob2
            rob2 = cur

        return rob2
