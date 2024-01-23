from plates import is_valid

def test_all_letters():
	assert is_valid("waleed") == True
	assert is_valid("wal05p") == False
	assert is_valid("12AMHERE") == False


def test_mixed_letters():
	assert is_valid("abc123") == True
	assert is_valid("cs50") == True
	assert is_valid("cs05") == False
	assert is_valid("XYZ012") == False
	assert is_valid("AB12C3") == False

def test_upper():
	assert is_valid("IAM HEARE") == False
	assert is_valid("waleeeeeed") == False


def test_others():
	assert is_valid("wale!1") == False
	assert is_valid("123wal") == False
	assert is_valid("wa") == True
	assert is_valid("12") == False
	assert is_valid("/B^D3*") == False
