import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

	matches = re.search(r"\"https?://(?:www.)?youtube.com/embed/(\w+)\"", s)
	if matches:
		video_code = matches.group(1)
	else:
		return None
	
	prefix = "https://youtu.be/"
	final_string = prefix + video_code

	return final_string


if __name__ == "__main__":
	main()
