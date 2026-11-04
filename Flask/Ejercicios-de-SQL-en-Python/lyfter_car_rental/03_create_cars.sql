
CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    brand VARCHAR(50) NOT NULL,
    model VARCHAR(50) NOT NULL,
    year INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'available',
    CONSTRAINT chk_car_status
        CHECK (status IN (
            'available',
            'rented',
            'disabled'
        )),
    CONSTRAINT chk_car_year
        CHECK (year BETWEEN 1900 AND 2100)
);

INSERT INTO lyfter_car_rental.cars
    (brand, model, year, status)
SELECT
    (ARRAY[
        'Toyota', 'Honda', 'Hyundai',
        'Nissan', 'Mitsubishi'
    ])[((n - 1) % 5) + 1],
    (ARRAY[
        'Corolla', 'Civic', 'Tucson',
        'Sentra', 'Outlander'
    ])[((n - 1) % 5) + 1],
    2015 + ((n - 1) % 12),
    'available'
FROM generate_series(1, 50) AS n;

SELECT * FROM lyfter_car_rental.cars;
