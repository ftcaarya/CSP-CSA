def account_balance():
    trans = float(input("Transaction: "))
    acc = trans

    while trans != 0:
        if acc < 250.00:
            print(f"WARNING: Your balance of ${acc:.2f} is less than $250.")
        if acc < 0.00:
            print(f"ALERT: Your account has a negative balance of ${acc:.2f}!")

        trans = float(input("Transaction: "))
        acc += trans

    print(f"Your final balance is ${acc:.2f}.")


account_balance()
