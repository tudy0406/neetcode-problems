# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1, cnt = head, 0
        while p1:
            cnt+=1
            p1 = p1.next
        
        target, count, p1, prev= cnt - n, 0, head, None
        while count < target:
            prev = p1
            p1 = p1.next
            count += 1
        
        if target == 0:
            head = head.next
            return head
        else:
            prev.next = p1.next
            p1 = None
        return head
            