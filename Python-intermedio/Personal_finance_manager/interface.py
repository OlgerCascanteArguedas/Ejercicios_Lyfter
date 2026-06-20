import FreeSimpleGUI as sg

from business_logic import FinanceManager, INCOME, EXPENSE
from persistence import (
    CATEGORIES_FILE,
    TRANSACTIONS_FILE,
    save_data,
    load_data
)


def load_initial_data(manager):
    categories = load_data(CATEGORIES_FILE)
    transactions = load_data(TRANSACTIONS_FILE)

    manager.load_categories(categories)
    manager.load_transactions(transactions)


def save_all_data(manager):
    save_data(
        CATEGORIES_FILE,
        manager.get_categories_as_dicts()
    )

    save_data(
        TRANSACTIONS_FILE,
        manager.get_transactions_as_dicts()
    )


def create_main_window(manager):
    headings = [
        "Title",
        "Amount",
        "Category",
        "Type"
    ]

    layout = [
        [
            sg.Text(
                "Personal Finance Manager",
                font=("Arial", 18)
            )
        ],
        [
            sg.Text(
                f"Balance: ${manager.get_balance():.2f}",
                key="-BALANCE-",
                font=("Arial", 14)
            )
        ],
        [
            sg.Table(
                values=manager.get_transactions_as_table(),
                headings=headings,
                key="-TABLE-",
                auto_size_columns=True,
                justification="center",
                num_rows=10
            )
        ],
        [
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income"),
            sg.Button("Exit")
        ]
    ]

    return sg.Window(
        "Personal Finance Manager",
        layout,
        finalize=True
    )


def create_category_window():
    layout = [
        [sg.Text("Category Name")],
        [sg.Input(key="-CATEGORY-")],
        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    return sg.Window(
        "Add Category",
        layout,
        modal=True
    )


def create_transaction_window(title, categories):
    layout = [
        [sg.Text("Title")],
        [sg.Input(key="-TITLE-")],
        [sg.Text("Amount")],
        [sg.Input(key="-AMOUNT-")],
        [sg.Text("Category")],
        [
            sg.Combo(
                categories,
                key="-CATEGORY-",
                readonly=True
            )
        ],
        [
            sg.Button("Save"),
            sg.Button("Cancel")
        ]
    ]

    return sg.Window(
        title,
        layout,
        modal=True
    )


def refresh_main_window(window, manager):
    window["-TABLE-"].update(
        values=manager.get_transactions_as_table()
    )

    window["-BALANCE-"].update(
        f"Balance: ${manager.get_balance():.2f}"
    )


def handle_add_category(manager):
    window = create_category_window()

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

        if event == "Save":
            try:
                category_name = values["-CATEGORY-"]

                manager.add_category(category_name)
                save_all_data(manager)

                sg.popup("Category added successfully")
                break

            except ValueError as error:
                sg.popup_error(str(error))

    window.close()


def handle_add_transaction(manager, transaction_type):
    categories = manager.get_categories_names()

    if not categories:
        sg.popup_error("Please create a category first.")
        return

    window_title = f"Add {transaction_type}"

    window = create_transaction_window(
        window_title,
        categories
    )

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Cancel"):
            break

        if event == "Save":
            try:
                title = values["-TITLE-"]
                amount = values["-AMOUNT-"]
                category = values["-CATEGORY-"]

                manager.add_transaction(
                    title,
                    amount,
                    category,
                    transaction_type
                )

                save_all_data(manager)

                sg.popup(f"{transaction_type} added successfully")
                break

            except ValueError as error:
                sg.popup_error(str(error))

    window.close()


def run_app():
    manager = FinanceManager()
    load_initial_data(manager)

    window = create_main_window(manager)

    while True:
        event, values = window.read()

        if event in (sg.WINDOW_CLOSED, "Exit"):
            save_all_data(manager)
            break

        if event == "Add Category":
            handle_add_category(manager)
            refresh_main_window(window, manager)

        elif event == "Add Expense":
            handle_add_transaction(manager, EXPENSE)
            refresh_main_window(window, manager)

        elif event == "Add Income":
            handle_add_transaction(manager, INCOME)
            refresh_main_window(window, manager)

    window.close()
