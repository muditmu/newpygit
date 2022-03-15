class computer:                # class and object
    def config(self):
        print("i5,16gb,1tb")

com1=computer()
print(type(com1))
com1.config()




class computer:                                # using __init_method

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("config is",self.cpu,self.ram)

com1=computer("i5",16)
com2=computer("mudit 3",8)
print(type(com1))
com1.config()
com2.config()
