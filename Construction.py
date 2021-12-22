class Student:
    #@Creating a constructor:
    def __init__(self):
        self.student_name = input("Enter The Student's name: ")
        self.student_age = input("Enter The Student's age: ")
        self.student_gen = input("Enter The Student's gender: ")

    def display(self):
        print("Enter The Student's name: ",self.student_name)
        print("Enter The Student's age: ",self.student_age)
        print("Enter The Student's gender: ",self.student_gen)

class Marks:
    def __init__(self):
        self.grade = input("Enter The Student's grade: ")
        print("Evaluate Marks for Subject: ")
        self.english = int(input("English marks: "))
        self.maths = int(input("Mathematics marks :"))
        self.science = int(input("Science Marks: "))
        self.social = int(input("Social Science marks: "))
        self.ICT = int(input("ICT Marks: "))

    def display(self):
        self.total = (self.english + self.maths + self.science + self.social + self.ICT)
        print ("Total Evaluated Marks:",self.total)
        
class Data(Student,Marks):
    def __init__(self):
         Student.__init__(self)
         Marks.__init__(self)
     
    def result(self):
        Marks.display(self)


S1 = Data()
S1.result()
S2 = Data()
     
     
        
