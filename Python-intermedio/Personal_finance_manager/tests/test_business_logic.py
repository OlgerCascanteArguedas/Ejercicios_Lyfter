import unittest

from business_logic import FinanceManager


class TestFinanceManager(unittest.TestCase):

    def setUp(self):
        self.manager = FinanceManager()

    def test_add_category(self):
        self.manager.add_category("Food")
        self.assertIn("Food", self.manager.categories)

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
            "Income"
        )

        self.assertEqual(len(self.manager.transactions), 1)

    def test_add_expense(self):
        self.manager.add_category("Food")
        self.manager.add_transaction(
            "Lunch",
            20,
            "Food",
            "Expense"
        )

        self.assertEqual(len(self.manager.transactions), 1)

    def test_transaction_without_categories_raises_error(self):
        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                20,
                "Food",
                "Expense"
            )

    def test_negative_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                -20,
                "Food",
                "Expense"
            )

    def test_zero_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                0,
                "Food",
                "Expense"
            )

    def test_non_numeric_amount_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Lunch",
                "abc",
                "Food",
                "Expense"
            )

    def test_category_does_not_exist_raises_error(self):
        self.manager.add_category("Food")

        with self.assertRaises(ValueError):
            self.manager.add_transaction(
                "Bus",
                5,
                "Transport",
                "Expense"
            )

    def test_balance_calculation(self):
        self.manager.add_category("General")

        self.manager.add_transaction(
            "Salary",
            1000,
            "General",
            "Income"
        )

        self.manager.add_transaction(
            "Food",
            300,
            "General",
            "Expense"
        )

        self.assertEqual(self.manager.get_balance(), 700)

    def test_get_transactions_as_table(self):
        self.manager.add_category("Food")

        self.manager.add_transaction(
            "Lunch",
            20,
            "Food",
            "Expense"
        )

        table = self.manager.get_transactions_as_table()

        self.assertEqual(
            table,
            [["Lunch", 20.0, "Food", "Expense"]]
        )


if __name__ == "__main__":
    unittest.main()
