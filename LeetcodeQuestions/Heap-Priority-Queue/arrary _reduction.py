class Solution:

    def reduceArray(self, nums):

        heap = nums
        heapq.heapify(heap)

        total = 0

        while len(heap) > 1

        one = heapq.heappop(heap)
