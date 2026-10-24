class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        nums = sorted(nums)
        output = []
        prev_i = float('-inf')


        for i in range(n):

            if nums[i] == prev_i:
                continue
            if nums[i] > 0:
                break

            l = i + 1
            r = n - 1
            prev_l = float('-inf')
            prev_r = float('-inf')

            while l < r:
                # Skipping existing solutions
                if nums[r] == prev_r:
                    r -= 1 
                    continue
                if nums[l] == prev_l:
                    l += 1
                    continue
                
                total = nums[i] + nums[l] + nums[r]

                # We found a new solution
                if total == 0:
                    output.append([nums[i], nums[l], nums[r]])
                    prev_l = nums[l]
                    prev_r = nums[r]
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1
            
            prev_i = nums[i]

        return output