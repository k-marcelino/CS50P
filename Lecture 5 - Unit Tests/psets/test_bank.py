from bank import value


def test_hello():
    assert(value("hello") == 0)


def test_case_sensitive():
    assert(value("HeLlO") == 0)


def test_h():
    assert(value("H") == 20)
    assert(value("Hey") == 20)


def test_otherwise():
    assert(value("Anything else") == 100)
    assert(value("What's up") == 100)
