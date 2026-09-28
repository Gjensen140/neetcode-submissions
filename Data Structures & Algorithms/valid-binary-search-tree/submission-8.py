# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Base Case: Leaf node
        if not root.left and not root.right:
            return True

        prev = float('-inf')

        def inOrder(node):
            nonlocal prev
            
            if not node:
                return True

            # 1. Check left subtree
            if not inOrder(node.left):
                return False

            # 2. Check current node against previous node
            if node.val <= prev:
                return False
            prev = node.val

            # 3. Check right subtree
            return inOrder(node.right)

        return inOrder(root)