

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
from email.policy import default
import re


class Solution:
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        #  this problem can be solved utilizing the same method used in finding the level order traversal of a binary tree
        # This time however there is a small twist to it
        # It would be really easy to just put the right child of the each node into the queue but that wouldn't really work
        #
