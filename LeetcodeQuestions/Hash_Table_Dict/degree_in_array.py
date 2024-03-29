# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        #  we need to find a contigous portion of the array that will contain the same degree of elems
        #  question worded kinda of weird
        #  i guess we need to dtermine the first and last occurence of the element that appears multiple times in the list
        left, right, count = {}, {}, Counter(nums)
        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i
            right[x] = i
            # the left and right objects are meant to allow us to know where within the list we will find the start and end of the element
        ans = len(nums)
        degree = max(count.values())
        print(ans, degree, count)
        for x in nums:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
