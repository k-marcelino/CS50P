
def main():

    while True:

        # Prompting user for input
        frac = str(input("Fraction: " )).strip()
        # Trying to transform input, if goes wrong will continuously prompt till the input is in the right format
        try:
            if '/' in frac:
                x, y = frac.split('/')
                # Transforming into integers
                x, y = int(x), int(y)

                # Final check before breaks the loop
                if x <= y and y != 0:
                    percentage = convert(frac)
                    break

        except (ValueError, ZeroDivisionError):
            pass

    # Printing result accordingly the remain range
    print(gauge(percentage))



def gauge(percentage):

    # Printing result accordingly the remain range
    if percentage >= 99:
        return 'F'
    elif percentage <= 1:
        return 'E'
    else:
        return(f'{percentage:.0f}%')


def convert(fraction):


    # spliting the input into 2 variables
    #if '/' in fraction:

    # Transforming into integers
    try:
        x, y = fraction.split('/')
        x, y = int(x), int(y)
    except ValueError:
        pass

    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError
    # Final check before breaks the loop
    #if x <= y and y != 0:
    return int(round(x / y * 100, 0))


if __name__ == "__main__":
    main()
