class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        count = 0

        candidate = nums[0]

        for i in range(n):

            if count == 0:
                candidate = nums[i]

            if candidate == nums[i]:
                count += 1
            else:
                count -= 1

            

        
        return candidate