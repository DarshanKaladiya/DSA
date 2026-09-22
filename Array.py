#method 1

import array

a = array.array('i', [10, 20, 30, 40, 50])
print(a)

for i in range(5):
    print(a[i])

print("======================================== \n")

#method 2

import array as arr

b = arr.array('f', [10.1, 20.2, 30.3, 40.4, 50.5])
print(b)

for i in range(5):
    print(b[i])

print("======================================== \n")

#method 3

from array import *

c = array('u', ['a', 'b', 'c', 'd', 'e'])
print(c)

for i in range(5):
    print(c[i])
