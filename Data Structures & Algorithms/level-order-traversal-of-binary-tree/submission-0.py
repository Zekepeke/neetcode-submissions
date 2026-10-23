# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []
        if not root:
            return res
        queue.append(root)
        while queue:
            length = len(queue)
            temp_list = []
            while length > 0:
                cur_node = queue.popleft()

                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)

                temp_list.append(cur_node.val)
                length -= 1
            if temp_list:
                res.append(temp_list)

        return res
        