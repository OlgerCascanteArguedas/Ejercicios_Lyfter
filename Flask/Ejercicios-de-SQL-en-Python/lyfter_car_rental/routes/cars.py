
from flask import Blueprint, request, jsonify

from database import db, fetch_all


cars_bp = Blueprint("cars", __name__)

FIELDS = (
    "id",
    "brand",
    "model",
    "year",
    "status"
)


# LISTAR AUTOMOVILES
@cars_bp.get("/cars")
def list_cars():
    cars = fetch_all(
        "cars",
        FIELDS,
        request.args
    )

    return jsonify(cars)


# CREAR AUTOMOVIL
@cars_bp.post("/cars")
def create_car():
    data = request.get_json(silent=True) or {}

    required = ("brand", "model", "year")

    if any(data.get(field) is None for field in required):
        raise ValueError(
            "Faltan campos obligatorios"
        )

    year = data["year"]

    if type(year) is not int or not 1900 <= year <= 2100:
        raise ValueError("Año inválido")

    with db() as conn:
        car = conn.execute(
            """
            INSERT INTO lyfter_car_rental.cars
                (brand, model, year, status)
            VALUES (%s, %s, %s, 'available')
            RETURNING *
            """,
            (
                data["brand"],
                data["model"],
                year
            )
        ).fetchone()

    return jsonify(car), 201


# CAMBIAR ESTADO DEL AUTOMOVIL
@cars_bp.patch("/cars/<int:car_id>/status")
def change_car_status(car_id):
    data = request.get_json(silent=True) or {}

    status = data.get("status")

    if status not in ("available", "disabled"):
        raise ValueError(
            "Estado debe ser available o disabled"
        )

    with db() as conn:
        car = conn.execute(
            """
            UPDATE lyfter_car_rental.cars
            SET status = %s
            WHERE id = %s
              AND status IN ('available', 'disabled')
            RETURNING *
            """,
            (status, car_id)
        ).fetchone()

        if car is None:
            exists = conn.execute(
                """
                SELECT id
                FROM lyfter_car_rental.cars
                WHERE id = %s
                """,
                (car_id,)
            ).fetchone()

            if exists is None:
                return jsonify({
                    "error": "Automóvil no encontrado"
                }), 404

            return jsonify({
                "error": "No se puede cambiar el estado "
                         "de un automóvil alquilado"
            }), 409

    return jsonify(car)
