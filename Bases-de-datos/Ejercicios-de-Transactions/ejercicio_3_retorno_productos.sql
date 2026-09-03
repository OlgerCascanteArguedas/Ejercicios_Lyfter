
DO $$
DECLARE
    v_bill_id INTEGER := 1;
    v_status VARCHAR(20);
    v_item RECORD;
BEGIN

    SELECT status
    INTO v_status
    FROM bills
    WHERE bill_id = v_bill_id
    FOR UPDATE;


    IF NOT FOUND THEN
        RAISE EXCEPTION
            'La factura con ID % no existe.',
            v_bill_id;
    END IF;

    IF v_status = 'RETORNADA' THEN
        RAISE EXCEPTION
            'La factura con ID % ya fue retornada anteriormente.',
            v_bill_id;
    END IF;

    IF NOT EXISTS (
        SELECT 1
        FROM bill_products
        WHERE bill_id = v_bill_id
    ) THEN
        RAISE EXCEPTION
            'La factura con ID % no contiene productos.',
            v_bill_id;
    END IF;

    FOR v_item IN
        SELECT
            product_id,
            quantity
        FROM bill_products
        WHERE bill_id = v_bill_id
    LOOP

        UPDATE products
        SET stock = stock + v_item.quantity
        WHERE product_id = v_item.product_id;

    END LOOP;


    UPDATE bills
    SET status = 'RETORNADA'
    WHERE bill_id = v_bill_id;


    RAISE NOTICE
        'La factura con ID % fue retornada correctamente.',
        v_bill_id;

END $$;



SELECT
    bill_id,
    user_id,
    bill_date,
    total,
    status
FROM bills
ORDER BY bill_id;

SELECT
    product_id,
    product_name,
    stock
FROM products
ORDER BY product_id;
