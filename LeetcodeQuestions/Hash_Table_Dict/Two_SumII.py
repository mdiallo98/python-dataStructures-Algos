# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        myMap = {}

        for i in range(len(numbers)):
            curr = numbers[i]
            difference = target - curr
            if difference in myMap:
                return [myMap[difference] + 1, i+1]
            else:
                myMap[curr] = i

    def with_Binary_search(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return (l+1, r+1)
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
