class Database:
    def __init__(self):
        # Simulate Users table as an in-memory list
        self.users_table = []

    def initialize_database(self):
        # This function simulates table creation, but since we're using a list, it doesn't do anything
        print("Users table initialized (simulated).")

    def create_user(self, first_name, last_name, user_name, password, initial_amount):
        # Check if the user already exists
        for user in self.users_table:
            if user["User_name"] == user_name:
                print(f"Error: User with username '{user_name}' already exists.")
                return

        # Auto-increment ID
        user_id = len(self.users_table) + 1
        current_balance = initial_amount  # Current balance starts with the initial amount

        # Add user to the "table"
        new_user = {
            "id": user_id,
            "First_name": first_name,
            "Last_name": last_name,
            "User_name": user_name,
            "Password": password,
            "Initial_Amount": initial_amount,
            "Current_Balance": current_balance
        }
        self.users_table.append(new_user)
        print(f"User '{user_name}' created successfully!")

    def show_users(self):
        # Show all users
        if not self.users_table:
            print("No users found.")
        else:
            for user in self.users_table:
                print(f"ID: {user['id']}, Name: {user['First_name']} {user['Last_name']}, "
                      f"Username: {user['User_name']}, Initial Amount: {user['Initial_Amount']}, "
                      f"Current Balance: {user['Current_Balance']}")
