from collections import Counter


#  this will be a place where i will practice

def bubbleSort(nums):
    #  bubble sort is a naive sorting algorithm that will sort the element in an array
    #  the time complexity that will result for performing the computation will be O(n^2)

    for r in range(len(nums)):

        for j in range(r-1):
            print(r, j)
            if nums[j] > nums[j+1]:
                tmp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = tmp
        print(nums)
    return nums


lst = [14, 7, 8, 12, 68, 45, 12, 32, 89, 41, 23]

# res = bubbleSort(lst)


def MergeSort(nums):
    #  we will continue dividing until there is one element left in the array
    while len(nums) > 1:

        left = nums[len(nums)//2:]
        right = nums[:len(nums)//2]

        MergeSort(left)
        MergeSort(right)

    #  outside of this function
    i = 0
    j = 0
    r = 0
