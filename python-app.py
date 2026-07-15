from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory "database" of tasks — good enough for learning backend basics.
tasks = [
    {"id": 1, "title": "Learn Flask routing", "done": False},
    {"id": 2, "title": "Understand REST APIs", "done": False},
]


@app.route("/")
def home():
    return jsonify(
        {
            "message": "Welcome to your first backend project!",
            "try": ["GET /api/tasks", "POST /api/tasks", "GET /api/tasks/<id>"],
        }
    )


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    task = next((t for t in tasks if t["id"] == task_id), None)
    if task is None:
        return jsonify({"error": "Task not found"}), 404
    return jsonify(task)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return jsonify({"error": "title is required"}), 400

    new_task = {
        "id": (max((t["id"] for t in tasks), default=0) + 1),
        "title": title,
        "done": False,
    }
    tasks.append(new_task)
    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
