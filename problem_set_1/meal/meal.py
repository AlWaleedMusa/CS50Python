def main():

	time = input("What time is it? ").strip()
	time_float = convert(time)

	if time_float >= 7.00 and time_float <= 8.00:
		print("breakfast time")
	elif time_float >= 12.00 and time_float <= 13.00:
			print("lunch time")
	elif time_float >= 18.00 and time_float <= 19.00:
		print("dinner time")


def convert(time):
	x, y = time.split(":")
	hour = float(x)
	minutes = float(y) * 1 / 60
	return float(hour + minutes)

if __name__ == "__main__":
    main()
