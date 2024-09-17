import mysql.connector
import pandas as pd
from mysql.connector import Error
import datetime
from tabulate import tabulate


class ATM_Management:
    def __init__(self):
        # Initialize database connection and cursor
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Anny@626",
                database="atm_management"
            )
            self.cursor = self.conn.cursor()
            self.current_user = None  # Track the currently logged-in user
            self.balance = 0
            self.User_ID = None  # Track the user's ID
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def signup_user(self, First_name, Last_name, User_name, Password, Initial_Amount):
        try:
            # Insert user details into the Users table
            query = '''INSERT INTO Users
                       (First_name, Last_name, User_name, Password, Initial_Amount, Current_Balance)
                       VALUES (%s, %s, %s, %s, %s, %s)'''
            self.cursor.execute(query, (First_name, Last_name, User_name, Password, Initial_Amount, Initial_Amount))
            self.conn.commit()
            print("Signup successful")
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def login(self, User_name, Password):
        try:
            # Retrieve the user's password, balance, and ID from the database
            query = "SELECT Password, Current_Balance, id FROM Users WHERE User_name = %s"
            self.cursor.execute(query, (User_name,))
            result = self.cursor.fetchone()

            if result and result[0] == Password:
                self.current_user = User_name
                self.balance = result[1]
                self.User_ID = result[2]
                print("Login successful!")
                return True  # Return True for successful login
            else:
                print("Invalid username or password.")
                return False  # Return False for failed login
        except mysql.connector.Error as e:
            print(f"Error: {e}")
            return False

    def update_balance_in_db(self, curr_balance, amount, transaction_type):
        try:
            # Update the balance in the Users table
            query = "UPDATE Users SET Current_Balance = %s WHERE id = %s"
            self.cursor.execute(query, (curr_balance, self.User_ID))
            self.record_transaction(transaction_type, amount)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def record_transaction(self, transaction_type, amount):
        try:
            # Insert a new record into the Transactions table
            query = '''INSERT INTO Transaction
                       (User_ID, Transaction_Type, Amount, Transaction_Date)
                       VALUES (%s, %s, %s, %s)'''
            self.cursor.execute(query, (self.User_ID, transaction_type, amount, datetime.datetime.now()))
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error: {e}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.update_balance_in_db(self.balance, amount, "Deposit")
            print(f"Deposited {amount} into your account.")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.update_balance_in_db(self.balance, amount, "Withdraw")
                print(f"Withdrew {amount} from your account.")
            else:
                print("Insufficient funds")
        else:
            print("Invalid amount")

    def display_balance(self):
        if self.current_user:
            print(f"Your current balance is {self.balance}")
        else:
            print("You need to login first.")

    def show_transaction(self):
        if self.current_user:
            try:
                # Fetch all transactions for the logged-in user
                query = '''SELECT Transaction_id, Transaction_Type, Amount, Transaction_Date
                           FROM Transaction
                           WHERE User_ID = %s
                           ORDER BY Transaction_Date DESC'''
                self.cursor.execute(query, (self.User_ID,))
                transactions = self.cursor.fetchall()

                if transactions:
                    # Convert the result into a DataFrame for better presentation
                    df = pd.DataFrame(transactions, columns=['Transaction ID', 'Type', 'Amount', 'Date & Time'])

                    # Format 'Date & Time' column for better readability
                    df['Date & Time'] = pd.to_datetime(df['Date & Time']).dt.strftime('%Y-%m-%d %H:%M:%S')

                    # Save the DataFrame to a CSV file for record-keeping
                    csv_filename = f"transactions_for_user_{self.User_ID}.csv"
                    df.to_csv(csv_filename, index=False)

                    # Display the DataFrame using tabulate for a clean output
                    print("\nRecent Transactions:")
                    print(tabulate(df, headers='keys', tablefmt='pretty', showindex=False))

                else:
                    print("No transactions found for this user.")

            except mysql.connector.Error as e:
                print(f"Error: {e}")
        else:
            print("You need to login first.")

    def main_menu(self):
        while True:
            print("\nATM Menu")
            print("1. Login")
            print("2. Signup")
            print("3. Quit")

            choice = input("Select an option (1-3): ")

            if choice == '1':
                User_name = input("Enter Username: ")
                Password = input("Enter Password: ")
                if self.login(User_name, Password):
                    # Show ATM options after login
                    self.user_menu()
            elif choice == '2':
                First_name = input("Enter First Name: ")
                Last_name = input("Enter Last Name: ")
                User_name = input("Enter Username: ")
                Password = input("Enter Password: ")
                Initial_Amount = float(input("Enter Initial Amount: "))
                self.signup_user(First_name, Last_name, User_name, Password, Initial_Amount)
            elif choice == '3':
                print("Thank you for using this ATM.")
                break
            else:
                print("Invalid option. Please select a valid option.")

    def user_menu(self):
        while True:
            print("\nATM Operations Menu")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Show Transactions")
            print("5. Logout")

            choice = input("Select an option (1-5): ")

            if choice == '1':
                try:
                    amount = float(input("Enter amount to deposit: "))
                    self.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == '2':
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    self.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a valid amount.")
            elif choice == '3':
                self.display_balance()
            elif choice == '4':
                self.show_transaction()  # No need to pass User_ID, it's already tracked by the object
            elif choice == '5':
                print("Logged out successfully.")
                break
            else:
                print("Invalid option. Please select a valid option.")


if __name__ == "__main__":
    atm = ATM_Management()
    atm.main_menu()


# def ATM():
#     pass
#
#
# def main():
#     atm = ATM()
#
#     while True:
#         print("\nATM Menu")
#         print("1. Login")
#         print("2. Signup")
#         print("3. Quit")
#
#         choice = input("Select an option (1-3): ")
#
#         if choice == '1':
#             User_name = input("Enter User_name: ")
#             Password = input("Enter Password: ")
#             atm.login(User_name, Password)
#         elif choice == '2':
#             # User_id = input("Enter user_ID: ") - autoincrement
#             First_name = input("Enter First_name: ")
#             Last_name = input("Enter Last_name: ")
#             User_name = input("Enter User_name: ")
#             Password = input("Enter Password: ")
#             Initial_Amount = input("Initial_Amount: ")
#             Current_Balance = Initial_Amount
#             atm.signup(First_name, Last_name, User_name, Password, Initial_Amount, Current_Balance)
#         else:
#             print("Thank you")
