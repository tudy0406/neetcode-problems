# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head
        if p1.next != None and p1.next.next != None:
            p1, p2 = p1.next.next, p2.next
        else:
            return False
        while True:
            if p1 == p2 and p1 != None and p2 != None:
                return True
            
            if p1.next == None or p1.next.next == None or p2.next == None:
                return False

            p1 = p1.next.next
            p2 = p2.next