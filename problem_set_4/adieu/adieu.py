def display_names(names):

	prefix = "Adieu, adieu, to"

	if len(names) == 1:
		print("\n{} {}".format(prefix, names[0]))
	elif len(names) == 2:
		print("\n{} {} and {}".format(prefix, names[0], names[1]))
	else:
		last_name = names[-1]
		print()
		print(prefix, end=" ")
		for i in range(len(names) - 1):
			if i != len(names) - 1:
				print(names[i], end=", ")
			else:
				print(names[i], end="")
		print("and {}".format(last_name))


names_list = []

while True:
	try:
		user_input = input("Name: ")
		names_list.append(user_input)

	except EOFError:
		break

display_names(names_list)
