INCOME = "Income"
EXPENSE = "Expense"


class Category:
    def __init__(self, name):
        self.name = name.strip()

    def to_dict(self):
        return {
            "name": self.name
        }


class Transaction:
    def __init__(self, title, amount, category, transaction_type):
        self.title = title.strip()
        self.amount = float(amount)
        self.category = category
        self.transaction_type = transaction_type

    def to_list(self):
        return [
            self.title,
            self.amount,
            self.category.name,
            self.transaction_type
        ]

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category.name,
            "transaction_type": self.transaction_type
        }


class FinanceManager:
    def __init__(self):
        self._categories = []
        self._transactions = []

    def add_category(self, name):
        name = name.strip()

        if not name:
            raise ValueError("Category name cannot be empty")

        if self._find_category(name):
            raise ValueError("Category already exists")

        category = Category(name)
        self._categories.append(category)

    def add_transaction(self, title, amount, category_name, transaction_type):
        if not self._categories:
            raise ValueError("Please create a category first")

        if not title.strip():
            raise ValueError("Title cannot be empty")

        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be numeric")

        if amount <= 0:
            raise ValueError("Amount must be greater than zero")

        category = self._find_category(category_name)

        if category is None:
            raise ValueError("Category does not exist")

        if transaction_type not in [INCOME, EXPENSE]:
            raise ValueError("Invalid transaction type")

        transaction = Transaction(
            title,
            amount,
            category,
            transaction_type
        )

        self._transactions.append(transaction)

    def _find_category(self, name):
        for category in self._categories:
            if category.name == name:
                return category

        return None

    def get_categories_names(self):
        return [
            category.name
            for category in self._categories
        ]

    def get_transactions_as_table(self):
        return [
            transaction.to_list()
            for transaction in self._transactions
        ]

    def get_balance(self):
        balance = 0

        for transaction in self._transactions:
            if transaction.transaction_type == INCOME:
                balance += transaction.amount

            elif transaction.transaction_type == EXPENSE:
                balance -= transaction.amount

        return balance

    def get_categories_as_dicts(self):
        return [
            category.to_dict()
            for category in self._categories
        ]

    def get_transactions_as_dicts(self):
        return [
            transaction.to_dict()
            for transaction in self._transactions
        ]

    def load_categories(self, categories_data):
        self._categories = []

        for category_data in categories_data:
            if "name" in category_data:
                category = Category(category_data["name"])
                self._categories.append(category)

    def load_transactions(self, transactions_data):
        self._transactions = []

        for transaction_data in transactions_data:
            required_fields = [
                "title",
                "amount",
                "category",
                "transaction_type"
            ]

            if not all(field in transaction_data for field in required_fields):
                continue

            try:
                self.add_transaction(
                    transaction_data["title"],
                    transaction_data["amount"],
                    transaction_data["category"],
                    transaction_data["transaction_type"]
                )
            except ValueError:
                continue
