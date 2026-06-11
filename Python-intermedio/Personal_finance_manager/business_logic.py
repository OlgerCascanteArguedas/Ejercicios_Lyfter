class Category:
    def __init__(self, name):
        self.name = name

class Transaction:
    def __init__(self, title, amount, category, transaction_type):
        self.title = title
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

    def to_list(self):
        return [
            self.title,
            self.amount,
            self.category,
            self.transaction_type
        ]

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "transaction_type": self.transaction_type
        }
class FinanceManager:
    def __init__(self):
        self.categories = []
        self.transactions = []

    def add_category(self, name):
        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty")

        if name in self.categories:
            raise ValueError("Category already exists")

        self.categories.append(name)

    def add_transaction(self, title, amount, category, transaction_type):
        title = title.strip()

        if not self.categories:
            raise ValueError("No categories available")

        if not title:
            raise ValueError("Title cannot be empty")

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be numeric")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        if category not in self.categories:
            raise ValueError("Category does not exist")

        if transaction_type not in ["Income", "Expense"]:
            raise ValueError("Invalid transaction type")

        transaction = Transaction(
            title,
            amount,
            category,
            transaction_type
        )

        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0

        for transaction in self.transactions:
            if transaction.transaction_type == "Income":
                balance += transaction.amount
            elif transaction.transaction_type == "Expense":
                balance -= transaction.amount

        return balance

    def get_transactions_as_table(self):
        return [
            transaction.to_list()
            for transaction in self.transactions
        ]

    def load_categories(self, categories):
        self.categories = categories

    def load_transactions(self, transactions_data):
        self.transactions = []

        for transaction_data in transactions_data:
            transaction = Transaction(
                transaction_data["title"],
                transaction_data["amount"],
                transaction_data["category"],
                transaction_data["transaction_type"]
            )

            self.transactions.append(transaction)

    def get_transactions_as_dicts(self):
        return [
            transaction.to_dict()
            for transaction in self.transactions
        ]
