
from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash

from database import db, fetch_all


users_bp = Blueprint("users", __name__)

FIELDS = (
    "id",
    "name",
    "email",
    "username",
    "birth_date",
    "status",
    "is_delinquent"
)


def public_user(user):
    if user is None:
        return None

    user = dict(user)
    user.pop("password", None)

    return user


# LISTAR USUARIOS
@users_bp.get("/users")
def list_users():
    users = fetch_all(
        "users",
        FIELDS,
        request.args
    )

    return jsonify([
        public_user(user)
        for user in users
    ])


# CREAR USUARIO
@users_bp.post("/users")
def create_user():
    data = request.get_json(silent=True) or {}

    required = (
        "name",
        "email",
        "username",
        "password",
        "birth_date"
    )

    if any(not data.get(field) for field in required):
        raise ValueError(
            "Faltan campos obligatorios"
        )

    password_hash = generate_password_hash(
        data["password"]
    )

    with db() as conn:
        user = conn.execute(
            """
            INSERT INTO lyfter_car_rental.users
                (name, email, username, password,
                 birth_date, status)
            VALUES (%s, %s, %s, %s, %s, 'active')
            RETURNING *
            """,
            (
                data["name"],
                data["email"],
                data["username"],
                password_hash,
                data["birth_date"]
            )
        ).fetchone()

    return jsonify(public_user(user)), 201


# CAMBIAR ESTADO DEL USUARIO
@users_bp.patch("/users/<int:user_id>/status")
def change_user_status(user_id):
    data = request.get_json(silent=True) or {}

    status = data.get("status")

    if status not in ("active", "inactive"):
        raise ValueError(
            "Estado debe ser active o inactive"
        )

    with db() as conn:
        user = conn.execute(
            """
            UPDATE lyfter_car_rental.users
            SET status = %s
            WHERE id = %s
            RETURNING *
            """,
            (status, user_id)
        ).fetchone()

    if user is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify(public_user(user))


# MARCAR USUARIO COMO MOROSO
@users_bp.patch("/users/<int:user_id>/delinquent")
def flag_delinquent(user_id):
    data = request.get_json(silent=True) or {}

    delinquent = data.get("is_delinquent")

    if not isinstance(delinquent, bool):
        raise ValueError(
            "is_delinquent debe ser true o false"
        )

    with db() as conn:
        user = conn.execute(
            """
            UPDATE lyfter_car_rental.users
            SET is_delinquent = %s
            WHERE id = %s
            RETURNING *
            """,
            (delinquent, user_id)
        ).fetchone()

    if user is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    return jsonify(public_user(user))
