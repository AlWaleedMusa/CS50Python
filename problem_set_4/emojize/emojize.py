import emoji

user_input = input("Input: ")

if "_" in user_input and "":
	if "africa" in user_input:
		user_input = ":globe_showing_Europe-Africa:"
		print("Output: {}".format(emoji.emojize(user_input)))
	elif "asia" in user_input or "Australia" in user_input:
		user_input = ":globe_showing_Asia-Australia:"
		print("Output: {}".format(emoji.emojize(user_input)))
	elif "americas" in user_input:
		user_input = ":globe_showing_Americas:"
		print("Output: {}".format(emoji.emojize(user_input)))
	else:
		print("Output: {}".format(emoji.emojize(user_input)))
else:
	print("Output: {}".format(emoji.emojize(user_input, language="alias")))
