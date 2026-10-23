
CREATE TABLE IF NOT EXISTS lyfter_car_rental.rentals (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    user_id INTEGER NOT NULL,
    car_id INTEGER NOT NULL,
    rental_date TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP,
    return_date TIMESTAMP,
    status VARCHAR(20) NOT NULL
        DEFAULT 'active',

    CONSTRAINT fk_rental_user
        FOREIGN KEY (user_id)
        REFERENCES lyfter_car_rental.users(id),

    CONSTRAINT fk_rental_car
        FOREIGN KEY (car_id)
        REFERENCES lyfter_car_rental.cars(id),

    CONSTRAINT chk_rental_status
        CHECK (status IN ('active', 'completed')),

    CONSTRAINT chk_return_date
        CHECK (
            return_date IS NULL
            OR return_date >= rental_date
        )
);

CREATE UNIQUE INDEX IF NOT EXISTS
    idx_one_active_rental_per_car
ON lyfter_car_rental.rentals(car_id)
WHERE status = 'active';
