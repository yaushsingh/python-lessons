#unpacking arguments 
 
attendance = {
    'present' : 3,
    'absent' : 3
}

def haajir(status : str , count : int):
    #function to update the attendance
    attendance[status] += count 
    return attendance[status]

#list containing tuples
student_attendance = [
    ('present', 22) ,
    ('absent', 2),
    ('absent' , 4),
    ('present', 34)
]

#for every tuple in list it will use tuple's element as argument in function
for a in student_attendance:
    haajir(a[0], a[1])
    """We can also use haajir(*a)"""

print(attendance)

second_attendance = [
    ('present', 12),
    ('present',9),
    ('absent',4),
    ('absent',9)
]
for b in second_attendance:
    #assigning  the value to the function arguments
    haajir(status = b[0], count = b[1])

print(attendance)
