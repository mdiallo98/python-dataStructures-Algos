class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()

        count = 0

        for i in range(len(nums)-1, 1, -1):
            curr = nums[i]
            start = 0
            end = i - 1
