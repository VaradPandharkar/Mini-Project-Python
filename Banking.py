def show_balance():
    print(f"Your balance is ${balance:.2f}")

def Deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def Withdraw():
    amount = float(input("Enter amount to be Withdrwan: "))
    if amount > balance:
        print("Insufficient Funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0 ")
        return 0
    else:
        return amount


balance = 0
is_running = True

while is_running:
    print("Banking Program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your Choice (1 - 4): ")

    if choice == '1':
        show_balance()
    elif choice == '2':
        balance += Deposit()
    elif choice == '3':
        balance -= Withdraw()
    elif choice == '4':
        is_running = False 
    else:
        print("That is not a Valid")

print("Thank You! Have a Nice Day")