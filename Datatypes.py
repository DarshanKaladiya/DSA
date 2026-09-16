#2. Accept two numbers and display their data types.

a = input("Enter first number: ")
b = input("Enter second number: ")

print("First value:", a, "Type:", type(a))
print("Second value:", b, "Type:", type(b))

#3. Convert a string number into an integer and float.

num = "25"

integer_num = int(num)
float_num = float(num)

print(integer_num, type(integer_num))
print(float_num, type(float_num))

#4. Find the length of a string.

text = "Darshan"

print("Length:", len(text))

#5. Create a list, tuple, set, and dictionary and display their types.

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dictionary = {"name": "Rahul", "age": 20}

print(type(my_list))
print(type(my_tuple))
print(type(my_set))
print(type(my_dictionary))



