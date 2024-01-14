from twttr import shorten

def test_default():
    tests_dict = {
        'twitter': 'twttr',
        "What's your name?": "Wht's yr nm?",
        'CS50': 'CS50'
    }

    # Don't know why did not work with list comprehension
    #[assert(shorten(key) == value) for key, value in tests_dict.items()]

    # Testing all values in the dict
    for key, value in tests_dict.items():
        assert(shorten(key) == value)


def test_lower_case():

    # With List Comphehension
    vowels = ['a', 'e', 'i', 'o', 'u']

    for letter in vowels:
        assert(shorten(letter) == '')

def test_upper_case():

    # With List Comphehension
    vowels = ['A', 'E', 'I', 'O', 'U']

    for letter in vowels:
        assert(shorten(letter) == '')
