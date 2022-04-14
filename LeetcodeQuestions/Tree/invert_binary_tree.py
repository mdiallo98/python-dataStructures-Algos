# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            levels = []
            queue_lenght = len(queue)
            for i in range(queue_lenght):
                node = queue.popleft()
                if node:
                    levels.append(node.val)
                    queue.append(node.right)
                    queue.append(node.left)
            if levels:
                result.append(levels)
        return result
