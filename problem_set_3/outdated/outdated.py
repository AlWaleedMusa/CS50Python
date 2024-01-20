month = {
    "January" : "01",
    "February" : "02",
    "March" : "03",
    "April" : "04",
    "May" : "05",
    "June" : "06",
    "July" : "07",
    "August" : "08",
    "September" : "09",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}

while True:
	user_input = input("Date: ").strip()

	if "/" in user_input:
		try:
			user_input = user_input.split("/")
			for num in user_input:
				if num.isdigit():
					continue
				else:
					break
			if int(user_input[0]) < 13 and int(user_input[1]) < 32:
				if int(user_input[0]) < 10:
					user_input[0] = "0" + user_input[0]
				if int(user_input[1]) < 10:
					user_input[1] = "0" + user_input[1]
				print("{}-{}-{}".format(user_input[2], user_input[0], user_input[1]))
				exit()
		except ValueError:
			pass
		except TypeError:
			pass
	
	elif "," in user_input:
		try:
			user_input = user_input.split()
			user_input[1] = int(user_input[1][:-1])
			for k, v in month.items():
				if user_input[0].title() == k and user_input[1] < 32:
					month = v
					date = user_input[1]
					year = user_input[2]
					if int(date) < 10:
						print("{}-{}-0{}".format(year, month, date))
					else:	
						print("{}-{}-{}".format(year, month, date))
					exit()
		except ValueError:
			pass
	else:
		pass

