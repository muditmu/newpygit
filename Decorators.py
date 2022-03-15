print(__name__)       # special varial (__name__)

def div(a,b):    # using simple div programing
    print(a/b)
div(4,2)


def div(a,b):
    print(a/b)
div(2,4)



def div(a,b):     # if numerator is less than denominator i want to swap them
    if a<b:
        a,b=b,a
    print(a/b)
div(2,4)




def div(a,b):         # decorators using
    print(a/b)
def smart_div(func):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

div1 = smart_div(div)
div1(2,4)




