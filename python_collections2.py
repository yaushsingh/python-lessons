from collections import defaultdict
my_office = 'Gidan'
workers = ['ayush','prabha','susan','umesh']
other_workers = [('khusi','goec'),('Kabin','KTFT'),('sajan','Pees')]

worker_office = defaultdict(lambda : my_office) #defaultdict takes in functions only
#accessing the workers who dont work in my  office

for person, office in other_workers:
    worker_office[person] = office
    
print(worker_office[workers[0]]) 
print(worker_office['Kabin'])
print(worker_office['susan'])

#namedtuple
from collections import namedtuple

sc =('savings',123)

account = namedtuple('account',('name', 'balance'))
ac = account('checking',345)
print(ac.name)
print(ac.balance)


#deque can push a element from start or end
from collections import deque

friends = deque(('ayush','shiva','mahadev', 'mahakal','shambho'))
print(friends)
friends.append('karpoor') #adds element at last of list
print(friends)
friends.appendleft('pashupati') #adds element at first of list
print(friends)


friends.pop()
print(friends)  #removes element from end
friends.popleft() #removes elements from start

print(friends)