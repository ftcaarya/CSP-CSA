def manage_bank_account():
    balance = 1000  
    while True:
        print("\nBank Account Management")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposited ${amount}. New balance: ${balance}")
        
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print(f"Withdrew ${amount}. New balance: ${balance}")
        
        elif choice == '3':
            print(f"Current balance: ${balance}")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")