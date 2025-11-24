import random 
 
#-------------------------------- 
# Class for a single bank account 
#-------------------------------- 
class Account: 
    """ 
    Represents a single bank account with basic functionalities like 
    deposit, withdraw, and balance check. 
    """ 
    def __init__(account, name, initial_deposit): 
        account.name = name 
        account.balance = initial_deposit 
        account.account_number = account.generate_account_number() 
        print(f"Account for '{account.name}' created successfully.") 
        print(f"Your Account Number is: {account.account_number}") 
 
    def generate_account_number(account): 
        """Generates a random 10-digit account number.""" 
        return ''.join([str(random.randint(0, 9)) for _ in range(10)]) 
 
    def deposit(account, amount): 
        """Deposits a specified amount into the account.""" 
        if amount > 0: 
            account.balance += amount 
            print(f"Successfully deposited ${amount:.2f}. New balance: ${account.balance:.2f}") 
        else: 
            print("Invalid deposit amount. Please enter a positive number.") 
 
    def withdraw(account, amount): 
        """Withdraws a specified amount from the account if funds are sufficient.""" 
        if 0 < amount <= account.balance: 
            account.balance -= amount 
            print(f"Successfully withdrew ${amount:.2f}. New balance: ${account.balance:.2f}") 
        else: 
            print("Invalid withdrawal amount or insufficient funds.") 
 
    def check_balance(account): 
        """Prints the current balance of the account.""" 
        print(f"Current balance for account {account.account_number}: ${account.balance:.2f}") 
 
    def display_details(account): 
        """Displays the full details of the account.""" 
        print("\n--- Account Details ---") 
        print(f"Account Holder: {account.name}") 
        print(f"Account Number: {account.account_number}") 
        print(f"Balance: ${account.balance:.2f}") 
        print("-----------------------")

    
  
        
 
#-------------------------------- 
# Class for managing the entire bank 
#-------------------------------- 
class Bank: 
    """ 
    Manages all bank accounts and top-level operations like creating, 
    closing, and accessing accounts. 
    """ 
    def __init__(account): 
        account.accounts = {}  # Dictionary to store account_number: Account_object 
 
    def create_account(account): 
        """Guides the user through creating a new account.""" 
        name = input("Enter account holder's name: ") 
        if not name.strip(): 
            print("Name cannot be empty.") 
            return 
             
        try: 
            initial_deposit = float(input("Enter initial deposit amount: $")) 
            if initial_deposit < 0: 
                print("Initial deposit cannot be negative.") 
                return 
            new_account = Account(name, initial_deposit) 
            account.accounts[new_account.account_number] = new_account 
        except ValueError: 
            print("Invalid input for deposit. Please enter a valid number.") 
 
    def find_account(account, account_number): 
        """Finds and returns an account object based on the account number.""" 
        return account.accounts.get(account_number) 
 
    def close_account(account): 
        """Closes an account after confirming with the user.""" 
        account_number = input("Enter the account number to close: ") 
        account = account.find_account(account_number) 
        if account: 
            confirm = input(f"Are you sure you want to close the account for {account.name}? (yes/no): ").lower() 
            if confirm == 'yes': 
                del account.accounts[account_number] 
                print("Account closed successfully.") 
            else: 
                print("Account closure cancelled.") 
        else: 
            print("Account not found.") 
 
    def perform_transaction(account): 
        """Handles transactions for an existing customer.""" 
        account_number = input("Enter your account number: ") 
        account = account.find_account(account_number) 
 
        if not account: 
            print("Account not found. Please check the account number and try again.") 
            return 
 
        print(f"\nWelcome, {account.name}!") 
        while True: 
            print("\nTransaction Menu:") 
            print("1. Deposit") 
            print("2. Withdraw") 
            print("3. Check Balance") 
            print("4. View Account Details") 
            print("5. Return to Main Menu") 
            
             
            try: 
                choice = int(input("Enter your choice (1-5): ")) 
 
                if choice == 1: 
                    amount = float(input("Enter amount to deposit: $")) 
                    account.deposit(amount) 
                elif choice == 2: 
                    amount = float(input("Enter amount to withdraw: $")) 
                    account.withdraw(amount) 
                elif choice == 3: 
                    account.check_balance() 
                elif choice == 4: 
                    account.display_details() 
                elif choice == 5: 
                    break 
                else: 
                    print("Invalid choice. Please enter a number between 1 and 5.") 
            except ValueError: 
                print("Invalid input. Please enter a number.") 
 
#-------------------------------- 
# Main execution block 
#-------------------------------- 
def main(): 
    """The main function to run the bank application.""" 
    my_bank = Bank() 
 
    while True: 
        print("\n===== Welcome to Python Bank =====") 
        print("1. Create New Account") 
        print("2. Access Existing Account") 
        print("3. Close an Account") 
        print("4. Exit") 
         
        try: 
            choice = int(input("Enter your choice (1-4): ")) 
 
            if choice == 1: 
                my_bank.create_account() 
            elif choice == 2: 
                my_bank.perform_transaction() 
            elif choice == 3: 
                my_bank.close_account() 
            elif choice == 4: 
                print("Thank you for using Python Bank. Goodbye!") 
                break 
            else: 
                print("Invalid choice. Please select a valid option.") 
        except ValueError: 
            print("Invalid input. Please enter a number.") 
 
if __name__ == "__main__": 
    main() 
 
 