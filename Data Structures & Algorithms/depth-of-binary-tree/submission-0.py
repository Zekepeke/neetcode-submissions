# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        left_sub = self.maxDepth(root.right)
        right_sub = self.maxDepth(root.left)

        return max(left_sub, right_sub) + 1
        