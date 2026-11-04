
from flask import Blueprint, request, jsonify

from database import db, fetch_all


rentals_bp = Blueprint("rentals", __name__)

FIELDS = (
    "id",
    "user_id",
    "car_id",
    "rental_date",
    "return_date",
    "status"
)


# LISTAR ALQUILERES
@rentals_bp.get("/rentals")
def list_rentals():
    rentals = fetch_all(
        "rentals",
        FIELDS,
        request.args
    )

    return jsonify(rentals)


# CREAR ALQUILER
@rentals_bp.post("/rentals")
def create_rental():
    data = request.get_json(silent=True) or {}

    user_id = data.get("user_id")
    car_id = data.get("car_id")

    if (
        type(user_id) is not int
        or type(car_id) is not int
    ):
        raise ValueError(
            "user_id y car_id deben ser enteros"
        )

    with db() as conn:
        # Verificar usuario
        user = conn.execute(
            """
            SELECT id, status, is_delinquent
            FROM lyfter_car_rental.users
            WHERE id = %s
            """,
            (user_id,)
        ).fetchone()

        if user is None:
            return jsonify({
                "error": "Usuario no encontrado"
            }), 404

        if user["status"] != "active":
            return jsonify({
                "error": "Usuario inactivo"
            }), 409

        if user["is_delinquent"]:
            return jsonify({
                "error": "Usuario moroso"
            }), 409

        # Reservar automóvil disponible
        car = conn.execute(
            """
            UPDATE lyfter_car_rental.cars
            SET status = 'rented'
            WHERE id = %s
              AND status = 'available'
            RETURNING id
            """,
            (car_id,)
        ).fetchone()

        if car is None:
            return jsonify({
                "error": "Automóvil no disponible"
            }), 409

        # Crear alquiler
        rental = conn.execute(
            """
            INSERT INTO lyfter_car_rental.rentals
                (user_id, car_id, status)
            VALUES (%s, %s, 'active')
            RETURNING *
            """,
            (user_id, car_id)
        ).fetchone()

    return jsonify(rental), 201


# FUNCION PARA COMPLETAR ALQUILER
def finish_rental(rental_id):
    with db() as conn:
        rental = conn.execute(
            """
            UPDATE lyfter_car_rental.rentals
            SET status = 'completed',
                return_date = CURRENT_TIMESTAMP
            WHERE id = %s
              AND status = 'active'
            RETURNING *
            """,
            (rental_id,)
        ).fetchone()

        if rental is None:
            return jsonify({
                "error": "Alquiler activo no encontrado"
            }), 404

        car = conn.execute(
            """
            UPDATE lyfter_car_rental.cars
            SET status = 'available'
            WHERE id = %s
              AND status = 'rented'
            RETURNING id
            """,
            (rental["car_id"],)
        ).fetchone()

        if car is None:
            raise ValueError(
                "Estado inconsistente del automóvil"
            )

    return jsonify(rental)


# COMPLETAR ALQUILER
@rentals_bp.patch("/rentals/<int:rental_id>/complete")
def complete_rental(rental_id):
    return finish_rental(rental_id)


# CAMBIAR ESTADO DEL ALQUILER
@rentals_bp.patch("/rentals/<int:rental_id>/status")
def change_rental_status(rental_id):
    data = request.get_json(silent=True) or {}

    status = data.get("status")

    if status != "completed":
        raise ValueError(
            "Solo se permite cambiar a completed"
        )

    return finish_rental(rental_id)
