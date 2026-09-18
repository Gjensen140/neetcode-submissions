# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        l = None
        r = None

        if p.val < q.val:
            l = p
            r = q
        else:
            l = q
            r = p
        
        while True:
            if (root.val < l.val):
                root = root.right
            elif (root.val > r.val):
                root = root.left
            else:
                return root