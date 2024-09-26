class BankAccount:
    # Create a Bank Account class with two attributes.
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    # Create a deposit method that increases the account's balance by the specified amount.
    def deposit(self, amount):
        self.balance += amount
        return self

    # Create a withdrawal method that decreases the account's balance by the specified amount.
    # Include a condition that if the balance goes below 0, charge a $5 fee.
    def withdrawal(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= (amount + 5)
        else:
            self.balance -= amount
        return self

    # Create a display method that prints the account's balance.
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    # Create a yield interest method that increases the account balance by the current balance * the interest rate
    # (as long as the balance is positive).
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self

class User:
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.bank_account = BankAccount(int_rate, balance)

    def make_deposit(self, amount):
        self.bank_account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.bank_account.withdrawal(amount)
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.bank_account.balance}")

# Test the User class
user1 = User("John Doe", "john@example.com", 0.01, 200)
user2 = User("Alice Smith", "alice@example.com", 0.2, 500)

# Display account balance for user1
user1.display_user_balance()

# Display account balance for user2
user2.display_user_balance()



