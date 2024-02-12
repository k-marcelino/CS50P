from numb3rs import validate


def test_expected_values():
    assert(validate("255.255.255.255") == True)
    assert(validate("127.0.0.1") == True)

def test_out_range_255():
    assert(validate("275.3.6.28") == False)
    assert(validate("10.-5.6.28") == False)
    assert(validate("3.17.299.28") == False)
    assert(validate("1.2.255.275") == False)

def test_no_dots():
    assert(validate("255255255255") == False)

def test_not_4_bytes():
    assert(validate("99.99.99.99.99") == False)
    assert(validate("5.5.5.5.5.5.5.5.5") == False)
    assert(validate("255") == False)
    assert(validate("1.2") == False)

def test_non_numerical():
    assert(validate("cat") == False)
    assert(validate("text") == False)

# in the terminal (same directory) execute: pytest test_numb3rs.py