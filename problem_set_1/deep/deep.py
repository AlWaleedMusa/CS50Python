message = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

if message == "42":
	print("Yes")
elif message == "forty-two":
	print("Yes")
elif message == "forty two":
	print("Yes")
else:
	print("No")
