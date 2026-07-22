class Student:
    name  = ""                            # This is class attributes
    age = 0
    Dep = ""

    def greet(self):
        print("Good Morning")

        
    def getinfo(self):
        print(f"The Name is {self.name}, The Age is {self.age} and the Department is {self.Dep}")


    def __init__(self, name, age,Dep):
        self.name = name
        self.age = age
        self.Dep = Dep
        print("Hey I am Constructor")

    def display(self):
        S1.greet()
        print(f"The Name is {self.name}, The Age is {self.age} and the Department is {self.Dep}")  
        print("")


S1 = Student("Sahil", 20, "CS-Ai")
S1.display()
# print(S1.name, S1.age, S1.Dep)


S2 = Student("Junaid" , 19, "Ai")
S2.display()
# S2.name = "Juni"                                       # This is instance or object attributes
# print(S2.name, S2.age, S2.Dep)


# S1.greet()
# S1.getinfo()
