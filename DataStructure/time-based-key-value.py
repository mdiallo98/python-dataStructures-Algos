from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.store:
            return ""
        if timestamp < self.store[key][0][0]:
            return ""

        left, right = 0, len(self.store[key])
        while left < right:
            mid = (right - left) // 2

            if timestamp >= self.store[key][mid][0]:
                left = mid + 1
            else:
                right = mid
        return "" if right == 0 else self.store[key][right-1][1]
