def main():
	greeting = input("Greeting: ").strip()
	result = value(greeting)
	print("${:d}".format(result))


def value(greeting):
	first_word = greeting.split()
	first_letter = greeting[0].lower()

	if first_word[0].lower() == "hello":
		return 0
	elif first_letter == "h":
		return 20
	else:
		return 100


if __name__ == "__main__":
    main()
