# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #  we need to find a contigous portion of the array that will contain the same degree of elems
