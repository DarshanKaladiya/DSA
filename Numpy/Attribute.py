#ndim
from numpy import *

arr1 = array([1,2,3,4,5]) 
print(arr1.ndim)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.ndim)

#shape
arr1 = array([1,2,3,4,5])
print(arr1.shape)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.shape)

#size
arr1 = array([1,2,3,4,5])
print(arr1.size)

arr2 = array([[1,2,3], [4,5,6]])
print(arr2.size)

#itemsize
arr1 = array([1,2,3,4,5])
print(arr1.itemsize)

arr2 = array([1.1,2.1,3.5,4,5.0])
print(arr2.itemsize)

#dtype
arr1 = array([1,2,3,4,5]) 
print(arr1.dtype)

arr2 = array([1.1,2.1,3.5,4,5.0]) 
print(arr2.dtype)

#nbytes
arr2 = array([[1,2,3], [4,5,6]])
print(arr2.nbytes)



