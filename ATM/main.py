from atm import *


def main():
    print("Welcome to the ATM!")

    accounts = read_accounts()

    while True:
        try:
            account = input("Enter your account number (or type 'exit' to quit): ")
            if account.lower() == 'exit':
                print("Goodbye!")
                return

            pin = input("Enter your PIN: ")

            if validate_pin(accounts, account, pin):
                print(f"Welcome, Account {account}!")
                break
            else:
                print("Invalid account or PIN. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")

    while True:
        try:
            print("\n1. Check balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Transfer")
            print("5. Change PIN")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                print(f"Balance: {check_balance(accounts, account)}")

            elif choice == '2':
                try:
                    amount = int(input("Enter amount to deposit: "))
                    if amount <= 0:
                        print("Amount must be positive.")
                    else:
                        print(deposit(accounts, account, amount))
                        write_accounts(accounts)
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            elif choice == '3':
                try:
                    amount = int(input("Enter amount to withdraw: "))
                    if amount <= 0:
                        print("Amount must be positive.")
                    else:
                        print(withdraw(accounts, account, amount))
                        write_accounts(accounts)
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            elif choice == '4':
                account2 = input("Enter destination account number: ")
                try:
                    amount = int(input("Enter amount to transfer: "))
                    if amount <= 0:
                        print("Amount must be positive.")
                    else:
                        print(transfer(accounts, account, account2, amount))
                        write_accounts(accounts)
                except ValueError:
                    print("Invalid amount. Please enter a number.")

            elif choice == '5':
                print(change_pin(accounts, account))
                write_accounts(accounts)

            elif choice == '6':
                print("Goodbye!")
                write_accounts(accounts)
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


main()
