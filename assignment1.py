def add(x,y):
    z = x + y

    return z


def sub(x,y):
    z = x - y
    
    return z


def multiply(x,y):
    z = x * y
    
    return z

def divide(x,y):
    return x / y

def input_two_numbers():

    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    return x, y

flag = "y"
while flag.lower() == "y":
    operator = int(
                    input(
                        """Please enter a operation: 
                            1.add 
                            2.subtract 
                            3.multiply 
                            4.divide 
                        """
                    )
                )


    if operator == 1:
        x, y = input_two_numbers()
        z = add(x,y)
        print(f"the sum of {x} and {y} is {z}")
    elif (operator == 2):
        x1, y1 = input_two_numbers()
        z = sub(x1,y1)
        print(f"the difference is {z}")
    elif operator == 3:
        x, y = input_two_numbers()
        z = multiply(x,y)
        print(f"the product is {z}")
    elif operator==4:
        x, y = input_two_numbers()
        print("performing divide")
        z=divide(x,y)
        print(f"the result is {z}")
    flag = input("Do you want to continue? (y/n): ")
    if flag.lower() != "y":
        break


   