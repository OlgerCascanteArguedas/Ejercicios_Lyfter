
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS order_details;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_name TEXT NOT NULL,
    customer_phone TEXT NOT NULL UNIQUE
);

CREATE TABLE items (
    item_id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    current_price NUMERIC NOT NULL CHECK (current_price >= 0)
);

CREATE TABLE orders (
    order_id TEXT PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    delivery_address TEXT NOT NULL,
    delivery_time TEXT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

CREATE TABLE order_details (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id TEXT NOT NULL,
    item_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC NOT NULL CHECK (unit_price >= 0),
    special_request TEXT,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (item_id)
        REFERENCES items(item_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
