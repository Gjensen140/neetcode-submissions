class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        #i: Index of the current element
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            # Include current index
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return res
