# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def __init__(self):
        self.isTreeBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            
            left = depth(root.left)
            right = depth(root.right)

            if abs(left-right) > 1:
                self.isTreeBalanced = False

            return 1+max(left, right)

        depth(root)
        return self.isTreeBalanced