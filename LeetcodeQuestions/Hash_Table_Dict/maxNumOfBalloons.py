from calendar import c


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #  Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

        # You can use each character in text at most once. Return the maximum number of instances that can be formed.

        count = defaultdict(0)
        for char in text:
            if char in "balloon":
                count[char] += 1
        count = 0
        while count:
            s = ""
            for char in "balloon":
