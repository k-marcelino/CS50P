menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Control Variable
total = 0

while True:

    # Try to get user input
    try:
        item = str(input('Item: ')).strip().title()
    except EOFError:
        print('\n')
        break

    # if item == 'D':
    #     break

    if item in menu:
        total += menu[item]
        # Print Result
        print(f"Total: ${total:.2f}")

