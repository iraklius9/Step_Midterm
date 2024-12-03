import os

DATA_FILE = 'data.txt'


def read_accounts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        accounts = {}
        for line in file:
            account, pin, balance = line.split()
            accounts[account] = {'pin': pin, 'balance': int(balance)}
        return accounts


def write_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        for account, details in accounts.items():
            file.write(f"{account} {details['pin']} {details['balance']}\n")


def validate_pin(accounts, account, pin):
    if account in accounts and accounts[account]['pin'] == pin:
        return True
    return False


def check_balance(accounts, account):
    return accounts[account]['balance'] if account in accounts else 'Account not found'


def deposit(accounts, account, amount):
    if account in accounts:
        accounts[account]['balance'] += amount
        write_accounts(accounts)
        return 'Deposit successful.'
    return 'Account not found.'


def withdraw(accounts, account, amount):
    if account not in accounts:
        return 'Account not found.'
    if accounts[account]['balance'] < amount:
        return 'Not enough funds.'
    accounts[account]['balance'] -= amount
    write_accounts(accounts)
    return 'Withdrawal successful.'


def transfer(accounts, account1, account2, amount):
    if account1 not in accounts or account2 not in accounts:
        return 'One or both accounts not found.'
    if accounts[account1]['balance'] < amount:
        return 'Not enough funds.'
    accounts[account1]['balance'] -= amount
    accounts[account2]['balance'] += amount
    write_accounts(accounts)
    return 'Transfer successful.'


def change_pin(accounts, account):
    if account in accounts:
        while True:
            current_pin = input("Enter your current PIN (or type 'exit' to cancel): ")
            if current_pin.lower() == 'exit':
                return "PIN change canceled."

            if accounts[account]['pin'] == current_pin:
                while True:
                    new_pin = input("Enter your new PIN(4 digits): ")
                    confirm_pin = input("Confirm your new PIN: ")
                    if new_pin == confirm_pin and len(new_pin) == 4:
                        accounts[account]['pin'] = new_pin
                        write_accounts(accounts)
                        return "PIN changed successfully."
                    else:
                        print("PIN confirmation does not match. Please try again.")
            else:
                print("Incorrect current PIN. Please try again.")
    return "Account not found."
