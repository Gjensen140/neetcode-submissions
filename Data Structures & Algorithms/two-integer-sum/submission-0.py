class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        n = len(nums)

        for i in range(n):
            dif = target - nums[i]
            if dif in seen:
                return [seen[dif], i]
            else:
                seen[nums[i]] = i
        
        