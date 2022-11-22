class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        builder = s

        for i, val in enumerate(s):
            if stack and stack[-1][0] in ["(", ")"]:
                stack.pop()
