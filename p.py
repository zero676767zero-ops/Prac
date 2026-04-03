from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample Data
students = {
    1: {"name": "Alice", "marks": 85},
    2: {"name": "Bob", "marks": 90},
    3: {"name": "Charlie", "marks": 78}
}

# Home Route
@app.route("/")
def home():
    return "Student Marks Web Service Running!"

# Get all students
@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)

# Get student by ID
@app.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    if id in students:
        return jsonify(students[id])
    return jsonify({"error": "Student not found"}), 404

# Add student (POST)
@app.route("/students", methods=["POST"])
def add_student():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        sid = int(data.get("id"))
        name = data.get("name")
        marks = int(data.get("marks"))

        if sid in students:
            return jsonify({"error": "Student ID already exists"}), 400

        students[sid] = {"name": name, "marks": marks}

        return jsonify({"message": "Student added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# Add student using GET
@app.route("/addstudents", methods=["GET"])
def add_students_get():
    sid = request.args.get("id", type=int)
    name = request.args.get("name")
    marks = request.args.get("marks", type=int)

    if sid is None or name is None or marks is None:
        return jsonify({"error": "Missing required parameters"}), 400

    if sid in students:
        return jsonify({"error": "Student ID already exists"}), 400

    students[sid] = {"name": name, "marks": marks}

    return jsonify({"message": "Student added successfully!"}), 201


# Run server
if __name__ == "__main__":
    app.run(debug=True)