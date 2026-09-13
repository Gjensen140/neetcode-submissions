class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l < r:
            # Mid in our window
            m = (l + r) // 2

            # Checking middle values
            if nums[m] > nums[m + 1]:
                return nums[m + 1]
            elif nums[m - 1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[r]:
                # Min must be in our right half
                l = m + 1
            else:
                # Min is in our left half
                r = m - 1

        # Only remaining value
        return nums[l]
            