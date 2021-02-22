my_student = {
    'name' : "Rolf Smith",
    'grades' : [70,80,75,86]
}

def average(student) :
    avg = sum(student['grades'])/len(student['grades'])
    return avg
#callling average function with my_student as argument    
print(average(my_student))

#defining a object structure
class Student :
    #dunder function special function 
    #self is blank object that is created before calling dunder function
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade
    def average(self):
        return sum(self.grades) / len(self.grades)
#creating an object by calling the object and passing argument
student_one = Student('Rolf Smith', [70, 80, 75, 86])  
student_two = Student('ayush', [48,58,98,87,57])
print(student_one.name)
print(student_one.average())
print(Student.average(student_one))
print(student_one.grades)
#printing the name of class assigned to student_one
print(student_one.__class__)