from numpy import *
arr1=array([
    [1,2,3,4],
    [5,6,7,8]
           ])
print(arr1)
print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)


from numpy import *
arr1=array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
           ])
arr2=arr1.flatten()  # 2dim array convert into 1d array
arr3=arr2.reshape(3,4) # 1dim array convert into 3d array
m=matrix(arr1)        # 2dim array convert into matrix formate

print(arr3)
print(m)


from numpy import *
m = matrix ('1 2 3 4 ; 5 6 7 8')  # 2 rows and 4 colum
print(m)
m = matrix ('1 2 ; 3 4 ; 5 6 ; 7 8')    # 4 rows and 3 colum
print(m)
m = matrix ('1 2 3 ; 4 5 6 ; 7 8 9')     # 3 rows and 3 colum
print(m)
print(diagonal(m))
print(m.min())
print(m.max())




from numpy import *     # add 2 matrix 
m1=matrix('1 2 3 ; 4 5 6 ; 7 8 9')
m2=matrix('2 3 4 ; 2 5 7 ; 7 1 3')
m3=m1+m2;
print(m3)


