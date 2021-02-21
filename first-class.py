operations = {  #dictionary with a functions
    "average": lambda seq: sum(seq) / len(),
    "total" : lambda seq : sum(seq),
    "top" : max # lambda seq: sum(seq) is equal to sum .so,
}
#list of dictionary
students = [
    {"name" : "Ayush", "grades": (60,78,77,76,87)},
    {"name" : "Prabha", "grades": (88,76,98,76,95)},
    {"name": "Mahima", "grades" : (78,68,79,75,84)},
    {"name": "Garima", "grades": (97,89,78,85,83)}
]
#accessing the lists of dictionary and also calling the dictionary
# with function
for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"student : {name}")
    operation = input("Enter 'average' or 'total' or 'top' ")

    result = operations[operation]('grades')
    print(result)