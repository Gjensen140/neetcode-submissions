# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Empty Root
        if not root:
            return []

        result = []
        # 2. Initialize the queue with the root node
        queue = deque([root])
        
        # 3. Process the tree level by level
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            current_level = []
            
            # Iterate exactly through the nodes belonging to this level
            for _ in range(level_size):
                node = queue.popleft()  # Remove node from the front
                current_level.append(node.val)
                
                # Enqueue the children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            # Append the completed level to our final result
            result.append(current_level)
            
        return result

        