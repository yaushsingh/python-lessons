class uncountableError(ValueError):
    def __init__(self,wrong_value):
        super().__init__("Invalid value for n,{}. n must begreater than 0".format(wrong_value))



def count_from_zero_to_n(n):
    if n < 1:
        raise uncountableError(n)
    for x in range(0,n+1):
        print(x)
count_from_zero_to_n(int(input("enter a number : ")))