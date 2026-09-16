#1. Perform addition, subtraction, multiplication, and division.

a = 20
b = 5

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#2. Find the remainder and quotient of two numbers.

a = 17
b = 5

print("Remainder:", a % b)
print("Quotient:", a // b)

#3. Check whether a number is even or odd.

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

#4. Compare two numbers using relational operators.

a = 10
b = 20

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

#5. Demonstrate logical operators (and, or, not).

a = 10
b = 20

print(a > 5 and b > 15)
print(a > 15 or b > 15)
print(not(a > 5))

#6. Demonstrate assignment operators (+=, -=, *=, /=).

a = 10

a += 5
print("After += :", a)

a -= 3
print("After -= :", a)

a *= 2
print("After *= :", a)

a /= 4
print("After /= :", a)

#7. Find the largest of two numbers using comparison operators.

a = 25
b = 40

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)
