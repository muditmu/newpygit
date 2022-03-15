class student:                           #outer class   dl4scf7806
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
        self.lap=self.laptop()

    def show(self):
        print(self.name,self.rollno)
        self.lap.show()

    class laptop:                     #inner class
        def __init__(self):
            self.brand="hp"
            self.cpu="i5"
            self.ram=8

        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student("mudit",2)   # object
s2=student("rahul",3)

s1.show()               # print
s2.show()


