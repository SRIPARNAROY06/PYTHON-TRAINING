
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "SriRoy36@",
    "database": "company_db",
    "cursorclass": pymysql.cursors.DictCursor,
    "autocommit": True,
}

def run_query(sql):
    conn = pymysql.connect(**DB_CONFIG)
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
            return cur.fetchall()
    finally:
        conn.close()

# INNER JOIN (departments that have a valid head employee)
@app.get("/inner join")
def inner_join():
    sql = """
    SELECT d.dept_id, d.dept_name, d.location,
           e.id AS head_id, e.name AS head_name, e.role AS head_role, e.salary AS head_salary
    FROM departments d
    INNER JOIN employees e ON d.head_emp_id = e.id
    ORDER BY d.dept_id;
    """
    return jsonify(run_query(sql)), 200

# LEFT JOIN (all departments; head may be NULL)
@app.get("/left join")
def left_join():
    sql = """
    SELECT d.dept_id, d.dept_name, d.location,
           e.id AS head_id, e.name AS head_name, e.role AS head_role
    FROM departments d
    LEFT JOIN employees e ON d.head_emp_id = e.id
    ORDER BY d.dept_id;
    """
    return jsonify(run_query(sql)), 200

# RIGHT JOIN (all employees; show department they head if any)
@app.get("/right join")
def right_join():
    sql = """
    SELECT d.dept_id, d.dept_name, d.location,
           e.id AS emp_id, e.name AS emp_name, e.role AS emp_role
    FROM departments d
    RIGHT JOIN employees e ON d.head_emp_id = e.id
    ORDER BY e.id;
    """
    return jsonify(run_query(sql)), 200

if __name__ == "__main__":
    app.run(debug=True)
