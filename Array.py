'''from array import *
values=array('i',[5,9,8,4,2])
print(values)'''



'''from array import *
values=array('i',[5,9,8,4,2])
print(values[0]) '''


'''from array import *
values=array('i',[5,9,8,4,2])
values.reverse()
print(values[0])'''

'''from array import *
values=array('i',[5,9,8,4,2])
print(values.buffer_info())'''


'''from array import *
values=array('i',[5,9,8,4,2])
for e in values:
    print(e)'''


'''from array import *
values=array('u',['a','e','i'])
for e in values:
    print(e)'''

'''from array import *
values=array('i',[5,9,8,4,2])
newarray=array(values.typecode, (a*a for a in values))
for e in newarray:
    print(e)'''


'''from array import *
values=array('i',[5,9,8,4,2])
newarray=array(values.typecode, (a*a for a in values))
i=0
while i<len(newarray):
    print(newarray[i])
    i=i+1'''

# Array values from user in python
'''from array import *
arr=array('i',[])
n=int(input("enter the length of the array"))
for i in range(n):
    x=int(input("enter the next value"))
    arr.append(x)



    print(arr)

value=int(input("enter the value for search"))

k=0
for e in arr:
    if e==value:
        print(k)
        break
    k=k+1

print(arr.index(value))'''



from array import *
arr=array('i',[])
n=int(input("enter the length of the array"))
for n in range(n):
    arr.append(n)
print(arr)



