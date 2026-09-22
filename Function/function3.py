# 21. Function to calculate Fibonacci numbers
def fibonacci(n):
    a = 0
    b = 1
    result = []

    for i in range(n):
        result.append(a)
        a, b = b, a + b

    return result


# 22. Function to find the second-largest number in a list
def second_largest(numbers):
    unique_numbers = list(set(numbers))
    unique_numbers.remove(max(unique_numbers))
    return max(unique_numbers)


# 23. Function to sort a list without using sort()
def sort_list(numbers):
    numbers = numbers.copy()

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

# 24. Function to merge two lists and remove duplicates
def merge_lists(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result

print(fibonacci(10))

print(second_largest([10, 20, 5, 30, 15]))

print(sort_list([5, 2, 8, 1, 3]))

print(merge_lists([1, 2, 3], [3, 4, 5]))
