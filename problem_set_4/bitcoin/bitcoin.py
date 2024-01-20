import requests
import json
import sys

def calculate_rate(rate, num):
	result = rate * num
	print("${:,.4f}".format(result))

def main():
	if len(sys.argv) == 1:
		sys.exit("Missing command-line argument")

	if sys.argv[1].replace('.', '', 1).isdigit():
		sys.argv[1] = float(sys.argv[1])
	elif sys.argv[1].isdigit() == False:
		sys.exit("Command-line argument is not a number")

	num = float(sys.argv[1])


	try:
		url = "https://api.coindesk.com/v1/bpi/currentprice.json"
		respond = requests.get(url)
	except requests.exceptions.RequestException:
		print("Exception request")

	li = json.loads(respond.text)
	rate = li["bpi"]["USD"]["rate_float"]
	calculate_rate(rate, num)

if __name__ == "__main__":
	main()
