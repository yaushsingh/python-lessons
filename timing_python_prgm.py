import time

def powers(limit):
    return [x**2 for x in range(limit)]
'''
it is tedious to start and end time every piece of line
so we can define a function to measure time  
start = time.time()
powers(5000000)
end = time.time()
'''
def measure_runtime(func): #can take function as argument 
    start = time.time()
    func()
    end = time.time()
    print(end - start)

measure_runtime( lambda : powers(5000)) 
#we create lambda function as powers function returns 
#list not function

#timeit module has timeit module which can call the above code

import timeit
#timeit module has  timeit function which can take string as function
#the string should be a python string
print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
#timeit is handy when we try to compare two line of string
#timeit is slow as it runs million times by default for benchmarking the statement over and over