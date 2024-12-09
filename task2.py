def sum_of_positive_with_flooring(numbers):
    total = 0
    for num in numbers:
        if num > 0:
            total += int(num)
    return total


result = sum_of_positive_with_flooring([1, -4, 7, 12])
print(result)