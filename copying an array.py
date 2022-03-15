from numpy import *
arr=array([1,2,3,4,5])
arr=arr+5
print(arr)
print(sin(arr))
print(cos(arr))


from numpy import *  # add two array is called vectorized operation
arr1=array([1,2,3,4,5])
arr2=array([6,7,8,9,10])
arr3=arr1+arr2
print(arr3)
print(sin(arr3))
print(cos(arr3))
print(log(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(min(arr3))
print(max(arr3))
print(sort(arr3))
print(concatenate([arr1,arr2]) )

from numpy import *
arr1=array([2,6,8,1,3])
arr2=arr1
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


from numpy import *   #shallow copy
arr1=array([2,6,8,1,3])
arr2=arr1.view()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))


from numpy import *   #Deep copy
arr1=array([2,6,8,1,3])
arr2=arr1.copy()
arr1[1]=7
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

