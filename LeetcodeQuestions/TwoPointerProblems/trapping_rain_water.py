class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        l, r = 0, len(height) - 1
