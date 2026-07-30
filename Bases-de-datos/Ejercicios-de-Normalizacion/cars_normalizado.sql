
PRAGMA foreign_keys = ON;


DROP TABLE IF EXISTS insurance_policies;
DROP TABLE IF EXISTS insurance_companies;
DROP TABLE IF EXISTS car_ownership;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS cars;

CREATE TABLE cars (
    vin TEXT PRIMARY KEY,
    make TEXT NOT NULL,
    model TEXT NOT NULL,
    manufacture_year INTEGER NOT NULL
        CHECK (manufacture_year BETWEEN 1886 AND 2100),
    color TEXT NOT NULL
);


CREATE TABLE owners (
    owner_id INTEGER PRIMARY KEY,
    owner_name TEXT NOT NULL,
    owner_phone TEXT UNIQUE
);


CREATE TABLE car_ownership (
    car_ownership_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin TEXT NOT NULL,
    owner_id INTEGER NOT NULL,
    FOREIGN KEY (vin)
        REFERENCES cars(vin)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (owner_id)
        REFERENCES owners(owner_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT,
    UNIQUE (vin, owner_id)
);


CREATE TABLE insurance_companies (
    insurance_company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL UNIQUE
);

CREATE TABLE insurance_policies (
    insurance_policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_ownership_id INTEGER NOT NULL,
    insurance_company_id INTEGER NOT NULL,
    coverage_type TEXT NOT NULL,
    FOREIGN KEY (car_ownership_id)
        REFERENCES car_ownership(car_ownership_id)
        ON UPDATE CASCADE
        ON DELETE CASCADE,
    FOREIGN KEY (insurance_company_id)
        REFERENCES insurance_companies(insurance_company_id)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);
