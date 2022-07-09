class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_removal = set()
        stack = []

        for i in range(len(s)):

            if s[i] not in "()":
                continue
            if s[i] == "(":
                stack.append(i)
            elif not stack:
                index_removal = set()
            else:
                stack.pop()

        index_removal = index_removal.intersection(stack)

        string_builder = []

        for idx, char in enumerate(s):
            if idx not in index_removal:
                string_builder.append(char)
