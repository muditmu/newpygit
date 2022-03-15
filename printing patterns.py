for i in range(4):
    for j in range(4):
        print("#",end="")
    print()


for i in range(4):
    for j in range(1+i):
        print("*",end="")
    print()




x=5
y=x//2

for i  in range(1,x+1,2):
    if y>0 :
        print(' '*y,end='')
        y=y-1
    print('*'*i)


for i in range(4):
    for j in range(4-i):
        print("#",end="")
    print()

