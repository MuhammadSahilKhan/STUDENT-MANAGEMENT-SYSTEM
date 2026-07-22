#  P1...........................................................................................................

class Programmer:
    company = "Microsoft"
    name = ""
    age = 0
    salary = 0
    pincode = 0

    def __init__(self, n, a, s, p):
        self.name = n
        self.age = a
        self.salary = s
        self.pincode = p

    def display(self):
        print("The Programmer detial is following:")
        print(f" The Name is {self.name}\n The age is {self.age} \n The salary is {self.salary}\n The pincode is {self.pincode}\n Work At {self.company}")
        print("")


P1 = Programmer("Sahil", 20, 120000, 123)
P1.display()


P2 = Programmer("Junaid", 19, 100000, 100)
P2.display()

P3 = Programmer("Sami", 21, 150000, 133)
P3.display()

P4 = Programmer("Hassan", 22, 160000, 153)
P4.display()




# P2...........................................................................................................


class calculator:
    num1 = 0

    def __init__(self,n):
        self.num1= n

    def square(self):
        self.s = (self.num1**2)
    
    def cube(self):
        self.c = (self.num1**3)

    
    def squareroot(self):
        self.r = (self.num1**0.5)

    def display(self):
        print(f" The sqaure is {self.s}\n The Cube is {self.c}\n The Squareroot is {self.r}")



N = calculator(25)
N.square()
N.cube()
N.squareroot()
N.display()


N2 = calculator((int(input("Enter a number: "))))
N2.square()
N2.cube()
N2.squareroot()
N2.display()




# P3...........................................................................................................


class calculator:
    num1 = 0

    def __init__(self,n):
        self.num1= n

    def square(self):
        self.s = (self.num1**2)
    
    def cube(self):
        self.c = (self.num1**3)

    
    def squareroot(self):
        self.r = (self.num1**0.5)

    def display(self):
        print(f" The sqaure is {self.s}\n The Cube is {self.c}\n The Squareroot is {self.r}")

    @staticmethod
    def hello():
        print("Hello Sir")



N = calculator(25)
N.hello()
N.square()
N.cube()
N.squareroot()
N.display()


N2 = calculator((int(input("Enter a number: "))))
N2.hello()
N2.square()
N2.cube()
N2.squareroot()
N2.display()



# P4...........................................................................................................
import random
class train:

    def __init__(self, tNo, fro, to):
        self.tNo = tNo
        self.fro = fro
        self.to = to


    def book(self):
        print(f"The Ticket is booked in train no: {self.tNo} going from {self.fro} to {self.to}")

    def getstatus(self):
        print(f"The Train has train no: {self.tNo} is successfully going")

    def getfare(self):
        print(f"The Ticket fare in train no: {self.tNo} going from {self.fro} to {self.to} is {random.randint(200,1000)}")


T1 = train(2321, "Swat", "Islamabad")
T1.book()
T1.getstatus()
T1.getfare()