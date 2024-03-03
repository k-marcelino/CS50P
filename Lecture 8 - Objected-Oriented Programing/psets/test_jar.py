from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(20)
    assert jar.capacity == 20


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    with pytest.raises(ValueError):
        jar = Jar()
        assert(jar.deposit(13))
        assert(jar.deposit(20))

def test_withdraw():
    with pytest.raises(ValueError):
        jar = Jar()
        assert(jar.withdraw(1))

# In the terminal run "pytest test_jar.py"