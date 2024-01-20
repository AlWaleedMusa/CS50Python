import pyfiglet
import sys

if len(sys.argv) == 1:
    user = input("Input: ")
    f = pyfiglet.figlet_format(user)
    print("Output: ")
    print(f)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    fonts = pyfiglet.FigletFont.getFonts()
    if sys.argv[2] in fonts:
        user = input("Input: ")
        font_string = sys.argv[2]
        font = pyfiglet.Figlet(font=font_string)
        print("Output: ")
        print(font.renderText(user))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
