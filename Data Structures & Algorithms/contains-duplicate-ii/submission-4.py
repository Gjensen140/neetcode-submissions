class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        seen = set()
        l = 0
        r = 0

        k = min(n, k)

        for _ in range(k):
            
            if nums[r] in seen:
                return True
            
            seen.add(nums[r])
            r += 1

        while r < n:
            if nums[r] in seen:
                return True

            seen.add(nums[r])
            seen.remove(nums[l])
            r += 1 
            l += 1

        return False