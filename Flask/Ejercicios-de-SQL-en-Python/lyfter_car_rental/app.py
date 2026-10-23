
from flask import Flask, jsonify
from dotenv import load_dotenv
from psycopg import errors

from routes.users import users_bp
from routes.cars import cars_bp
from routes.rentals import rentals_bp

load_dotenv()

app = Flask(__name__)

app.register_blueprint(users_bp)
app.register_blueprint(cars_bp)
app.register_blueprint(rentals_bp)


@app.get("/")
def home():
    return jsonify({
        "message": "Lyfter Car Rental API",
        "status": "running"
    })


@app.errorhandler(ValueError)
def bad_request(error):
    return jsonify({
        "error": str(error)
    }), 400


@app.errorhandler(errors.UniqueViolation)
def duplicate_record(error):
    return jsonify({
        "error": "El registro ya existe"
    }), 409


@app.errorhandler(errors.ForeignKeyViolation)
def foreign_key_error(error):
    return jsonify({
        "error": "La referencia no existe"
    }), 400


@app.errorhandler(errors.CheckViolation)
def check_error(error):
    return jsonify({
        "error": "Los datos no cumplen las restricciones"
    }), 400


if __name__ == "__main__":
    app.run(debug=True)
