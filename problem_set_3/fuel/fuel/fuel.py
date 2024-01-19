import math
while True:
	try:
		user_input = input("Fraction: ").strip().split("/")

		x = int(user_input[0])
		y = int(user_input[1])

		if y == x:
			print("F")
			break
		if x < y and y != 0:
			r = int(round((x/y) * 100))

			if r <= 1:
				print("E")
				break
			elif r >= 99:
				print("F")
				break
			else:
				print("{}%".format(r))
				break

	except ValueError:
		pass
	except ZeroDivisionError:
		pass
