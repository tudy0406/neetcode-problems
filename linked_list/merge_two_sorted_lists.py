# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        l3 = None
        head = None
        while l1 and l2:
            if l1.val < l2.val:
                if not l3:
                    l3 = l1
                    head = l1
                else:
                    l3.next = l1
                    l3 = l3.next
                l1 = l1.next
            else:
                if not l3:
                    l3 = l2
                    head = l2
                else:
                    l3.next = l2
                    l3 = l3.next
                l2 = l2.next
        while l1:
            if not l3:
                l3 = l1
                head = l1
            else:
                l3.next = l1
                l3 = l3.next
            l1 = l1.next
        while l2:
            if not l3:
                l3 = l2
                head = l2
            else:
                l3.next = l2
                l3 = l3.next
            l2 = l2.next
        return head
        