
import heapq


def kSmallestPairs(nums1, nums2, k):
    #  maybe two use heaps simoultanously

    heapq.heapify(nums1)
    heapq.heapify(nums2)
    res = []
    while nums1 or nums2:

        for _ in range(k):
            one = heapq.heappop(nums1)
            second = heapq.heappop(nums2)
