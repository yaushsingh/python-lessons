class movie:
    #my error was i typed __intit__ insted of __init__
    def __init__ (self, name, year):
        #name in self.name is not a variable rather a property of self 
        self.name = name
        self.year = year

#sending the parameter to the class and accessing its property called name
#we are not assigning any variable 
print(movie ('The Matrix',1994).name)
print(movie ("The Matrix", 1994).year)

#we can also assign varbiable and access it which is useful method
matrix = movie("The Matrix Reloaded",2004)
print(matrix.name)
print (matrix.year)