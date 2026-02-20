# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        reminder = 0
        cnt1, cnt2 = 0, 0
        while p1:
            cnt1+=1
            p1 = p1.next
        while p2:
            cnt2+=1
            p2 = p2.next

        p1, p2 = l1, l2
        prev = None

        while p1 and p2:
            sumVal = p1.val + p2.val + reminder

            if cnt1>=cnt2:
                p1.val = int(sumVal) % 10
                prev = p1
            else:
                p2.val = int(sumVal) % 10
                prev = p2

            if sumVal > 9:
                reminder = 1
            else:
                reminder = 0
            p1, p2 = p1.next, p2.next
        
        while p1:
            sumVal = p1.val + reminder
            p1.val = int(sumVal)%10
            if sumVal > 9:
                reminder = 1
            else:
                reminder = 0
            prev = p1
            p1 = p1.next
        
        while p2:
            sumVal = p2.val + reminder
            p2.val = int(sumVal)%10
            if sumVal > 9:
                reminder = 1
            else:
                reminder = 0
            prev = p2
            p2 = p2.next
        
        if reminder == 1:
            temp = ListNode()
            temp.val = 1
            prev.next = temp

        if cnt1 >= cnt2:
            return l1
        else:
            return l2
