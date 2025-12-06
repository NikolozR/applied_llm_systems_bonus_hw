
add_employee_tool_schema = {
    "name": "add_employee",
    "description": "Adds new employee in employee table with given data (name, role, department, salary)",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Name of the employee.",
            },
            "role": {
                "type": "string",
                "description": "Role of employee in company",
            },
            "department": {
                "type": "string",
                "description": "Department where the employee works.",
            },
            "salary": {
                "type": "number",
                "description": "Employee's monthly salary.",
            },
        },
        "required": ["name", "role", "department", "salary"],
    },
}


delete_employee_tool_schema = {
    "name": "delete_employee",
    "description": "Deletes employee from employees table based on given id",
    "parameters": {
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "ID of the employee.",
            },
        },
        "required": ["id"],
    },
}


get_id_by_name_tool_schema = {
    "name": "get_id_by_name",
    "description": "Retrieves employee ID by searching name, may return several ids if several employees have the same name",
    "parameters": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "Name of the employee.",
            },
        },
        "required": ["name"],
    },
}