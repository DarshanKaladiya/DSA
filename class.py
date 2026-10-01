class Student:
    def get_data(self):
        self.rollno = int(input("Enter Roll No: "))
        self.name = input("Enter Name: ")
        self.program = input("Enter Program: ")

    def display(self):
        print("Student Details:")
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Program:", self.program)


student = Student()

student.get_data()
student.display()
