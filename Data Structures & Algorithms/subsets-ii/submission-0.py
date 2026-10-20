class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        output = set()
        cur = []

        def dfs(i):
            output.add(tuple(sorted(cur).copy()))
            
            if i == n:
                return

            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            dfs(i + 1) 

        dfs(0)

        return list(output)