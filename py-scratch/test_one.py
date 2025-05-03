import operator
import inspect

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

print(inspect.getfile(operator))
print(round(3.5))


