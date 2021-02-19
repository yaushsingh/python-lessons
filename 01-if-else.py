#!/usr/bin/python3

number =  input("Enter a number: ")

if (int(number) > 0):
	print("The number is Positive", int(number))
elif (int(number) == 0):
	print("It is zero")
elif (int(number) < 0):
	print(f"{int(number)} is negative")
else:
	print("Invalid Number!!!")
