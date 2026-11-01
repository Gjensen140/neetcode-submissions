'''
Since the array is always of odd length:
- If current m is even and nums[m] == nums[m + 1]: recurse right
- If current m is odd and nums[m] == nums[m - 1]: recurse right
- Else: recurse left 
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            m = (l + r) // 2

            if (m == 0 or m == n-1 or
                nums[m] != nums[m + 1] and nums[m] != nums[m - 1]
            ):
                return nums[m]
            elif (nums[m] == nums[m + 1] and m%2 == 0 or
                nums[m] == nums[m - 1] and m%2 == 1
            ):
                l = m + 1
            else:
                r = m - 1

        return nums[r]
