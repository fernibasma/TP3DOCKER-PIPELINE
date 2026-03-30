from flask import Flask, request, jsonify
from app.tasks import get_tasks, add_task, delete_task

app = Flask(__name__)

@app.route("/tasks", methods=["GET"])
def list_tasks():
    return jsonify(get_tasks())

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    task = data.get("task")

    add_task(task)   # ✅ CORRECTION

    return jsonify({"task": task}), 201  # ✅ CORRECTION

@app.route("/tasks", methods=["DELETE"])
def remove_task():
    data = request.json
    task = data.get("task")

    delete_task(task)

    return jsonify({"message": "deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)