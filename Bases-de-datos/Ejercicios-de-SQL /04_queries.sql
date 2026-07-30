SELECT *
FROM products;

SELECT
    id,
    code,
    name,
    price,
    brand,
    stock_available
FROM products
WHERE price > 50000;

SELECT
    ip.id AS invoice_product_id,
    p.id AS product_id,
    p.name AS product_name,
    i.invoice_number,
    i.purchase_date,
    i.buyer_email,
    ip.quantity,
    ip.unit_price,
    ip.total_amount
FROM invoice_products AS ip
INNER JOIN products AS p
    ON p.id = ip.product_id
INNER JOIN invoices AS i
    ON i.id = ip.invoice_id
WHERE p.id = 3;

SELECT
    p.id AS product_id,
    p.code AS product_code,
    p.name AS product_name,
    SUM(ip.quantity) AS total_units_purchased,
    SUM(ip.total_amount) AS total_purchased_amount
FROM invoice_products AS ip
INNER JOIN products AS p
    ON p.id = ip.product_id
GROUP BY
    p.id,
    p.code,
    p.name
ORDER BY total_units_purchased DESC;

SELECT
    id,
    invoice_number,
    purchase_date,
    buyer_email,
    buyer_phone,
    cashier_employee_code,
    total_amount
FROM invoices
WHERE buyer_email = 'cliente1@email.com'
ORDER BY purchase_date ASC;

SELECT
    id,
    invoice_number,
    purchase_date,
    buyer_email,
    total_amount
FROM invoices
ORDER BY total_amount DESC;

SELECT
    id,
    invoice_number,
    purchase_date,
    buyer_email,
    buyer_phone,
    cashier_employee_code,
    total_amount
FROM invoices
WHERE invoice_number = 'FAC-001';

SELECT
    i.invoice_number,
    i.purchase_date,
    i.buyer_email,
    i.buyer_phone,
    i.cashier_employee_code,
    p.code AS product_code,
    p.name AS product_name,
    ip.quantity,
    ip.unit_price,
    ip.total_amount AS line_total,
    i.total_amount AS invoice_total
FROM invoices AS i
INNER JOIN invoice_products AS ip
    ON ip.invoice_id = i.id
INNER JOIN products AS p
    ON p.id = ip.product_id
WHERE i.invoice_number = 'FAC-001';


