"""01_bank_system.py - Mini project: a bank with accounts and transfers."""


class Account:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self, amount: float) -> None:
        self.balance += amount
        self.history.append(f"deposit {amount}")

    def withdraw(self, amount: float) -> None:
        if amount > self.balance:
            raise ValueError(f"{self.owner} has insufficient funds")
        self.balance -= amount
        self.history.append(f"withdraw {amount}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, owner: str, balance: float = 0) -> Account:
        self.accounts[owner] = Account(owner, balance)
        return self.accounts[owner]

    def transfer(self, sender: str, receiver: str, amount: float) -> None:
        self.accounts[sender].withdraw(amount)
        self.accounts[receiver].deposit(amount)


if __name__ == "__main__":
    bank = Bank()
    bank.open_account("Ada", 500)
    bank.open_account("Ben", 100)

    bank.transfer("Ada", "Ben", 150)
    try:
        bank.transfer("Ben", "Ada", 1000)
    except ValueError as error:
        print("Transfer failed:", error)

    for account in bank.accounts.values():
        print(f"{account.owner}: ${account.balance} | {account.history}")
