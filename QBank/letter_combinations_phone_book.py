class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        charMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz"
        }

        def generate(idx, currStr):
