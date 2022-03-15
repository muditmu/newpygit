'''age=int(input("enter your age"))
if age in range(7,100):
    if age>18:
         print("drive")
    if age<18:
         print("Not drive ")
    if age==18:
            print("not decided")'''


age=int(input("enter your age"))
if age in range(7,100):
    if age>18:
         print("drive")
    elif age<18:
         print("Not drive ")
    else:
         print("not decided")