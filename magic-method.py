class Student:
    def __init__(self,name):
        self.name = name

movies = ['matrix','Finding Nemo']

class Garage:
    #defining a constructor
    def __init__(self):
        self.cars = []
#defining a dunder method that gives the length of object
    def __len__(self):
        return len(self.cars)
    #dunder method for indexing
    def __getitem__(self,i):
        return self.cars[i]
    
    #return the string representing an object
    def __repr__(self):
        return f'<Garage{self.cars}>'

    

    def __str__(self):
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')
ford.cars.append('Bucati')
#for indexing we will define the another dunder function
print(ford[0]) #this is equivalent to Garage.__getitem__(ford,0)

#after defining len and getitem dunder function in class we can now iterate over the our object
for car in ford:
    print(car)
print(ford)
print(Garage.__repr__(ford))