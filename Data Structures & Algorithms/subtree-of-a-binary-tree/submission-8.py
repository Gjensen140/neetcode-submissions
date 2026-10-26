# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True 
        if not root:
            return False
        
        
        # We found the start of a potential match
        if (self.sameTree(root, subRoot)):
            return True

        left_search = False
        right_search = False


        left_search = self.isSubtree(root.left, subRoot)
        right_search = self.isSubtree(root.right, subRoot)

        return left_search or right_search
    
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            left = self.sameTree(root.left, subRoot.left)
            right = self.sameTree(root.right, subRoot.right)
            return left and right
        
        return False
