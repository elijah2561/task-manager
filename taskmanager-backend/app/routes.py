from flask import Blueprint, request, jsonify
from app.services import (
    create_task,
    get_all_tasks,
    get_task,
    update_task,
    delete_task,
)

api_bp = Blueprint("api", __name__)

@api_bp.route("/tasks", methods=["POST"])
def create():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    task = create_task(data)
    return jsonify(task.to_dict()), 201

@api_bp.route("/tasks", methods=["GET"])
def list_tasks():
    tasks = get_all_tasks()
    return jsonify([task.to_dict() for task in tasks])

@api_bp.route("/tasks/<int:task_id>", methods=["GET"])
def retrieve(task_id):
    task = get_task(task_id)
    return jsonify(task.to_dict())

@api_bp.route("/tasks/<int:task_id>", methods=["PUT"])
def update(task_id):
    data = request.get_json()
    task = update_task(task_id, data)
    return jsonify(task.to_dict())

@api_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete(task_id):
    delete_task(task_id)
    return jsonify({"message": "Task deleted"}), 204
