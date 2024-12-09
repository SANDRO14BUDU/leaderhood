def find_missing_number(nums):
    n = len(nums) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return total_sum - actual_sum


print(find_missing_number([1, 2 , 4, 5]))
print(find_missing_number([3, 5, 6, 1, 2]))
print(find_missing_number([2]))


