from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        counts = defaultdict(int)

        counts[0] += 1
        cur = 0
        output = 0

        for i in range(n):
            cur += nums[i]
            diff = cur - k

            output += counts.get(diff, 0)

            counts[cur] += 1

        return output