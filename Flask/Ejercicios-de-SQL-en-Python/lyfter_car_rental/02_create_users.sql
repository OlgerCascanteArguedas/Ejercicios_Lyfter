
CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    birth_date DATE NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    CONSTRAINT chk_user_status
        CHECK (status IN ('active', 'inactive'))
);

INSERT INTO lyfter_car_rental.users
    (name, email, username, password, birth_date, status)
SELECT
    'User ' || n,
    'user' || n || '@example.com',
    'user' || n,
    'test_hash_' || n,
    DATE '1980-01-01' + (n * 100),
    'active'
FROM generate_series(1, 50) AS n
ON CONFLICT (username) DO NOTHING;

SELECT * FROM lyfter_car_rental.users;
