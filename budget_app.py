class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.__balance = 0.0

    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger_entries = ["{:<23}{:>7.2f}".format(item["description"][:23], item["amount"]) for item in self.ledger]
        total = "Total: {:.2f}".format(self.__balance)
        return header + "\n".join(ledger_entries) + "\n" + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.__balance += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

    def transfer(self, amount, category_instance):
        if self.withdraw(amount, f"Transfer to {category_instance.description}"):
            category_instance.deposit(amount, f"Transfer from {self.description}")
            return True
        return False

    def check_funds(self, amount):
        return self.__balance >= amount


def create_spend_chart(categories):
    spent_amounts = [sum(abs(item["amount"]) for item in cat.ledger if item["amount"] < 0) for cat in categories]
    total_spent = sum(spent_amounts)
    spent_percentage = [int((spent / total_spent) * 10) * 10 for spent in spent_amounts]
    
    header = "Percentage spent by category\n"
    chart = "\n".join(f"{val:>3}| {' '.join('o' if p >= val else ' ' for p in spent_percentage)} " for val in range(100, -1, -10))
    
    footer = "    " + "-" * (3 * len(categories) + 1) + "\n"
    descriptions = [cat.description for cat in categories]
    max_length = max(map(len, descriptions))
    descriptions = [desc.ljust(max_length) for desc in descriptions]
    footer += "\n".join("    " + " ".join(desc[i] for desc in descriptions) + " " for i in range(max_length))
    
    return header + chart + "\n" + footer
