import random
import sys

def main():
	"""
	start of the program get level from user and pass the return value to generate integers
	"""

	level = get_level()
	generate_integer(level)


def get_level():
	"""
	ask user for input (level) to play
	1= 1 digit numbers (easy)
	2= 2 digit numbers (medium)
	3= 3 digit numbers (hard)

	return: level
	"""

	levels = [1, 2, 3]
	while True:
		try:
			level = int(input("Level: "))
			if level in levels:
				return level
		except ValueError:
			pass


def generate_integer(level):
	"""
	use the return level int to choose and generate 10 set of tuple
	with random numbers and store that in a list (random_nums)
	then initiate run_game function with the level and the list as arguments

	param: level: level pass from the get level function (1, 2 or 3)
	"""

	random_nums = []
	level = level

	if level == 1:
		for _ in range(10):
			num1 = random.randint(0, 9)
			num2 = random.randint(0, 9)
			random_nums.append((num1, num2))
		run_game(level, random_nums) # running the game
	elif level == 2:
		for _ in range(10):
			num1 = random.randint(10, 99)
			num2 = random.randint(10, 99)
			random_nums.append((num1, num2))
		run_game(level, random_nums) # running the game
	elif level == 3:
		for _ in range(10):
			num1 = random.randint(100, 999)
			num2 = random.randint(100, 999)
			random_nums.append((num1, num2))
		run_game(level, random_nums) # running the game


def run_game(level, number_list):
	"""
	run the game by printing each question on a line and wait for the right answer
	if no answer after 3 attempts show the right answer and move to the next
	question
	if right answer add 1 to score and move to the next one

	param: level: level pass from the get level function (1, 2 or 3)
	param: number_list: random list of integer tuples to print questing from

	return: Score
	"""
	score = 0

	if level == 1:
		for num in number_list:
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
				if answer != right_answer:
					print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	elif level == 2:
		for num in number_list:
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
				if answer != right_answer:
					print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	elif level == 3:
		for num in number_list:
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
				if answer != right_answer:
					print("{} + {} = {}".format(num[0], num[1], right_answer))
			except ValueError:
				pass

	print_and_replay(score) # calling to display score and ask for a new game


def print_and_replay(score):

	print("Score: {}".format(score))
	replay = input("would you like to play again: (Y / N): ")

	if replay.upper() == "Y":
		main()
	else:
		sys.exit("Good Game")


if __name__ == "__main__":
    main()
