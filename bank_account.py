import os
os.system('clear')

user_list = []
account_list = []
first_name = ''
last_name = ''
middle_name = ''
account_type = ''
balance = 0.0
current_user = None
current_account = None
action =''
transfer = 0.0

class User:
    def __init__(self,first_name,last_name,middle_name):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
    def __repr__(self):
        return (f"{self.last_name}, {self.first_name} {self.middle_name[0]}")

class BankAccount:
    def __init__(self,user,account_type,balance):
        self.user = user
        self.account_type = account_type
        self.balance = float(balance)
        self.status = "Open"

    def __repr__(self):
        return (f"{self.user}, [{self.account_type}] [{self.status}] Current Balance: ${self.balance} ")

    def close_account(self):
        self.status = "Closed"
        input("Press enter to continue")
        action_list(current_user,current_account)
    
    def freeze_account(self):
        self.status = "Frozen"

    def add_funds(self,deposit):
        self.balance = self.balance + deposit

    def withdrawl_funds(self,withdrawl):
        self.balance = self.balance - withdrawl
        self.overdraft_check()

    def overdraft_check(self):
        if self.balance < 0.0 :
            self.balance = self.balance -35.00
            print("You have over drawn the your account.") 
            print("A fee of $35.00 has been applied.")

def create_user():
    os.system('clear')
    first_name = input("What is the first name for the account? \n")
    last_name = input("What is the last name for the account? \n")
    middle_name = input("What is the middle name for the account? \n")
    user_list.append (User(first_name,last_name,middle_name))

def create_account(current_user):
    os.system('clear')
    user=current_user
    account_type = input("Is this a checking or saving account? \n")
    balance = float(input("Please enter your opening deposit amount: "))
    if balance < 100.00:
        print("You must deposit at least $100.00 to open an account.")
        return
    account_list.append(BankAccount(user,account_type,balance))
    print(account_list[:])
    input("Press enter to continue")

def working_on_it():
    os.system('clear')
    print("working on it")
    input("Press enter to continue")
    action_list(current_user,current_account)

def action_list(current_user,current_account):
    os.system('clear')
    print(f"The current user is: {current_user}")
    print(f"The current account is {current_account}")
    print("#" * 30)
    print(" ")
    print("What action would you like to preform?")
    print(' 1) Add user')
    print(' 2) Change user')
    print(' 3) Open account')
    print(' 4) Change account')
    print(' 5) Close acount ')
    print(' 6) Deposit')
    print(' 7) Withdrawl')
    print(' 8) Transfer')
    print(' 9) EXIT')
    action = input()

    try:   
        if action == '1':
            create_user()
            current_user = user_list[-1]
            input("Press enter to continue")
            action_list(current_user,current_account)
        elif action == '2':
            user_number = int(input("Enter user number: "))
            current_user = user_list[user_number]
            action_list(current_user,current_account)
        elif action == '4':
            account_number = int(input("Enter account number: "))
            current_account = account_list[account_number]
            action_list(current_user,current_account)
        elif action == '3':
            create_account(current_user)
            current_account =account_list[-1]
            action_list(current_user,current_account)
        elif action == '5':
            current_account.close_account()
        elif action == '6':
            deposit = float(input("Enter the amount of the deposit: "))
            current_account.add_funds(deposit)
            print(f"You new account balance is {current_account.balance}")
            print(input("Press enter to continue"))
            action_list(current_user,current_account)
        elif action == '7':
            withdrawl = float(input("Enter the amount of the withdrawl: "))
            current_account.withdrawl_funds(withdrawl)
            print(f"You new account balance is {current_account.balance}")
            print(input("Press enter to continue"))
            action_list(current_user,current_account)
        elif action == '8':
            os.system('clear')
            recieve = int(input("Enter the account to tranfer to: [enter 1 for this test]"))
            transfer = float(input("Enter the amout to transfer: "))
            withdrawl = transfer
            deposit = transfer
            current_account.withdrawl_funds(withdrawl)
            target_account = account_list[recieve]
            target_account.add_funds(deposit)
            print(f"${transfer} has been moved from \n {current_account.user} [{current_account.account_type}] with a new balance of: ${current_account.balance} \n to \n {target_account.user} [{target_account.account_type}] with a new balance of: ${target_account.balance}")
            print(input("Press enter to continue"))
            action_list(current_user,current_account)
        elif action == '9':
            exit
        else:
            print("invalid selection")
            input()
            action_list(current_user,current_account)
    except(IndexError):
        print("Invailid account number")
        print(input("Press enter to continue"))
        action_list(current_user,current_account)




action_list(current_user,current_account)











