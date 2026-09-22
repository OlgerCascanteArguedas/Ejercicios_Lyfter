from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

FILE_NAME = "tasks.json"

VALID_STATUSES = [
    "Por Hacer",
    "En Progreso",
    "Completada"
]


def read_tasks():
    """Lee las tareas desde el archivo JSON."""

    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def write_tasks(tasks):
    """Guarda las tareas en el archivo JSON."""

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def validate_task(data):
    """Valida los datos obligatorios de una tarea."""

    if "title" not in data or not str(data["title"]).strip():
        return "El título es obligatorio."

    if "description" not in data or not str(data["description"]).strip():
        return "La descripción es obligatoria."

    if "status" not in data or not str(data["status"]).strip():
        return "El estado es obligatorio."

    if data["status"] not in VALID_STATUSES:
        return (
            "Estado inválido. Los estados permitidos son: "
            "Por Hacer, En Progreso o Completada."
        )

    return None

@app.route("/tasks", methods=["GET"])
def get_tasks():

    # Cada endpoint lee directamente del archivo.
    tasks = read_tasks()

    status = request.args.get("status")

    if status:
        if status not in VALID_STATUSES:
            return jsonify({
                "error": "Estado inválido."
            }), 400

        tasks = [
            task for task in tasks
            if task["status"] == status
        ]

    return jsonify(tasks), 200

@app.route("/tasks", methods=["POST"])
def create_task():

    tasks = read_tasks()

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Debe enviar datos en formato JSON."
        }), 400

    # Validar identificador
    if "id" not in data:
        return jsonify({
            "error": "El identificador es obligatorio."
        }), 400

    # Validar ID duplicado
    for task in tasks:
        if task["id"] == data["id"]:
            return jsonify({
                "error": "Ya existe una tarea con ese identificador."
            }), 409

    # Validar título, descripción y estado
    error = validate_task(data)

    if error:
        return jsonify({
            "error": error
        }), 400

    new_task = {
        "id": data["id"],
        "title": data["title"],
        "description": data["description"],
        "status": data["status"]
    }

    tasks.append(new_task)

    write_tasks(tasks)

    return jsonify({
        "message": "Tarea creada correctamente.",
        "task": new_task
    }), 201

@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):

    tasks = read_tasks()

    data = request.get_json(silent=True)

    if not data:
        return jsonify({
            "error": "Debe enviar datos en formato JSON."
        }), 400

    for task in tasks:

        if task["id"] == task_id:

            error = validate_task(data)

            if error:
                return jsonify({
                    "error": error
                }), 400

            task["title"] = data["title"]
            task["description"] = data["description"]
            task["status"] = data["status"]

            write_tasks(tasks)

            return jsonify({
                "message": "Tarea actualizada correctamente.",
                "task": task
            }), 200

    return jsonify({
        "error": "Tarea no encontrada."
    }), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):

    tasks = read_tasks()

    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            write_tasks(tasks)

            return jsonify({
                "message": "Tarea eliminada correctamente."
            }), 200

    return jsonify({
        "error": "Tarea no encontrada."
    }), 404


if __name__ == "__main__":
    app.run(debug=True)
