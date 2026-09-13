class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Prefix and suffix to track info about position i
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        # Passing through
        for i in range(1, n):
            ind = -1 * i
            suffix[ind - 1] = suffix[ind] * nums[ind]
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # Handling the ends
        suffix[0] = suffix[1] * nums[1]
        prefix[-1] = prefix[-2] * nums[-2]

        output = [0] * n
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output