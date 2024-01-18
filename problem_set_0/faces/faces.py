message = input()
li = message.split()

def change_to_emoji(list):
	print(list)
	if ":)" in list:
		idx = list.index(":)")
		list[idx] = "\U0001F642"

		if ":(" in list:
			idx = list.index(":(")
			list[idx] = "\U0001F641"

	elif ":(" in list:
		idx = list.index(":(")
		list[idx] = "\U0001F641"

	new_string = " ".join(list)
	print(new_string)

change_to_emoji(li)
