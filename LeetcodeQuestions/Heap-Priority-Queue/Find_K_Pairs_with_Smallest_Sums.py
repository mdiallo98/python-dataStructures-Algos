
import heapq


def kSmallestPairs(nums1, nums2, k):
    #  maybe two use heaps simoultanously

    heapq.heapify(nums1)
    heapq.heapify(nums2)

    while nums1 or nums2
