
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        # Checking ends
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r

        while l <= r:
            # Mid in our window
            m = (l + r) // 2

            # Checking middle values
            if nums[m] == target:
                return m
            elif nums[m] >= nums[l]:
                # left half is sorted
                # Target is in left half
                if target >= nums[l] and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                # Right half is sorted
                # Target is in right half
                if target <= nums[r] and target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            


        # Only remaining value
        return -1
            