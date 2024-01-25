def main():

	string = input("Expression: ").strip()
	string_to_list = string.split()
	num1 = int(string_to_list[0])
	op = string_to_list[1]
	num2 = int(string_to_list[2])

	if op == "+":
		print("{}".format(float(num1 + num2)))
	elif op == "-":
		print("{}".format(float(num1 - num2)))
	elif op == "/":
		print("{}".format(float(num1 / num2)))
	elif op == "*":
		print("{}".format(float(num1 * num2)))

if __name__ == "__main__":
	main()
