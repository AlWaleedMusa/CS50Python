import sys
import csv

if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
	sys.exit("Not a Python file ")
elif sys.argv[2][-4:] != ".csv":
	sys.exit("File to write to is not a csv format")

file_read = sys.argv[1]
file_write = sys.argv[2]

names_list = []
try:
	with open(file_read) as file:
		reader = csv.DictReader(file)
		for i in reader:
			i = dict(i)
			for k, v in i.items():
				names_list.append(v.strip())
except FileNotFoundError:
	sys.exit("Could not read {}".format(file_read))

new_list = []
for i in range(len(names_list)):
	if i % 2 == 0:
		last_name, first_name = names_list[i].split(",")
		new_dict = {"first" : first_name.strip(), "last" : last_name.strip()}
		new_list.append(new_dict)
	else:
		school = names_list[i]
		new_dict.update({"house" : school})
		
with open(file_write, "w", newline="") as file:
	writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
	writer.writeheader()
	for i in range(len(new_list)):
		writer.writerow(new_list[i])