from secrets import randbelow


class Solution:

    def __init__(self, w: List[int]):
        self.lst = []

        prefix = 0
        for n in w:
            prefix += n
            self.lst.append(prefix)
        self.total = prefix

    def pickIndex(self) -> int:
        target = self.total * random.random()

        l, r = 0, len(self.lst) - 1
