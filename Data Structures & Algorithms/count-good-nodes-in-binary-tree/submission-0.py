# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, largest):
            
            output = 0

            # We found a good node
            if node.val >= largest:
                output += 1
                largest = node.val
            
            left = dfs(node.left, largest) if node.left else 0
            right = dfs(node.right, largest) if node.right else 0

            return (output + left + right)


            
        return dfs(root, root.val)
