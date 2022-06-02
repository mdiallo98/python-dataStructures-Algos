from collections import defaultdict


class UndergroundSystem:

    def __init__(self):
        checkInReg = defaultdict(list)
        checkOutReg = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.person = id
        if self.checkInReg[self.person][0] != stationName:
            self.checkInReg[self.person].append(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:

    def getAverageTime(self, startStation: str, endStation: str) -> float:
