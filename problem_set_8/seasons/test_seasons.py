from seasons import time_converter


def test_date():
    assert time_converter(10477) == "Fifteen million, eighty-six thousand, eight hundred eighty minutes"
    assert time_converter(365) == "Five hundred twenty-five thousand, six hundred minutes"
