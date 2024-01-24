import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
	sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
	sys.exit("Too many command-line arguments")

before_img = sys.argv[1]
after_img = sys.argv[2]

extensions = ["jpeg" ,"jpg" ,"png"]
first_ext = before_img.split(".", maxsplit=1)
second_ext = after_img.split(".", maxsplit=1)

if first_ext[1] not in extensions or second_ext[1] not in extensions:
	sys.exit("Invalid output")
elif first_ext[1] != second_ext[1]:
	sys.exit("Input and output have different extensions")


try:
	shirt = Image.open("shirt.png")
	photo = Image.open(before_img)

	a, b = shirt.size
	photo = ImageOps.fit(photo, (a, b))

	photo.paste(shirt, shirt)
	photo.save(after_img)

except FileNotFoundError:
	sys.exit("Input does not exist")
