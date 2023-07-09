import pandas as pd
import matplotlib.pyplot as plt

class Account:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.contact = ""
        self.password = ""
        self.balance = 0

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address
    
    def set_contact(self, contact):
        self.contact = contact

    def get_contact(self):
        return self.contact
    
    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password
    
    def set_balance(self, balance):
        self.balance += balance

    def get_balance(self):
        return self.balance


def save_accountsExcel(account_list, filename):
    data = {
        'Name': [],
        'Address': [],
        'Contact': [],
        'Password': [],
        'Balance': []
    }
    
    for account in account_list:
        data['Name'].append(account.get_name())
        data['Address'].append(account.get_address())
        data['Contact'].append(account.get_contact())
        data['Password'].append(account.get_password())
        data['Balance'].append(account.get_balance())
    
    df = pd.DataFrame(data)
    
    file_extension = filename.split('.')[-1]
    if file_extension == 'xlsx':
        try:
            df.to_excel(filename, index=False)
            print("Account info saved successfully!")
        except Exception as e:
            print(f"Error saving the Excel file: {str(e)}")
    elif file_extension=='csv':
        try:
            df.to_csv(filename, index = False)
            print("Account info saved successfully!")
        except Exception as e:
            print(f"Error saving the csv file: {str(e)}")
    elif file_extension=='sql':
        try:
            df.to_sql(filename, index = False)
            print("Account info saved successfully!")
        except Exception as e:
            print(f"Error saving the sql file: {str(e)}")
    elif file_extension=='txt':
        try:
            with open(filename, "w") as file:
                for account in account_list:
                    file.write(f"Name: {account.get_name()}\n")
                    file.write(f"Address: {account.get_address()}\n")
                    file.write(f"Contact: {account.get_contact()}\n")
                    file.write(f"Password: {account.get_password()}\n")
                    file.write(f"Balance: {account.get_balance()}\n")
                    file.write("\n")
            print("Account info saved successfully!")
        except Exception as e:
            print(f"Error saving the txt file: {str(e)}")    
    else:
        print("Invalid file type.")

