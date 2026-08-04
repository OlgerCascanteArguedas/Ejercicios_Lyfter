PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS car_policy;
DROP TABLE IF EXISTS policy_types;
DROP TABLE IF EXISTS insurance_companies;
DROP TABLE IF EXISTS car_ownership;
DROP TABLE IF EXISTS owners;
DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS vehicle_models;
DROP TABLE IF EXISTS manufacturers;

CREATE TABLE manufacturers (
    manufacturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_name TEXT NOT NULL UNIQUE
);

CREATE TABLE vehicle_models (
    vehicle_model_id INTEGER PRIMARY KEY AUTOINCREMENT,
    manufacturer_id INTEGER NOT NULL,
    model_name TEXT NOT NULL,
    manufacture_year INTEGER NOT NULL CHECK (manufacture_year BETWEEN 1886 AND 2100),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(manufacturer_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    UNIQUE (manufacturer_id, model_name, manufacture_year)
);

CREATE TABLE cars (
    vin TEXT PRIMARY KEY,
    vehicle_model_id INTEGER NOT NULL,
    color TEXT NOT NULL,
    FOREIGN KEY (vehicle_model_id) REFERENCES vehicle_models(vehicle_model_id)
        ON UPDATE CASCADE ON DELETE RESTRICT
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
    FOREIGN KEY (vin) REFERENCES cars(vin)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES owners(owner_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    UNIQUE (vin, owner_id)
);

CREATE TABLE insurance_companies (
    insurance_company_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL UNIQUE
);

CREATE TABLE policy_types (
    policy_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
    policy_name TEXT NOT NULL UNIQUE
);

CREATE TABLE car_policy (
    car_policy_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vin TEXT NOT NULL,
    policy_type_id INTEGER NOT NULL,
    insurance_company_id INTEGER NOT NULL,
    FOREIGN KEY (vin) REFERENCES cars(vin)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (policy_type_id) REFERENCES policy_types(policy_type_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (insurance_company_id) REFERENCES insurance_companies(insurance_company_id)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    UNIQUE (vin, policy_type_id, insurance_company_id)
);
