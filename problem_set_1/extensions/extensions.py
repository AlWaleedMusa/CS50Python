def main():

	prefix = {"gif": "image/gif", "jpg": "image/jpeg", "jpeg": "image/jpeg", "png": "image/png", "pdf": "application/pdf", "txt": "text/plain", "zip": "application/zip"}

	user_input = input("File name: ").strip().lower()
	extension_list = user_input.split(".")
	ext = extension_list[-1]

	for k, v in prefix.items():
		if k == ext:
			print(v)

	if ext not in prefix.keys():
		print("application/octet-stream")

if __name__ == "__main__":
	main()
