class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.pos = 0
        self.res = None

        def dfs(node):
            if not node:
                return None
            dfs(node.left)
            self.pos += 1
            if self.pos == k:
                self.res = node.val
                return
            dfs(node.right)
        dfs(root)
        return self.res
