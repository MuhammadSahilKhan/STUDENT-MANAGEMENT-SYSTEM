class Student:
    name = "Sahil"          # This is class attributes
    age = 20
    Dep = "CS-Ai"

    def greet(self):
        print("Good Morning")

    def getinfo(self):
        print(f"The Name is {self.name}, The Age is {self.age} and the Department is {self.Dep}")



S1 = Student()
S1.greet()
print(S1.name, S1.age, S1.Dep)
print("")

S1 = Student()
S1.greet()
S1.name = "Juni"            # This is instance or object attributes
print(S1.name, S1.age, S1.Dep)

print("")

S1.greet()
S1.getinfo()
