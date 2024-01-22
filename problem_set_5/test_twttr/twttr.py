def main():
	word = input("Input: ").strip()
	new_word = shorten(word)
	print("Output: {}".format(new_word))


def shorten(word):
	vowel_list = ["A", "E", "I", "O", "U"]
	new_list = []

	for letter in word:
		if letter.upper() in vowel_list:
			continue
		new_list.append(letter)

	new_string = "".join(new_list)
	return new_string


if __name__ == "__main__":
    main()
