
def findMaxLength(nums):
    count = 0
    window_len = 0
    hash_table = {}
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        if nums[i] == 1:
            count += 1

        if count == 0:
            window_len = i + 1
        if count in hash_table:
