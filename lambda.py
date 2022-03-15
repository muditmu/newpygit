def sqare(a):          # simple form sqare programing
    return a*a
result=sqare(7)
print(result)



f=lambda a : a*a       # using lambda sqare programing
result=f(7)
print(result)



f=lambda a,b : a+a       # using lambda add  programing
result=f(7,6)
print(result)



# filter map reduce (using lambda)

def is_even(n):                  # simple form (filter)
    return n%2==0
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(is_even,nums))
print(evens)



f=lambda n : n%2==0              #using lambda (filter)
nums=[3,2,6,8,4,6,2,9]
evens=list(filter(lambda n : n%2==0,nums))
print(evens)



f=lambda n : n*2              #using lambda (map)
doubles=list(map(lambda n : n*2,evens))
print(doubles)


from functools import reduce     # using lambda (reduce)
f=lambda a,b : a+b
sum=reduce(lambda a,b : a+b , doubles)
print(sum)
