# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root.left and not root.right:
            return root.val

        count = 0

        def inorder(node, k):
            nonlocal count

            left = float('-inf')
            right = float('-inf')

            if node.left:
                left = inorder(node.left, k)
            
            count = count + 1
            
            
            if count == k:
                return node.val

            if node.right:
                right = inorder(node.right, k)
            
            return max(left, right)
        
        output = inorder(root, k)
        return output