# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        slow = head
        fast = head.next

        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        cur = prev

        while head and cur:
            # assigning 6 next to 0
            temp1 = head.next
            head.next = cur 
            head = temp1
            # Assigning 1 next to 6
            temp2 = cur.next
            cur.next = head
            cur = temp2
