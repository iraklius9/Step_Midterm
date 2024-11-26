import os

DATA_FILE = 'data.txt'


def read_accounts():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return {line.split()[0]: int(line.split()[1]) for line in file}


def write_accounts(accounts):
    with open(DATA_FILE, 'w') as file:
        for account, balance in accounts.items():
            file.write(f'{account} {balance}\n')


def check_balance(account):
    accounts = read_accounts()
    return accounts.get(account, 'Account not found')


def deposit(account, amount):
    accounts = read_accounts()
    if account in accounts:
        accounts[account] += amount
    else:
        accounts[account] = amount
    write_accounts(accounts)


def withdraw(account, amount):
    accounts = read_accounts()
    if account not in accounts:
        return 'Account not found'
    if accounts[account] < amount:
        return 'Not enough funds'
    accounts[account] -= amount
    write_accounts(accounts)
    return 'Operation was successful'


def transfer(account1, account2, amount):
    accounts = read_accounts()
    if account1 not in accounts:
        return 'Account not found'
    if accounts[account1] < amount:
        return 'Not enough funds'
    accounts[account1] -= amount
    accounts[account2] += amount
    write_accounts(accounts)
    return 'Operation was successful'
