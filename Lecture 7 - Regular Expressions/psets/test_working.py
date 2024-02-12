from working import convert
import pytest

def test_expected_values():
    assert(convert('9 AM to 5 PM') == '09:00 to 17:00')
    assert(convert('9:00 AM to 5:00 PM') == '09:00 to 17:00')
    assert(convert('9 AM to 5:30 PM') == '09:00 to 17:30')
    assert(convert('10 PM to 8 AM') == '22:00 to 08:00')

def test_wrong_connector():
    with pytest.raises(ValueError):
        assert(convert('9 AM - 5 PM'))
        assert(convert('0 AM - 17:00 PM'))
        assert(convert('0 AM 17:00 PM'))

def test_hour_outside_range():
    with pytest.raises(ValueError):
        assert(convert('13 AM to 15 PM'))

def test_minute_outside_range():
    with pytest.raises(ValueError):
        assert(convert('9:60 AM to 5:60 PM'))

def test_non_numerical():
    with pytest.raises(ValueError):
        assert(convert("cat"))
        assert(convert("text"))

# In the terminal run "pytest test_working.py"