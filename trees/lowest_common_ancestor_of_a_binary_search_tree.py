# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   

    def isSameTree(self, p : Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.isSame = False
        def traversal(p1: Optional[TreeNode], q1: Optional[TreeNode]) -> None:
            if not p1:
                return None
            traversal(p1.left, q1)
            traversal(p1.right, q1)
            if self.isSameTree(p1, q1):
                self.isSame = True
        traversal(root, subRoot)
        return self.isSame
        