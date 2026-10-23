# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        upper_bound = float('inf')
        lower_bound = float('-inf')


        return self.validate_tree(root, lower_bound, upper_bound)
    
    def validate_tree(self, root, lower_bound, upper_bound):
        if not root:
            return True
        res = False
        if lower_bound < root.val and root.val < upper_bound:
            res = True
        
        sub_left = self.validate_tree(root.left, lower_bound, root.val)
        sub_right = self.validate_tree(root.right, root.val, upper_bound)
        return res and sub_left and sub_right
            
        