# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sample array we get [1,1,1,2,3,3,4,5,5,5]
        # goal is to bring back a K amount of the most freqent elements in the list
        # So first step is to map the element to how frequent it appears in the list

        myMap = {}
        myHeap = []

        for
