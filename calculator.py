
def main():
	a = int(input("Enter the first number  : "))
	b = int(input("Enter the second number :"))
	op = input("Enter a number operation : ")

	if op == "+":
		int result = a + b

	elif op == "-":
		int result = a - b

	elif op == "*":
		int result = a * b

	elif op == "/":
		int result = a / b

	else:
		print("Sorry this number operation does not exist")
		main()

	print("The result is" , result)
	repeat = input("Do you want to repeat? [y/n] : ")

	if repeat in ("y"):
		main()

	else:
		print("Thank You for using this program")

main()