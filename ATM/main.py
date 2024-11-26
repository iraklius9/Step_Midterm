from atm import *


def main():
    while True:
        print('\n1. Check balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Transfer')
        print('5. Exit')
        choice = input('Choose an option: ')

        if choice == '1':
            account = input('Enter account number: ')
            print(f'Balance: {check_balance(account)}')

        elif choice == '2':
            account = input('Enter account number: ')
            try:
                amount = int(input('Enter amount to deposit: '))
                if amount <= 0:
                    print('Amount must be positive.')
                else:
                    deposit(account, amount)
                    print('Deposit successful')
            except ValueError:
                print('Invalid amount. Please enter a number.')

        elif choice == '3':
            account = input('Enter account number: ')
            try:
                amount = int(input('Enter amount to withdraw: '))
                if amount <= 0:
                    print('Amount must be positive.')
                else:
                    message = withdraw(account, amount)
                    print(message)
            except ValueError:
                print('Invalid amount. Please enter a number.')

        elif choice == '4':
            account1 = input('Enter source account number: ')
            account2 = input('Enter destination account number: ')
            try:
                amount = int(input('Enter amount to transfer: '))
                if amount <= 0:
                    print('Amount must be positive.')
                else:
                    message = transfer(account1, account2, amount)
                    print(message)
            except ValueError:
                print('Invalid amount. Please enter a number.')

        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')


main()
