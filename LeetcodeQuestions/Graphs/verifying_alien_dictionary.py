class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        ordDict = {c: i for c, i in enumerate(order)}

        for i in range(len(words) - 1):
            wrd1, wrd2 = words[i], words[i+1]
