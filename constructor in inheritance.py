'''class A:                             # constructor in inheritance
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in B Init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")


a1=B()'''






class A:                             #MRO(Method resolution oder)
    def __init__(self):
        print("in A Init")
    def feature1(self):
        print("feature 1 working")
    def feature2(self):
        print("feature 2 working")

class B:
    def __init__(self):
        print("in B Init")
    def feature3(self):
        print("feature 3 working")
    def feature4(self):
        print("feature 4 working")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("in C Init")
    def feature5(self):
        super().feature2()

a1=C()
a1.feature1()
a1.feature5()




