 #practice of inheritance 
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school,salary):
        super().__init__(name, school)
        self.salary = salary
    
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.5)
print(rolf.salary)
rolf.marks.append(57)
rolf.marks.append(67)
rolf.marks.append(76)
"""The code still runs though workingsutdent class doesnot have 
average function the class student has it which is inherited by 
workingstudent class"""
print(rolf.average())
print(rolf.weekly_salary())
"""but the anna=Student('anna',"oxford")
            print(anna.weekly_salary())
            will get error as no method called weekly_salary is 
            \defined in student class"""