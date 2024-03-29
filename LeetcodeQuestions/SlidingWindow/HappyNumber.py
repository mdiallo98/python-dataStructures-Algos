class Solution:
    def isHappyNaive(self, n: int) -> bool:

        def get_Next(n):
            sumT = 0
            while n > 0:
                n, digit = divmod(n, 10)
                sumT = digit**2
            return sumT
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = get_Next(n)
        return n == 1
