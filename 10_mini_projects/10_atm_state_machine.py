"""10_atm_state_machine.py - Mini project: an ATM that follows rules."""


class ATM:
    MAX_ATTEMPTS = 3

    def __init__(self, pin: str, balance: float):
        self._pin = pin
        self.balance = balance
        self.state = "idle"          # idle -> active, or locked
        self.failed_attempts = 0

    def insert_card(self, pin: str) -> str:
        if self.state == "locked":
            return "Card is locked. Contact your bank."
        if pin == self._pin:
            self.state = "active"
            self.failed_attempts = 0
            return "PIN accepted."
        self.failed_attempts += 1
        if self.failed_attempts >= self.MAX_ATTEMPTS:
            self.state = "locked"
            return "Too many wrong PINs. Card locked."
        return f"Wrong PIN ({self.MAX_ATTEMPTS - self.failed_attempts} tries left)."

    def withdraw(self, amount: float) -> str:
        if self.state != "active":
            return "Please insert your card first."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Dispensed ${amount}. Balance: ${self.balance}"

    def eject(self) -> str:
        if self.state == "active":
            self.state = "idle"
        return "Card ejected."


if __name__ == "__main__":
    atm = ATM("1234", 300)
    print(atm.withdraw(50))
    print(atm.insert_card("0000"))
    print(atm.insert_card("1234"))
    print(atm.withdraw(120))
    print(atm.withdraw(500))
    print(atm.eject())
    for _ in range(3):
        print(atm.insert_card("9999"))
    print(atm.insert_card("1234"))
