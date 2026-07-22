import csv
class Student:
    UNIVERSITY = "IST Islamabad"
    Total_Students = 0

    def __init__(self):
        self.name = ""
        self.age = 0
        self.dep = ""
        self.cgpa = 0
        self.loc = ""

        Student.Total_Students+=1

    def getdata(self):
        print("Enter Your Information:")
        self.name = input("Enter Your Name: ")
        self.age = int(input("Enter Your Age: "))
        self.dep = input("Enter Your Department: ")
        self.cgpa = float(input("Enter Your CGPA: "))
        self.loc = input("Enter Your Location: ")
        print("")


    def Display_Data(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"From: {self.loc}")
        print(f"University: {Student.UNIVERSITY}")
        print(f"Department: {self.dep}")
        print(f"CGPA: {self.cgpa}")
        print("")


    def introduce(self):
        print(f" Hello my name is {self.name}\n I am Student of {self.dep} at {self.UNIVERSITY}\n I am from {self.loc}\n My CGPA is {self.cgpa}")
        print("")

    def birthday(self):
        self.age+=1
        print(f"Happy Birthday! Your new age is {self.age}")
        print("")


    def update_cgpa(self):
        new_cgpa = float(input("Enter Your New CGPA: "))
        self.cgpa = new_cgpa
        print(f"CGPA Updated Successfully.\nYour new CGPA is {self.cgpa}")
        print("")


    def is_honour_student(self):
        if(self.cgpa>=3.5):
            print("You are a Honour Student")
        else:
            print("You are a Regular Student")
        print("")


    def total_Student(self):
        print(f"The total number of Student is: {Student.Total_Students}")
        print("")


student = []


def add_Student():
    s = Student()
    s.getdata()
    student.append(s)
    print("Student Added Successfully!")


def Search_Student():
    found = False
    Sname= input("Enter Student Name to Search: ")

    for s in student:
        if s.name.lower() == Sname.lower():
            s.Display_Data()
            found = True
            break

    if not found:
        print("Student not found")


def Delete_Student():
    found = False
    Dname= input("Enter Student Name to Delete: ")
    
    for s in student:
        if s.name.lower() == Dname.lower():
            student.remove(s)
            Student.Total_Students -= 1
            print("Student Deleted Successfully!")
            found = True
            break
    if not found:
        print("Student not found")


def Save_Data():
    with open("SMS.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Age", "Department", "CGPA", "Location"])
    
        for s in student:
            writer.writerow([s.name, s.age, s.dep, s.cgpa, s.loc])
    print("Data Saved Successfully!")



while True:

    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Save Data To CSV")
    print("5. Exit the program")

    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            add_Student()

        case 2:
            Search_Student()

        case 3:
            Delete_Student()
            
        case 4:
            Save_Data()

        case 5:
            print("Thanks For using")
            break
        
        case _:
            print("Invalid input")