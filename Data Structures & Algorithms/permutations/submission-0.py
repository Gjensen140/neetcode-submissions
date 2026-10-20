class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n == 0:
            return [[]]
        
        # Create subproblem
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            m = len(p)
            for i in range(m + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)

        return res