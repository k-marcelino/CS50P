amount = 50
coin = 25
print (f"Amount Due: {amount}")

while amount > 0:
    

    # while coin not in [5, 10, 25]:
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        pass
    else:
        print(f"Amount Due: {amount}")
        continue

    amount -= coin

    print(f"Amount Due: {amount}") if amount > 0 else print(f"Change Owed: {abs(amount)}")