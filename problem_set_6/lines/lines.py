import sys

if len(sys.argv) < 2:
	sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 2:
	sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
	sys.exit("Not a Python file ")

file_name = sys.argv[1]

try:
	with open(file_name) as file:
		lines = file.readlines()
except FileNotFoundError:
	sys.exit("File does not exist")

counter = 0
for line in lines:
	if (
		line.strip().startswith("#") or
		line.strip().startswith("\n") or
		line.strip().isspace()
	):
		continue
	elif line.strip() == "":
		continue
	else:
		counter += 1

print(counter)
