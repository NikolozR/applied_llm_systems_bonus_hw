import sqlite3

def get_connection():
    return sqlite3.connect('company.db')

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


def get_id_by_name(name):
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id FROM employees 
            WHERE LOWER(name) = LOWER(?)
        """, (name,))
        result = cur.fetchone()
        return result
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close() # type: ignore