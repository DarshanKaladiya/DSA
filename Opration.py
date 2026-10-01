class Operation:

    def calculate(self):
        print("1. Sum")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Square")
        print("6. Cube")
        print("7. Square Root")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("Result =", a + b)

            case 2:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("Result =", a - b)

            case 3:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("Result =", a * b)

            case 4:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))

                if b == 0:
                    print("Cannot divide by zero")
                else:
                    print("Result =", a / b)

            case 5:
                a = int(input("Enter a number: "))
                print("Square =", a * a)

            case 6:
                a = int(input("Enter a number: "))
                print("Cube =", a * a * a)

            case 7:
                    a = float(input("Enter a number: "))
                    print("Square Root =", a ** 0.5)
                    
            case _:
                print("Invalid choice")


obj = Operation()
obj.calculate()
