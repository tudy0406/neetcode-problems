# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def __init__(self):
        self.maxDiameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            self.maxDiameter = max(l+r, self.maxDiameter)
            return 1 + max(l,r)
        depth(root)
        return self.maxDiameter