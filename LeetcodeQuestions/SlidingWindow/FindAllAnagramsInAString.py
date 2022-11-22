class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        plen = len(p)

        if len(s) < len(p):
            return []

        pCount = Counter(p)
        window = defaultdict(0)
        res = []
        for r in range(len(s)):
            #  i need to add each char into my window
            window[s[r]] += 1

            #  we know when the window and pCount are the same then we can return
            if window == pCount:
                res.append(i - plen + 1)
