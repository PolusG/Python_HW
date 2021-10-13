from calculator import calculator
def calculator(number1,number2,operator):
	if operator == "+":
		print(number1 + number2)
	elif operator == "-":
		print(number1 - number2)
	elif operator == "*":
        	print(number1 * number2)
        elif operator == "/":
        	print(number1 / number2)
	elif operator == "//":
        	print(number1 // number2)
        elif operator == "**":
        	print(number1 ** number2)
	else:
		return flase
def parse_input():
	while True:
		n1 = flaot(input("Enter the first number: "))
		n2 = flaot(input("Enter the second number: "))
		op = input("Enter the operator: ")
		if not (op=="+" or op=="-" or op=="*" or op=="/" or op=="//" or op=="**"):
			break
		calculator(n1,n2,op)
