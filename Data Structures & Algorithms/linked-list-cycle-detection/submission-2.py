# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Empty Case
        if not head:
            return False
            
        slow = head
        fast = head.next

        while fast and slow:
            if slow == fast:
                return True
            
            if not fast.next:
                return False 
            
            fast = fast.next.next
            slow = slow.next
            

        
        return False