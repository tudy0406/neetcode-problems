# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
                
            tail.next = list1 if list1 else list2
            return dummy.next

        lists = [l for l in lists if l]

        if not lists:
            return None
        
        for i in range(1, len(lists)):
            lists[i] = merge2Lists(lists[i-1], lists[i])
        
        return lists[-1]
