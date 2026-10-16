class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        output = []

        cur = []
        def dfs(i):
            if i >= n or (sum(cur) > target):
                return
            elif sum(cur) == target:
                output.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i)

            cur.pop()
            dfs(i+1)
        
        dfs(0)
        return output
                