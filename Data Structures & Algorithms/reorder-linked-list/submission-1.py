# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        #merge both 
        curr, second = head, prev
        while second:
            """
            [1,2,3]
            [5,4]
            """
            x, y = curr.next, second.next
            curr.next = second
            second.next = x
            curr, second = x, y
            

        
"""
2 pointers
get the length of the list first, 
maintain 2 pointers -> 1 for first half of list and one for the second half
second half needs to be reversed in order to use it
then just read the elements alternatively and insert them in middle

"""