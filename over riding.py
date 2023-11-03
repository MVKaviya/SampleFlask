"""class Emp:             #super() method
    def emp(self):
        print("hello madhan emp1")
class Emp2(Emp):
    def emp(self):
        super().emp()
        print("hello vijay emp2")
class Emp3(Emp2):
    def emp(self):
        super().emp()
        print("hello arun emp3")
e=Emp3()
e.emp()

#__init__ and super() method:

class Emp:
    def __init__(self):
        print("hello")
        print("welcome")
class Emp2(Emp):
    def __init__(self):
        super().__init__()
        print("bye")
        print("end")
e=Emp2()"""
    

class Emp:
    def __init__(self):
        print("hello")
        print("welcome")
class Emp2(Emp):
    def __init__(self):
        super().__init__()
        print("bye")
class Emp3(Emp2):
    def __init__(self):
        super().__init__()
        print("happy")
        print("end")
e=Emp3()
