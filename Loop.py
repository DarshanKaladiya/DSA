#1. Print numbers from 1 to 10 using a for loop.

for i in range(1, 11):
    print(i)

#2. Print numbers from 10 to 1 using a while loop

i = 10

while i >= 1:
    print(i)
    i -= 1

#3. Print multiplication table of a number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#4. Find the sum of numbers from 1 to n

n = int(input("Enter n: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)

#5. Find the factorial of a number

n = int(input("Enter a number: "))

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial:", factorial)

#6. Print all even numbers between 1 and 100

for i in range(2, 101, 2):
    print(i)

#7. Reverse a number using a loop

num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)

#8. Count the digits of a number

num = int(input("Enter a number: "))

num = abs(num)

if num == 0:
    count = 1
else:
    count = 0

    while num > 0:
        count += 1
        num //= 10

print("Number of digits:", count)

#9. Check whether a number is prime

num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

#10. Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    
    a, b = b, a + b
