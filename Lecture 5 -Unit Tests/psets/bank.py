def main():

    # Prompts user for a greeting
    greeting = str(input("Hello, Newman \n")).strip().lower()
    #print(greeting)
    print(value(greeting))


# Modified function so the test_bank.py will catch the errors
def value(greeting):
    # It was not working before transforming inside of the function contray to do this directly when inputing
    greeting = str(greeting).lower()

    # Checking conditions and responding accordingly
    if greeting.startswith("hello"):
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

# Right Solution
# def value(greeting):
#    # Checking conditions and responding accordingly
#    if greeting.startswith("hello"):
#        return int(0)
#    elif greeting[0] == 'h':
#        return int(20)
#    else:
#        return int(100)
#

if __name__ == "__main__":
    main()
