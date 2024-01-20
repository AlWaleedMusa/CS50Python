import random


def main():
	level = get_level()
	generate_integer(level)


def get_level():
    levels = [1, 2, 3]
    while True:
        try:
            level = int(input("Level: "))
            if level in levels:
                return level
        except ValueError:
            pass
        
def generate_integer(level):
	random_nums = []
	score = 0

	if level == 1:
		for _ in range(10):
			num1 = random.randint(0, 9)
			num2 = random.randint(0, 9)
			random_nums.append((num1, num2))
		for num in random_nums:
			try:
				for _ in range(3):
					try:
						answer = int(input("{} + {} = ".format(num[0], num[1])))
						right_answer = num[0] + num[1]
						if int(answer) == right_answer:
							score += 1
							break
						else:
							print("EEE")
					except ValueError:
						print("EEE")
				print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	elif level == 2:
		for _ in range(10):
			num1 = random.randint(10, 99)
			num2 = random.randint(10, 99)
			random_nums.append((num1, num2))
		for num in random_nums:
			try:
				for _ in range(3):
					try:
						answer = int(input("{} + {} = ".format(num[0], num[1])))
						right_answer = num[0] + num[1]
						if int(answer) == right_answer:
							score += 1
							break
						else:
							print("EEE")
					except ValueError:
						print("EEE")
				print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	elif level == 3:
		for _ in range(10):
			num1 = random.randint(100, 999)
			num2 = random.randint(100, 999)
			random_nums.append((num1, num2))
		for num in random_nums:
			try:
				for _ in range(3):
					try:
						answer = int(input("{} + {} = ".format(num[0], num[1])))
						right_answer = num[0] + num[1]
						if int(answer) == right_answer:
							score += 1
							break
						else:
							print("EEE")
					except ValueError:
						print("EEE")
				print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	print("Score: {}".format(score))


if __name__ == "__main__":
    main()