
def fib(n):       # fibonacci series

    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(5)





x=0
y=1
for i in range(10):
    z=x+y
    print(z)
    x=y
    y=z
    i+=1