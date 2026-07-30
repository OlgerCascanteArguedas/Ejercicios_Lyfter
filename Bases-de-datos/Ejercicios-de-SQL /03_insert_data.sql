PRAGMA foreign_keys = ON;
INSERT INTO products (
    code,
    name,
    price,
    entry_date,
    brand,
    stock_available
)
VALUES
    (
        'P001',
        'Laptop Lenovo IdeaPad',
        450000,
        '2026-07-01',
        'Lenovo',
        10
    ),
    (
        'P002',
        'Mouse inalámbrico',
        15000,
        '2026-07-02',
        'Logitech',
        30
    ),
    (
        'P003',
        'Monitor de 24 pulgadas',
        95000,
        '2026-07-03',
        'Samsung',
        15
    ),
    (
        'P004',
        'Teclado mecánico',
        55000,
        '2026-07-04',
        'Redragon',
        20
    ),
    (
        'P005',
        'Memoria USB 64 GB',
        12000,
        '2026-07-05',
        'Kingston',
        50
    );

INSERT INTO invoices (
    invoice_number,
    purchase_date,
    buyer_email,
    total_amount,
    buyer_phone,
    cashier_employee_code
)
VALUES
    (
        'FAC-001',
        '2026-07-20',
        'cliente1@email.com',
        480000,
        '8888-1111',
        'EMP-001'
    ),
    (
        'FAC-002',
        '2026-07-21',
        'cliente2@email.com',
        110000,
        '8888-2222',
        'EMP-002'
    ),
    (
        'FAC-003',
        '2026-07-22',
        'cliente1@email.com',
        134000,
        '8888-1111',
        'EMP-003'
    ),
    (
        'FAC-004',
        '2026-07-23',
        'cliente3@email.com',
        95000,
        '8888-3333',
        'EMP-001'
    );


INSERT INTO invoice_products (
    invoice_id,
    product_id,
    quantity,
    unit_price,
    total_amount
)
VALUES
    -- Factura FAC-001
    (1, 1, 1, 450000, 450000),
    (1, 2, 2, 15000, 30000),

    -- Factura FAC-002
    (2, 4, 2, 55000, 110000),

    -- Factura FAC-003
    (3, 3, 1, 95000, 95000),
    (3, 2, 1, 15000, 15000),
    (3, 5, 2, 12000, 24000),

    -- Factura FAC-004
    (4, 3, 1, 95000, 95000);


INSERT INTO shopping_carts (
    user_email,
    status
)
VALUES
    ('cliente1@email.com', 'ACTIVE'),
    ('cliente2@email.com', 'COMPLETED');

INSERT INTO shopping_cart_products (
    shopping_cart_id,
    product_id,
    quantity
)
VALUES
    (1, 2, 2),
    (1, 5, 1),
    (2, 4, 1);
