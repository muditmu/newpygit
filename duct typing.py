'''class pycharm:                         # duct typing
    def execute(self):
        print("compiling")
        print("running")

class laptop:
    def code(self,ide):
        ide.execute()

ide=pycharm()

lap1=laptop()

lap1.code(ide)'''




class pycharm:                         # duct typing
    def execute(self):
        print("compiling")
        print("running")

class myeditor:
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")


class laptop:
    def code(self,ide):
        ide.execute()

ide = myeditor()

lap1=laptop()

lap1.code(ide)
