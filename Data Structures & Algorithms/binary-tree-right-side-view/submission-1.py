# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Empty Root Case
        if not root:
            return []

        levels = []
        queue = deque([root])

        while queue:
            n = len(queue)
            cur_level = []
            
            for i in range(n):
                node = queue.popleft()
                cur_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            levels.append(cur_level)
        
        output = []
        for level in levels:
            output.append(level[-1])
        
        return output
        