def load_accountsExcel(filename):
    accounts = []
    if filename.endswith(".xlsx"):
        try:
            df = pd.read_excel(filename)  # Read the Excel file using pandas
            for index, row in df.iterrows():
                account = Account()
                account.set_name(row['Name'])
                account.set_address(row['Address'])
                account.set_contact(row['Contact'])
                account.set_password(row['Password'])
                balance_line = row['Balance']
                if balance_line:  # Check if balance_line is not empty
                    account.set_balance(float(balance_line))
                else:
                    account.set_balance(0.0)  # Set a default balance value
                accounts.append(account)

            print("Account info loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        return accounts
    elif filename.endswith(".csv"):
        try:
            df = pd.read_csv(filename)  # Read the Excel file using pandas
            for index, row in df.iterrows():
                account = Account()
                account.set_name(row['Name'])
                account.set_address(row['Address'])
                account.set_contact(row['Contact'])
                account.set_password(row['Password'])
                balance_line = row['Balance']
                if balance_line:  # Check if balance_line is not empty
                    account.set_balance(float(balance_line))
                else:
                    account.set_balance(0.0)  # Set a default balance value
                accounts.append(account)

            print("Account info loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        return accounts
    elif filename.endswith(".txt"):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                for i in range(0, len(lines), 5):
                    account = Account()
                    account.set_name(lines[i].strip()[6:])
                    account.set_address(lines[i + 1].strip()[9:])
                    account.set_contact(lines[i + 2].strip()[9:])
                    account.set_password(lines[i + 3].strip()[10:])
                    balance_line = lines[i + 4].strip()[10:]
                    if balance_line:  # Check if balance_line is not an empty string
                        account.set_balance(float(balance_line))
                    else:
                        account.set_balance(0.0)  # Set a default balance value
                    accounts.append(account)
                    
            print("Account info loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        return accounts
    else:
        print("No such file extension!")


def show_chart(account_list):
    filename = input("Enter the file name to show: ")
    
    try:
        df = pd.read_excel(filename)
        if 'Balance' in df.columns:
            df['Balance'].plot()
            plt.title('Account Balance')
            plt.xlabel('Index')
            plt.ylabel('Balance')
            plt.show()
        else:
            print("The 'Balance' column does not exist in the file.")
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print(f"Error reading the Excel file: {str(e)}")


def create_account(account_list):
    # Logic for creating an account
    account = Account()
    name = input("Enter your name: ")
    account.set_name(name)
    address = input("Enter your address: ")
    account.set_address(address)
    try:
        contact = int(input("Enter your contact no.: "))
        account.set_contact(contact)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        return
    password = input("Enter new password: ")

    account.set_password(password)
    account_list.append(account)

    print("Account created successfully!")


def login(account_list):
    name = input("Enter username: ")
    login_successful = False
    exit_program = False  # Variable to control the outer while loop
    for account in account_list:
        if account.get_name() == name:
            password = input("Enter password: ")
            if account.get_password() == password:
                login_successful = True
                print("Logged in successfully!")
                while not exit_program:  # Loop until exit_program is True
                    print("\nWelcome to your account:")
                    print("1. Account detail")
                    print("2. Save account info to file")
                    print("3. Load account info from file")
                    print("4. Deposit.")
                    print("5. Withdraw.")
                    print("6. Chart of balance flow.")
                    print("7. Log out from your account.")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        display([account])
                    elif choice == "2":
                        filename = input("Enter the filename with .extension to save the account info: ")
                        save_accountsExcel([account], filename)
                    elif choice == "3":
                        filename = input("Enter the filename to load the account info from: ")
                        accounts = load_accountsExcel(filename)
                        if accounts:
                            account_list = accounts
                    elif choice == "4":
                        deposit([account])
                    elif choice == "5":
                        withdraw([account])
                    elif choice == "6":
                        show_chart([account])
                    elif choice == "7":
                        print("Logout successful!\n")
                        exit_program = True  # Set exit_program to True to terminate the outer while loop
                    else:
                        print("Invalid choice. Please try again.")
                break
            else:
                print("Wrong password! Try again.")
                return
    if not login_successful:
        print("Incorrect username.")


def deposit(account_list):
    flag = 0
    for account in account_list:
        filename = input("Enter the file name to save the account info: ")
        while flag == 0:
            password = input("Enter password: ")
            if account.get_password() == password:
                flag = 1

                try:
                    dep = float(input("Enter deposit amount: "))
                    account.set_balance(dep)
                    print("Deposited successfully!")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
            else:
                print("Password wrong. Try again!")
        save_accountsExcel([account], filename)


def withdraw(account_list):
    flag = 0
    for account in account_list:
        filename = input("Enter the file name to save the account info: ")
        while flag == 0:
            password = input("Enter password: ")
            if account.get_password() == password:
                flag = 1
                try:
                    withdraw_amount = float(input("Enter withdraw amount: "))
                    if withdraw_amount > account.get_balance():
                        print("Insufficient balance!")
                    else:
                        account.set_balance(-withdraw_amount)
                        print("Withdrawn successfully!")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        save_accountsExcel([account], filename)


def display(account_list):
    # Display the account details
    print("Account details:")
    for account in account_list:
        print("Name:", account.get_name())
        print("Address:", account.get_address())
        print("Contact:", account.get_contact())
        print("Password: ", "*" * len(account.get_password()))
        print("Balance:", account.get_balance())
        print()


# Main program
accounts = []
exit_program = False

while not exit_program:
    print("Welcome to home page:")
    print("1. Create Account")
    print("2. Login to Account")
    print("3. Load account info from file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account(accounts)
    elif choice == "2":
        login(accounts)
    elif choice == "3":
        filename = input("Enter the filename to load the account info from: ")
        accounts = load_accountsExcel(filename)
    elif choice == "4":
        print("Exited successfully!")
        exit_program = True
    else:
        print("Invalid choice. Please try again.")
