
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(120) NOT NULL,
    price NUMERIC(12,2) NOT NULL CHECK (price >= 0),
    stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS bills (
    bill_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    bill_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total NUMERIC(12,2) NOT NULL DEFAULT 0 CHECK (total >= 0),
    status VARCHAR(20) NOT NULL DEFAULT 'ACTIVA'
        CHECK (status IN ('ACTIVA', 'RETORNADA')),

    CONSTRAINT fk_bills_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);


CREATE TABLE IF NOT EXISTS bill_products (
    bill_product_id SERIAL PRIMARY KEY,
    bill_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    unit_price NUMERIC(12,2) NOT NULL CHECK (unit_price >= 0),
    subtotal NUMERIC(12,2) NOT NULL CHECK (subtotal >= 0),

    CONSTRAINT fk_bill_products_bill
        FOREIGN KEY (bill_id)
        REFERENCES bills(bill_id)
        ON DELETE CASCADE,

    CONSTRAINT fk_bill_products_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id),

    CONSTRAINT uq_bill_product UNIQUE (bill_id, product_id)
);


INSERT INTO users (full_name, email)
VALUES
    ('Ana Rodriguez', 'ana@email.com'),
    ('Carlos Sanchez', 'carlos@email.com')
ON CONFLICT (email) DO NOTHING;


INSERT INTO products (product_name, price, stock)
SELECT 'Laptop', 650000.00, 10
WHERE NOT EXISTS (
    SELECT 1 FROM products WHERE product_name = 'Laptop'
);

INSERT INTO products (product_name, price, stock)
SELECT 'Mouse', 15000.00, 50
WHERE NOT EXISTS (
    SELECT 1 FROM products WHERE product_name = 'Mouse'
);

INSERT INTO products (product_name, price, stock)
SELECT 'Teclado', 30000.00, 25
WHERE NOT EXISTS (
    SELECT 1 FROM products WHERE product_name = 'Teclado'
);

INSERT INTO products (product_name, price, stock)
SELECT 'Monitor', 180000.00, 15
WHERE NOT EXISTS (
    SELECT 1 FROM products WHERE product_name = 'Monitor'
);


SELECT * FROM users ORDER BY user_id;
SELECT * FROM products ORDER BY product_id;
