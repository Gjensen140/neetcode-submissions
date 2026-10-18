# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = ListNode(0)
        output = head

        while list1 and list2:
            if list1.val >= list2.val:
                output.next = list2
                list2 = list2.next
            else:
                output.next = list1
                list1 = list1.next
            
            output = output.next

        if list1:
            output.next = list1
        else:
            output.next = list2
        

        return head.next