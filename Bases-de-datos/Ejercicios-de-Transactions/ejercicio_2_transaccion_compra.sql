
DO $$

DECLARE
    v_user_id INTEGER := 1;
    v_bill_id INTEGER;
    v_total NUMERIC(12,2) := 0;
    v_item RECORD;

BEGIN


    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE user_id = v_user_id
    ) THEN
        RAISE EXCEPTION 'El usuario con ID % no existe.', v_user_id;
    END IF;

    CREATE TEMP TABLE temp_purchase (
        product_id INTEGER,
        quantity INTEGER
    ) ON COMMIT DROP;

    INSERT INTO temp_purchase (product_id, quantity)
    VALUES
        (1, 1),  -- 1 Laptop
        (2, 2),  -- 2 Mouse
        (3, 1);  -- 1 Teclado

    IF EXISTS (
        SELECT 1
        FROM temp_purchase
        WHERE quantity <= 0
    ) THEN
        RAISE EXCEPTION 'Todas las cantidades deben ser mayores que cero.';
    END IF;

    IF EXISTS (
        SELECT 1
        FROM temp_purchase tp
        LEFT JOIN products p
            ON p.product_id = tp.product_id
        WHERE p.product_id IS NULL
    ) THEN
        RAISE EXCEPTION 'Uno o más productos no existen.';
    END IF;

    PERFORM 1
    FROM products p
    INNER JOIN temp_purchase tp
        ON tp.product_id = p.product_id
    FOR UPDATE;

    FOR v_item IN
        SELECT
            p.product_id,
            p.product_name,
            p.stock,
            tp.quantity
        FROM temp_purchase tp
        INNER JOIN products p
            ON p.product_id = tp.product_id
    LOOP

        IF v_item.stock < v_item.quantity THEN
            RAISE EXCEPTION
                'Stock insuficiente para %. Disponible: %, solicitado: %.',
                v_item.product_name,
                v_item.stock,
                v_item.quantity;
        END IF;

    END LOOP;

    SELECT SUM(p.price * tp.quantity)
    INTO v_total
    FROM temp_purchase tp
    INNER JOIN products p
        ON p.product_id = tp.product_id;


    INSERT INTO bills (
        user_id,
        total,
        status
    )
    VALUES (
        v_user_id,
        v_total,
        'ACTIVA'
    )
    RETURNING bill_id INTO v_bill_id;

    INSERT INTO bill_products (
        bill_id,
        product_id,
        quantity,
        unit_price,
        subtotal
    )
    SELECT
        v_bill_id,
        p.product_id,
        tp.quantity,
        p.price,
        p.price * tp.quantity
    FROM temp_purchase tp
    INNER JOIN products p
        ON p.product_id = tp.product_id;

    UPDATE products p
    SET stock = p.stock - tp.quantity
    FROM temp_purchase tp
    WHERE p.product_id = tp.product_id;


    RAISE NOTICE
        'Compra realizada correctamente. Factura ID: %. Total: %',
        v_bill_id,
        v_total;

END $$;

SELECT * FROM bills ORDER BY bill_id;

SELECT
    bp.bill_id,
    p.product_name,
    bp.quantity,
    bp.unit_price,
    bp.subtotal
FROM bill_products bp
INNER JOIN products p
    ON p.product_id = bp.product_id
ORDER BY bp.bill_id, bp.bill_product_id;

SELECT
    product_id,
    product_name,
    stock
FROM products
ORDER BY product_id;
