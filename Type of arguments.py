
def person(name,age):    # position argument
    print(name)
    print(age)

person('mudit',30)



def person(name,age):    # keyword argument
    print(name)
    print(age)

person(name='mudit',age=30)



def person(name,age=29):    # default argument
    print(name)
    print(age)

person('mudit')



def sum(a,*b):    # variable length argument
    print(a)
    print(b)
    c=a
    for i in b:
        c=c+i
    print(c)

sum(5,6,34,75)



def person(name,**data):    # keywords variable length argument
    print(name)
    print(data)

person('mudit',age=28,city='noida',mob=8851324419)



def person(name,**data):    # keywords variable length argument
    print(name)
    for i,j in data.items():
        print(i,j)

person('mudit',age=28,city='noida',mob=8851324419)





a=10            # global  and local variable (local variable use as global variable)
print(id(a))

def somthing():
    a=5
    x=globals()['a']
    print(id(x))
    print('in side fun',a)
    globals()['a']=15

somthing()

print('out side fun',a)




a=10            # global  and local variable (local variable use as global variable)
print(id(a))

def somthing():
    global a
    a=15
    print('in side fun',a)
    print(id(a))


somthing()

print('out side fun',a)






