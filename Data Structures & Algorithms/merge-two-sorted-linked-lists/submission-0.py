# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        dummy = node = ListNode()
        
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        
        #append the remainder of the list which is not empty
        node.next = list1 or list2

        return dummy.next 

'''
In place addition of the values in first list 

new empty list 
append the element which is smaller
and keep on going till curr1 is not None and curr2 is not None 
'''
        