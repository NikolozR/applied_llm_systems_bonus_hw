import sqlite3

def get_connection():
    return sqlite3.connect('company.db')

def init_employee_table():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                role TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL
            )
        """)
        conn.commit()
        return "Database initialized."
    except Exception as e:
        return f"Error initializing DB: {e}"
    finally:
        conn.close() # type: ignore

def add_employee(name, role, department, salary):
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO employees (name, role, department, salary)
            VALUES (?, ?, ?, ?)
        """, (name, role, department, salary))
        conn.commit()
        last_id = cur.lastrowid
        return f"Success: Row ID {last_id} created"
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore


def delete_employee(id):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM employees WHERE id = ?", (id,))

        conn.commit()
        return f"Success: Row ID {id} created"
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore


def get_employee_by_name(name):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM employees 
            WHERE LOWER(name) = LOWER(?)
        """, (name,))
        result = cur.fetchall()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore

def get_top_k_employees_salary(k):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM employees 
            ORDER BY salary DESC LIMIT ?
        """, (k,))
    
        result = cur.fetchall()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore

def get_employees_by_role(role):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM employees 
            WHERE LOWER(role) = LOWER(?)
        """, (role,))
        result = cur.fetchall()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore

def get_employees_by_department(department):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT * FROM employees 
            WHERE LOWER(department) = LOWER(?)
        """, (department,))
        result = cur.fetchall()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore

def get_all_roles():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT DISTINCT role FROM employees
        """)
        result = [row[0] for row in cur.fetchall()]
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore

def get_all_departments():
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT DISTINCT department FROM employees
        """)
        result = [row[0] for row in cur.fetchall()]
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore
