# 11. Function to find the maximum of three numbers
def maximum_of_three(a, b, c):
    return max(a, b, c)


# 12. Function to count vowels in a string
def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count


# 13. Function to reverse a string
def reverse_string(text):
    return text[::-1]


# 14. Function to check whether a string is a palindrome
def is_palindrome(text):
    return text == text[::-1]


# 15. Function to find the sum of all elements in a list
def list_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


# 16. Function to find the largest element in a list
def largest_element(numbers):
    return max(numbers)


# 17. Function to remove duplicate elements from a list
def remove_duplicates(numbers):
    result = []
    for number in numbers:
        if number not in result:
            result.append(number)
    return result


# 18. Function to count how many times an element appears in a list
def count_element(numbers, element):
    count = 0
    for number in numbers:
        if number == element:
            count += 1
    return count


# 19. Function to check whether a number is prime
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 20. Function to return all prime numbers between two numbers
def primes_between(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes






print(maximum_of_three(10, 25, 15))
print(count_vowels("Hello World"))
print(reverse_string("Python"))
print(is_palindrome("madam"))

print(list_sum([1, 2, 3, 4, 5]))
print(largest_element([10, 25, 7, 40, 15]))
print(remove_duplicates([1, 2, 2, 3, 3, 4]))

print(count_element([1, 2, 2, 3, 2], 2))
