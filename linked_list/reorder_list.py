# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        
        prev = None
        curr = p1.next
        p1.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            

        l1 = head
        l2 = prev
        while l2 and l1:
            l12, l22 = l1.next, l2.next
            l1.next = l2
            l2.next = l12
            l1, l2 = l12, l22