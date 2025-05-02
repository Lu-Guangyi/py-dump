# Simple calculator for two digit selector.
char_valueOne = int(input("Enter first #value: "))
char_valueTwo = int(input("Enter second #value: "))
method = str(input("Enter method: "))

method_one = "Division"
method_two = "Multiplication"
method_three = "Subtraction"
method_four = "Addition"

def function(method):
	if method == method_one:
		print(char_valueOne / char_valueTwo)
	elif method == method_two:
		print(char_valueOne * char_valueTwo)
	elif method == method_three:
		print(char_valueOne - char_valueTwo)
	elif method == method_four:
		print(char_valueOne + char_valueTwo)
	else:
		print("End..")

function(method)