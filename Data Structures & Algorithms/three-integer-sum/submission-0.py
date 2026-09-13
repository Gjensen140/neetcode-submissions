class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = []
        nums.sort()
        for i in range(n - 2):
            # First number can't be positive in sorted array
            if nums[i] > 0:
                break
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                combined = -1 * (nums[l] + nums[r])
                if nums[i] == combined:
                    # They sum to 0
                    output.append([nums[i], nums[l], nums[r]])
                    # Skip duplicate values for second and third elements
                    while l < r and nums[l] == nums[l+1]: 
                        l += 1
                    while l < r and nums[r] == nums[r-1]: 
                        r -= 1
                    r -= 1
                    l += 1
                elif nums[i] > combined:
                    r -= 1
                else:
                    l += 1
            
        return output