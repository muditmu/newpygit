def greet():
    print("Hello")
    print("Good Morning")

def add(x,y):
    c=x+y
    print(c)


greet()
greet()
greet()
add(5,4)



def add(x,y):
    c=x+y
    return c
result=add(5,4)
print(result)



def add_sub(x,y):   #add and sub function
    c=x+y
    d=x-y
    return c,d
result1,result2=add_sub(5,4)
print(result1,result2)


def mul_div(x,y):    #multiple and division function
    a=x*y
    b=x/y
    return a,b
result1,result2=mul_div(8,2)
print(result1,result2)

