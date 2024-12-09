def sum_of_positive(numbers):
    return sum(num for num in numbers if num > 0)


print(sum_of_positive([1, -4, 7, 12]))
print(sum_of_positive([-1, -2. -3. -4]))
print(sum_of_positive([]))