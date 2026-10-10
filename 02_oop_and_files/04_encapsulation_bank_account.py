"""04_encapsulation_bank_account.py - Protect data inside a class."""


class InsufficientFundsError(Exception):
    """Raised when a withdrawal is bigger than the balance."""


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = balance  # the underscore means "please don't touch directly"

    @property
    def balance(self) -> float:
        """Read-only access to the balance."""
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount > self._balance:
            raise InsufficientFundsError(f"Balance is only {self._balance}")
        self._balance -= amount


if __name__ == "__main__":
    account = BankAccount("Tola", 100)
    account.deposit(50)
    account.withdraw(30)
    print(f"{account.owner} has ${account.balance}")

    try:
        account.withdraw(500)
    except InsufficientFundsError as error:
        print("Could not withdraw:", error)
