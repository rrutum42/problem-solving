# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # one pass
        dummy = ListNode(0, head)
        second = dummy
        first = head

        for i in range(n):
            first = first.next
        
        while first:
            second = second.next
            first = first.next

        second.next = second.next.next
        return dummy.next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         # two passes
#         ln = 0 
#         curr = head
#         while curr:
#             curr = curr.next
#             ln += 1

#         print(f"Length of linked list: {ln}")
        
#         remove_index = ln - n
#         if remove_index == 0:
#             return head.next

#         curr = head
#         for i in range(ln - 1):
#             if (i+1) == remove_index:
#                 curr.next = curr.next.next
#                 break
#             curr = curr.next 
            
#         return head

