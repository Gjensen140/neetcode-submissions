# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]
            
            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left[1] - right[1]) > 1 or not left[0] or not right[0]:
                return [False, 0]
            

            height = 1 + max(left[1], right[1])
            return [True, height]

        return dfs(root)[0]