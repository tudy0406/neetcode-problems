"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodes = {}
        p1 = head
        while p1:
            nodes[p1] = Node(p1.val)
            p1 = p1.next
        
        p1 = head
        while p1:
            if p1.next:
                nodes[p1].next = nodes[p1.next]
            else:
                nodes[p1].next = None
            if p1.random:
                nodes[p1].random = nodes[p1.random]
            else:
                nodes[p1].random = None
            p1 = p1.next
        
        if head:
            return nodes[head]
        return None