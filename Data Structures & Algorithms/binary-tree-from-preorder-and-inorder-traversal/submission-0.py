# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Use an iterator over preorder to naturally fetch the next root element
        preorder_iter = iter(preorder)
        
        def helper(left_bound: int, right_bound: int) -> Optional[TreeNode]:
            # Base case: if the boundary bounds no elements, return None
            if left_bound > right_bound:
                return None
            
            # The next element in preorder traversal is always the root of the current subtree
            root_val = next(preorder_iter)
            root = TreeNode(root_val)
            
            # Find the split point in the inorder array
            root_idx = inorder_map[root_val]
            
            # CRITICAL: Always construct the left subtree before the right subtree 
            # because the preorder sequence traverses the left child next.
            root.left = helper(left_bound, root_idx - 1)
            root.right = helper(root_idx + 1, right_bound)
            
            return root
            
        return helper(0, len(inorder) - 1)