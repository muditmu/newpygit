def count(list):

    even=0
    odd=0
    for i in list:
        if i%2==0:
            even=even+1
        else:
            odd=odd+1

    return even,odd
list=[20,14,17,19,28,48,98,47,12,55,67]

even,odd=count(list)

print(even)
print(odd)
print('even : {} and odd : {}'.format(even,odd))



# enter 5 name from users , find and display no of user who has lenth more than five letter
lst=[]
for i in range(5):
    x = input("Enter the name")
    lst.append(x)
def count(lst):
    greater = 0
    lesser = 0
    for i in lst:
        if len(i) >= 5:
            greater += 1
        else:
            lesser += 1
    return greater,lesser
greater,lesser = count(lst)
print("greater : {} and lesser : {}".format(greater,lesser))




def count(lst):
    greater = 0
    lesser = 0
    for i in lst:
        if len(i) >= 5:
            greater += 1
        else:
            lesser += 1
    return greater,lesser
list=['sonu','monu','mudit','rahul','abhishek']
greater,lesser = count(lst)
print("greater : {} and lesser : {}".format(greater,lesser))

