def main():

	message = input()
	string = message.split()
	print(change_to_emoji(string))


def change_to_emoji(string):
	""" change a simple :) or :( to an emoji
	
	args:
		string: string passed from user input to process

	return:
		a new string
	"""
	if ":)" in string:
		idx = string.index(":)")
		string[idx] = "\U0001F642"

		if ":(" in string:
			idx = string.index(":(")
			string[idx] = "\U0001F641"

	elif ":(" in string:
		idx = string.index(":(")
		string[idx] = "\U0001F641"

	new_string = " ".join(string)

	return new_string


if __name__ == "__main__":
	main()
