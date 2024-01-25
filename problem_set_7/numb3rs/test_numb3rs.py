from numb3rs import validate

def test_nums():
	assert validate("1.2.3.4") == True
	assert validate("12.13.14.15") == True
	assert validate("123.134.145.156") == True
	assert validate("255.255.255.256") == False

def test_all():
	assert validate("cat") == False
	assert validate("12.12.12.cat") == False
	assert validate("12/12/12/12") == False
	assert validate(" ") == False
	assert validate("hi.i.am.here") == False
	assert validate("1,2.3,4") == False
	assert validate("waleed 11.11.11.11") == False
