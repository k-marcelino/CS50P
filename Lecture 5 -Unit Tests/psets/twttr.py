def main():

    word = str(input("Input: ")).strip()
    print(shorten(word))


def shorten(word='twitter'):

    # With List Comphehension
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Empty vowel list to test if it will raise error
    #vowels = []

    # Just leave letter that are not in the list
    # I'm intentionally leaving this part buggy so the test will catch the error..
    # To make it right the code should be:
    #vowelless = ''.join([letter for letter in word if letter.lower() not in vowels])
    vowelless = ''.join([letter for letter in word if letter not in vowels]) #.lower()

    return vowelless


if __name__ == "__main__":
    main()
