import random


level = 0
while int(level) < 1:
	try:
		level = int(input("Level: "))
	except ValueError:
		pass

random_num = random.randint(1, level)

guess = 0
while guess != random_num:
	try:
		guess = int(input("Guess: "))
		if guess > random_num:
			print("Too large! ")
		elif guess < random_num:
			print("Too small!")
		else:
			print("Just right!")
			break
	except ValueError:
		pass
