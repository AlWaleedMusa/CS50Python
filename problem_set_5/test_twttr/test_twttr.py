from twttr import shorten

def main():
	test_all()

def test_all():
	assert shorten("AHMED IBRAHIM MUSA") == "HMD BRHM MS"
	assert shorten("salma yousif mohammed") == "slm ysf mhmmd"
	assert shorten("AllelA AlkhAmeEs") == "lll lkhms"
	assert shorten("wal123") == "wl123"
	assert shorten("waleed!@#") == "wld!@#"

if __name__ == "__main__":
	main()