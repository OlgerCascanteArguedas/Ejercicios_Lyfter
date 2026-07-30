PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    price NUMERIC NOT NULL CHECK (price >= 0),
    entry_date TEXT NOT NULL,
    brand TEXT NOT NULL,
    stock_available INTEGER NOT NULL DEFAULT 0
        CHECK (stock_available >= 0)
);

CREATE TABLE IF NOT EXISTS invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number TEXT NOT NULL UNIQUE,
    purchase_date TEXT NOT NULL,
    buyer_email TEXT NOT NULL,
    total_amount NUMERIC NOT NULL
        CHECK (total_amount >= 0)
);

CREATE TABLE IF NOT EXISTS invoice_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL
        CHECK (quantity > 0),
    unit_price NUMERIC NOT NULL
        CHECK (unit_price >= 0),
    total_amount NUMERIC NOT NULL
        CHECK (total_amount >= 0),

    FOREIGN KEY (invoice_id)
        REFERENCES invoices(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE IF NOT EXISTS shopping_carts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_email TEXT NOT NULL,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'ACTIVE'
        CHECK (status IN ('ACTIVE', 'COMPLETED', 'CANCELLED'))
);

CREATE TABLE IF NOT EXISTS shopping_cart_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    shopping_cart_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL
        CHECK (quantity > 0),

    FOREIGN KEY (shopping_cart_id)
        REFERENCES shopping_carts(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    FOREIGN KEY (product_id)
        REFERENCES products(id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,

    UNIQUE (shopping_cart_id, product_id)
);
