import operator
import inspect
import sqlite3
import trace

character_name = "Tom"
character_age = 50.45645
character_value = 0
value_str = str(character_value)
is_male = True
name = str(character_name[0])

# print(character_name.upper.isupper())
# print(character_name[0])
# print(len(character_name))
# print(character_name.index("T"))
def function(character_name):
	if character_name.index("T") == character_value:
		return True
	else:
		return False

function(character_name)

if function(character_name) == True:
	print("True")
elif function(character_name) == False:
	print("False")
else:
	print("Error")


first_value = int(input("Enter first number: "))
second_value = int(input("Enter second number: "))


ops = {
	"+": operator.add,
	"-": operator.sub,
	"*": operator.mul,
	"/": operator.truediv
}

ops_char = input("Enter an operator: ")
ops_func = ops[ops_char]
result = ops_func(first_value, second_value)
print(result)

# print(inspect.getfile(operator))
print(round(3.5))

operator_path = "/usr/lib/python3.13/operator.py"

if operator_path == inspect.getfile(operator): 
	while True:
		names = input("Enter name: ")
		num1 = int(input("Enter number: "))
		num2 = int(input("Enter 2nd number: "))
		operates = {
			"+": operator.add,
			"-": operator.sub,
			"*": operator.mul,
			"/": operator.truediv
		}

		operations = input("Operator?: ")
		operations_functions = operates[operations]
		result = operations_functions(num1, num2)
		print(result)
		if result == operations_functions(num1, num2):
			print("Function is completed.")
			break
		else:
			print("Error!")
			print("Again!")

color = input("Enter a Color: ")
plural_noun = input("Enter a PLural Noun: ")
celebrity = input("Enter a celebrtity: ")

print("Roses are" + color)
# print ("")

friends = ["Kevin", "Karen", "Jaden",]

print(friends[0])

if friends == ([0], [1], [2]):
        print("True")
else:
        print("False")

