from plates import is_valid


def test_start_with_2_letters():
    assert(is_valid("12") == False)


def test_min_max_chars():
    assert(is_valid("C") == False)
    assert(is_valid("EXCENDING") == False)


def test_numbers_in_middles():
    assert(is_valid("AAA22A") == False)


def test_non_alphanum_chars():
    assert(is_valid("Hello, World") == False)
    assert(is_valid("HI!@*") == False)


def test_first_num_zero():
    assert(is_valid("AAA022") == False)
