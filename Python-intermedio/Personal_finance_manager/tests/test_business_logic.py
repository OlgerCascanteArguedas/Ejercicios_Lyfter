import unittest

from business_logic import FinanceManager, INCOME, EXPENSE


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()

    def test_add_category(self):
        self.manager.add_category("Food")

        self.assertIn(
            "Food",
            self.manager.get_categories_names()
        )

    def test_empty_category_name_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_category("")

    def test_duplicate_category_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_category("Food")

    def test_add_income(self):
        self.manager.add_category("Salary")

        self.manager.add_transaction(
            "Monthly salary",
            1000,
            "Salary",
            INCOME
        )

        self.assertEqual(
            len(self.manager.get_transactions_as_table()),
            1
        )

    def test_add_expense(self):
        self.manager.add_category("Food")

        self.manager.add_transaction(
            "Lunch",
            20,
            "Food",
            EXPENSE
        )

        self.assertEqual(
            len(self.manager.get_transactions_as_table()),
            1
        )

    def test_transaction_without_categories_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                20,
                "Food",
                EXPENSE
            )

    def test_negative_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                -20,
                "Food",
                EXPENSE
            )

    def test_zero_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                0,
                "Food",
                EXPENSE
            )

    def test_non_numeric_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                "abc",
                "Food",
                EXPENSE
            )

    def test_category_does_not_exist_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Bus",
                5,
                "Transport",
                EXPENSE
            )

    def test_invalid_transaction_type_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                20,
                "Food",
                "Invalid"
            )

    def test_balance_calculation(self):
        self.manager.add_category("General")

        self.manager.add_transaction(
            "Salary",
            1000,
            "General",
            INCOME
        )

        self.manager.add_transaction(
            "Food",
            300,
            "General",
            EXPENSE
        )

        self.assertEqual(
            self.manager.get_balance(),
            700
        )

    def test_get_transactions_as_table(self):
        self.manager.add_category("Food")

        self.manager.add_transaction(
            "Lunch",
            20,
            "Food",
            EXPENSE
        )

        table = self.manager.get_transactions_as_table()

        self.assertEqual(
            table,
            [["Lunch", 20.0, "Food", "Expense"]]
        )

    def test_get_categories_as_dicts(self):
        self.manager.add_category("Food")

        self.assertEqual(
            self.manager.get_categories_as_dicts(),
            [{"name": "Food"}]
        )

    def test_load_categories(self):
        data = [
            {"name": "Food"},
            {"name": "Transport"}
        ]

        self.manager.load_categories(data)

        self.assertEqual(
            self.manager.get_categories_names(),
            ["Food", "Transport"]
        )

    def test_load_transactions(self):
        categories_data = [
            {"name": "Food"}
        ]

        transactions_data = [
            {
                "title": "Lunch",
                "amount": 20,
                "category": "Food",
                "transaction_type": EXPENSE
            }
        ]

        self.manager.load_categories(categories_data)
        self.manager.load_transactions(transactions_data)

        self.assertEqual(
            self.manager.get_transactions_as_table(),
            [["Lunch", 20.0, "Food", "Expense"]]
        )


if __name__ == "__main__":
    unittest.main()
