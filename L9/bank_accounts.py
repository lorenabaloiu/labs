class BankAccount:
    def __init__(self):
        self._balance = 0

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depunere: {amount} unități. Sold curent: {self._balance}.")
        else:
            print("Suma trebuie să fie pozitivă.")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Fonduri insuficiente.")
        elif amount > 0:
            self._balance -= amount
            print(f"Retragere: {amount} unități. Sold curent: {self._balance}.")
        else:
            print("Suma trebuie să fie pozitivă.")

    def get_balance(self):
        return self._balance

account = BankAccount()
account.deposit(100)
account.withdraw(50)
print("Sold final:", account.get_balance())
