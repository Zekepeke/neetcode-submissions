# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        stack_p = []
        self.list_of_descendants(root, p, stack_p)

        stack_q = []
        self.list_of_descendants(root, q, stack_q)

        for p in stack_p:
            print("P values", p.val)
        for q in stack_q:
            print("Q values", q.val)
        while stack_p and stack_q:
            if len(stack_p) > len(stack_q):
                stack_p.pop()
            elif len(stack_p) < len(stack_q):
                stack_q.pop()
            else:
                if stack_q[-1].val == stack_p[-1].val:
                    return stack_q[-1]
                else:
                    stack_p.pop()
                    stack_q.pop()

        return root

    
    def list_of_descendants(self, root, node, l):
        if not root:
            return
        l.append(root)              
        if root.val == node.val:
            return
        if root.val < node.val:
            self.list_of_descendants(root.right, node, l)
        else:
            self.list_of_descendants(root.left, node, l)

            







