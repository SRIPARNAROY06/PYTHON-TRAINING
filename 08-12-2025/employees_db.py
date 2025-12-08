from flask import Flask, request, jsonify
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "SriRoy36@",
    "database": "employees_data",
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}

def get_conn():
    return pymysql.connect(**DB_CONFIG)


@app.route("/employees", methods=["GET"])
def get_employees():
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employees")
            rows = cur.fetchall()
        return jsonify(rows), 200
    finally:
        conn.close()



@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM employees WHERE emp_id=%s", (emp_id,))
            row = cur.fetchone()
        return (jsonify(row), 200) if row else (jsonify({"error": "Not found"}), 404)
    finally:
        conn.close()



@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json(silent=True) or {}
    # Required: name. Optional: dept, role, salary, email, phone
    name = data.get("name")
    if not name:
        return jsonify({"error": "Missing fields", "fields": ["name"]}), 400

    dept = data.get("dept")
    role = data.get("role")
    email = data.get("email")
    phone = data.get("phone")

    salary = data.get("salary")
    if salary not in (None, ""):
        try:
            salary = float(salary)
        except (TypeError, ValueError):
            return jsonify({"error": "Invalid salary", "hint": "Provide a numeric value"}), 400
    else:
        salary = None

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO employees (name, dept, role, salary, email, phone)
                VALUES (%s, %s, %s, %s, %s, %s)
                """,
                (name, dept, role, salary, email, phone)
            )
            new_id = cur.lastrowid
        return jsonify({
            "emp_id": new_id,
            "name": name,
            "dept": dept,
            "role": role,
            "salary": salary if salary is not None else 0.00,  # for client convenience
            "email": email,
            "phone": phone
        }), 201
    except pymysql.IntegrityError as e:
        # e.g., duplicate email due to UNIQUE constraint
        return jsonify({"error": "Integrity error", "details": str(e)}), 409
    finally:
        conn.close()


@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json(silent=True) or {}
    allowed = ["name", "dept", "role", "salary", "email", "phone"]

    # Filter only allowed fields
    keys = [k for k in data.keys() if k in allowed]
    if not keys:
        return jsonify({"error": "No valid fields to update", "allowed": allowed}), 400

    # Validate salary if present
    if "salary" in data:
        try:
            data["salary"] = float(data["salary"])
        except (TypeError, ValueError):
            return jsonify({"error": "Invalid salary", "hint": "Provide a numeric value"}), 400

    set_clause = ", ".join([f"{k}=%s" for k in keys])
    values = [data[k] for k in keys]

    conn = get_conn()
    try:
        with conn.cursor() as cur:
            # optional existence check
            cur.execute("SELECT emp_id FROM employees WHERE emp_id=%s", (emp_id,))
            if not cur.fetchone():
                return jsonify({"error": "Not found"}), 404

            cur.execute(f"UPDATE employees SET {set_clause} WHERE emp_id=%s", (*values, emp_id))
        return jsonify({"message": "Updated", "updated_fields": keys}), 200
    except pymysql.IntegrityError as e:
        return jsonify({"error": "Integrity error", "details": str(e)}), 409
    finally:
        conn.close()


@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM employees WHERE emp_id=%s", (emp_id,))
            if cur.rowcount == 0:
                return jsonify({"error": "Not found"}), 404
        return jsonify({"message": "Deleted"}), 200
    finally:
        conn.close()


if __name__ == "__main__":
    app.run(debug=True)

