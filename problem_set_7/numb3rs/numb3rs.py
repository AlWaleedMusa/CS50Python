import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
	try:
		matches = re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)
		if matches:
			ip1 = int(matches.group(1))
			ip2 = int(matches.group(2))
			ip3 = int(matches.group(3))
			ip4 = int(matches.group(4))
			if ip1 <= 255 and ip2 <= 255 and ip3 <= 255 and ip4 <= 255:
				return True
			else:
				return False
		else:
			return False
	except AttributeError:
		return False



if __name__ == "__main__":
    main()
