# Main Code
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # Control Variables
    alpha_count = 0
    num_count = 0

    # First iterate through all characters and check if it's alpha, numeric or others.. then counts which one
    for char in s:
        if char.isalpha():
            alpha_count += 1

        elif char.isnumeric():
            num_count += 1
            # Checking condition where the first number cannot be a zero
            if (num_count == 1) and (int(char) == 0):
                return False

        # If is not an alphanumeric character, then break the code
        else:
            return False


    # Checking conditions on:
        # First 2 chars being letters;
        # the range of lenght, minimun 2 and maximum 6;
        # At least 2 alpha chars;
        # if there are any numbers, the last chars must be equal the number of numeric ones
    if (s[:2].isalpha()) and (2 <= len(s) <= 6) and (alpha_count >= 2) and (((num_count > 0) and (s[-num_count:].isnumeric())) or (num_count == 0)):
        return True

    else:
        return False


if __name__ == "__main__":
    main()
