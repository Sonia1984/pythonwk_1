from banking_pkg import account 

print("Welcome to Fisher Bank")
Userpin =  1234
Trials = 3
Username = "Mary"


def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("  === Automated Teller Machine ===   ")
balance = 0
balance_str = str(balance)
print("Balance as a string:", balance_str)

while Trials != 0:
    Pin = int(input("Please enter your 4 digit pin number:"))
    if Pin != Userpin:
        Trials -= 1
        print("Wrong Pin number, You have", Trials, "Trials Left")
    name = input("Enter name to register:")
    if name != Username:
        print("Invalid Name")
    else:
        print("Login Successful!")
    break
        

while True:
    print("What would you like to do?")
    option = input("Choose an option:")
    user_choice = input("1: Balance, 2: Deposit, 3: Withdraw, 4: Logout:")
    if option == "1":
        account_id = "your_account_id"
        account.show_balance(account_id)
    elif option == "2":
        balance = 100
        deposit_amount = float(input("Enter deposit amount: "))
        updated_balance = account.deposit(balance, deposit_amount)
        account.show_balance(updated_balance)
    elif option == "3":
          balance = 100
          withdraw_amount = float(input("Enter withdraw amount: "))
          updated_balance = account.withdraw(balance, withdraw_amount)
          account.show_withdraw(updated_balance)
    elif option == "4":
        account_id = "your_account_id"
        account.logout(account_id)
        break
    else:
        print("Goodbye Mary")




        
    


   











