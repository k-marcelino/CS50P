from um import count


def test_expected_values():
    assert(count('hello, um, world') == 1)
    assert(count('um, hello, um, world') == 2)
    assert(count('um...') == 1)
    assert(count('Um, thanks for the album.') == 1)

def test_um_inside_words():
    assert(count('yum') == 0)
    assert(count('yummy') == 0)
    assert(count('UMA') == 0)

# In the terminal run "pytest test_um.py"