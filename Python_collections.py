"""
* counter
* defaultdict
* ordereddict
* namedtuple
* deque
"""
#imorting from python collections
from collections import Counter


device_temperatures = [13.5,12.0,13.5,14.5,14.0,5.0,15.0,15.0,14.5]

temperature_counter = Counter(device_temperatures)
#Counter is dictionary
print(temperature_counter[15.0])
print(temperature_counter[14.5])


from collections import defaultdict

my_dict = { 'hello': 5}
try: 
    print(my_dict['hi'])
except KeyError:
    print("there is the KeyError")

#defaultdict doesnot raises key error
coworkers = [('Susan', "Sankhamul"),('Sajana','Kalanki'),
('Kabin', 'lubhu'),('Umesh', 'Baneshwor'),
('Kabin', 'lalitpur')
]
job_life = defaultdict(list) #list is a class too

#destructing a tuple in following line in for loop
for coworker,place in coworkers:
    job_life[coworker].append(place)

job_life.default_factory = int #default_factory gives value assigned if the key doesnot exists
print(job_life) 
print(job_life['Kabin'])
print(job_life['ayush']) #gives empty list if the Key doesnot exist
