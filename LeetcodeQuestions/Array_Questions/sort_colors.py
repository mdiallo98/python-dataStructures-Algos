class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #  you are giving a list that only contains 0,1,2 and the goal is to sort the list without using built-in sortin methods or any additional space

        #  You have several options:
        #  You can use primitive n^2 sorting techniques or implement merge or quick sort
        #  you can also count the frequencies of all three numbers in on pass than rewrite the list using the counts, this would N + N time complexity
        zero = 0
        one = 0
        two = 0
        for n in nums:
            if n == 0:
                zero += 1
            elif n == 1:
                one += 1
            else:
                two += 1
        i = 0
        while i <= len(nums) - 1:

            while zero != 0:
                nums[i] = 0
                i += 1
                zero -= 1
            while one != 0:
                nums[i] = 1
                i += 1
                one -= 1
            while two != 0:
                nums[i] = 2
                i += 1
                two -= 1
