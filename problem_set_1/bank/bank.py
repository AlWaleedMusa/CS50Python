greeting = input("Greeting: ").strip()
first_word = greeting[:5].lower()
first_letter = greeting[0].lower()

if first_word == "hello":
	print("$0")
elif first_letter == "h":
	print("$20")
else:
	print("$100")
