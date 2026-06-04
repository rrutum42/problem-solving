# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''
        # O(n.k)
        if len(lists) == 0:
            return None

        for i in range(1,len(lists)):
            lists[i] = self.mergeTwoLists(lists[i],lists[i-1])
        return lists[-1]
        '''
        '''
        We can use merge sort here to reduce to O(n.logk)
        '''
        if not lists or len(lists) == 0 :
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1,l2))
            lists = merged_lists
        return lists[0]

    
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