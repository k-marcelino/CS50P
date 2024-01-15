from fuel import gauge, convert
import pytest


### Convert Tests ###
def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("4/3")
#    with pytest.raises(ValueError, match=r".* 123 .*"):
#        4 / 3

def test_convert_values():
    assert(convert("0/4") == 0)
    assert(convert("1/4") == 25)
    assert(convert("2/4") == 50)
    assert(convert("3/4") == 75)
    assert(convert("4/4") == 100)

### Gauge Tests ###
def test_gauge_max():
    assert(gauge(100) == "F")
    assert(gauge(99) == "F")


def test_gauge_min():
    assert(gauge(0) == "E")
    assert(gauge(1) == "E")


def test_gauge_pct():
    assert(gauge(50) == "50%")

