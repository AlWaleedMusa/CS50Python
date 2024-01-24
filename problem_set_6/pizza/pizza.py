from tabulate import tabulate
import sys
import csv

if len(sys.argv) < 2:
	sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
	sys.exit("Not a Python file ")

file_name = sys.argv[1]

try:
	with open(file_name) as file:
		reader = csv.reader(file)
		reader = list(reader)
		header = reader[0]
		print(tabulate(reader[1:], header, tablefmt="grid"))
except FileNotFoundError:
	sys.exit("File does not exist")
