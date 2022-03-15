av=5
x=int(input("how many candies you want"))
i=1
while i<=x:
    if i>av:
        print("out of stock")
        break
    print("candy")
    i=i+1

print("bye")

for i in range(1,101):
    if i%3==0:
        continue
    print(i)
print("bye")


for i in range(1,101):
    if i%2!=0:
        pass
    print(i)
print("bye")

