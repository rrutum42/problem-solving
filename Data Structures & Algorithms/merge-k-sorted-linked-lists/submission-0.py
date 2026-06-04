# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        for i in range(1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i],lists[i-1])
        return lists[-1]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        dummy = node = ListNode(0)

        while list1 and list2:
            if list1.val<=list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        dummy.next = list1 or list2
            
        return node.next

        
'''
merge two list together and then keep on merging till we have 1 list
'''