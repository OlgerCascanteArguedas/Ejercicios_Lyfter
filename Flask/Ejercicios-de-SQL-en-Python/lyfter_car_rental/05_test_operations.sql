
-- ==========================================
-- LYFTER CAR RENTAL
-- TAREA 2: PRUEBAS BASICAS DE LA DB
-- ==========================================

SET search_path TO lyfter_car_rental;

-- ==========================================
-- TEST 1: AGREGAR UN USUARIO NUEVO
-- ==========================================

INSERT INTO users
    (name, email, username, password, birth_date, status)
VALUES
    ('Carlos Mora', 'carlos@example.com',
     'carlosm', 'test_hash_carlos',
     '1995-05-15', 'active');


-- ==========================================
-- TEST 2: AGREGAR UN AUTOMOVIL NUEVO
-- ==========================================

INSERT INTO cars
    (brand, model, year, status)
VALUES
    ('Toyota', 'RAV4', 2025, 'available');


-- ==========================================
-- TEST 3: CAMBIAR EL ESTADO DE UN USUARIO
-- ==========================================

UPDATE users
SET status = 'inactive'
WHERE username = 'carlosm';


-- ==========================================
-- TEST 4: CAMBIAR EL ESTADO DE UN AUTOMOVIL
-- ==========================================

UPDATE cars
SET status = 'disabled'
WHERE id = 10
  AND status = 'available';


-- ==========================================
-- TEST 5: GENERAR UN ALQUILER NUEVO
-- ==========================================

BEGIN;

DO $$
DECLARE
    v_user_id INTEGER := 1;
    v_car_id INTEGER := 1;
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM users
        WHERE id = v_user_id
          AND status = 'active'
    ) THEN
        RAISE EXCEPTION 'Usuario no disponible';
    END IF;

    UPDATE cars
    SET status = 'rented'
    WHERE id = v_car_id
      AND status = 'available';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Automovil no disponible';
    END IF;

    INSERT INTO rentals
        (user_id, car_id, status)
    VALUES
        (v_user_id, v_car_id, 'active');
END $$;

COMMIT;


-- ==========================================
-- TEST 6: CONFIRMAR DEVOLUCION DEL AUTO
-- ==========================================

BEGIN;

DO $$
DECLARE
    v_rental_id INTEGER;
    v_car_id INTEGER;
BEGIN
    SELECT id, car_id
    INTO v_rental_id, v_car_id
    FROM rentals
    WHERE user_id = 1
      AND car_id = 1
      AND status = 'active'
    ORDER BY rental_date DESC
    LIMIT 1
    FOR UPDATE;

    IF v_rental_id IS NULL THEN
        RAISE EXCEPTION 'Alquiler activo no encontrado';
    END IF;

    UPDATE rentals
    SET status = 'completed',
        return_date = CURRENT_TIMESTAMP
    WHERE id = v_rental_id;

    UPDATE cars
    SET status = 'available'
    WHERE id = v_car_id
      AND status = 'rented';

    IF NOT FOUND THEN
        RAISE EXCEPTION 'Estado del automovil inconsistente';
    END IF;
END $$;

COMMIT;


-- ==========================================
-- TEST 7: DESHABILITAR UN AUTOMOVIL
-- ==========================================

UPDATE cars
SET status = 'disabled'
WHERE id = 5
  AND status = 'available';


-- ==========================================
-- TEST 8: OBTENER AUTOMOVILES ALQUILADOS
-- ==========================================

SELECT *
FROM cars
WHERE status = 'rented';


-- ==========================================
-- TEST 9: OBTENER AUTOMOVILES DISPONIBLES
-- ==========================================

SELECT *
FROM cars
WHERE status = 'available';


-- ==========================================
-- CONSULTAS ADICIONALES DE VERIFICACION
-- ==========================================

-- Ver todos los usuarios
SELECT * FROM users;

-- Ver todos los automoviles
SELECT * FROM cars;

-- Ver todos los alquileres
SELECT * FROM rentals;

-- Ver historial de alquileres con JOIN
SELECT
    r.id AS rental_id,
    u.name AS customer,
    c.brand,
    c.model,
    r.rental_date,
    r.return_date,
    r.status
FROM rentals AS r
INNER JOIN users AS u
    ON r.user_id = u.id
INNER JOIN cars AS c
    ON r.car_id = c.id
ORDER BY r.rental_date DESC;

