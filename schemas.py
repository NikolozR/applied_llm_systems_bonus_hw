init_employee_table_tool_schema = {
    "name": "init_employee_table",
    "description": "Inits employee table with autoincrement ID column, name, role, department and salary, non of the columns can be NULL",
}


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


get_employee_by_name_tool_schema = {
    "name": "get_employee_by_name",
    "description": "Retrieves employee data by searching name, may return several rows if several employees have the same name",
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

get_top_k_employees_salary_tool_schema = {
    "name": "get_top_k_employees_salary",
    "description": "Retrieves top K employees by salary",
    "parameters": {
        "type": "object",
        "properties": {
            "k": {
                "type": "number",
                "description": "How many top employees is needed to be retrieved",
            },
        },
        "required": ["k"],
    },
}

get_employees_by_role_tool_schema = {
    "name": "get_employees_by_role",
    "description": "Retrieves employees by their role",
    "parameters": {
        "type": "object",
        "properties": {
            "role": {
                "type": "string",
                "description": "The role to search for (e.g. 'Manager', 'Engineer')",
            },
        },
        "required": ["role"],
    },
}

get_employees_by_department_tool_schema = {
    "name": "get_employees_by_department",
    "description": "Retrieves employees by their department",
    "parameters": {
        "type": "object",
        "properties": {
            "department": {
                "type": "string",
                "description": "The department to search for (e.g. 'HR', 'IT')",
            },
        },
        "required": ["department"],
    },
}

get_all_roles_tool_schema = {
    "name": "get_all_roles",
    "description": "Retrieves a list of all unique roles in the company",
}

get_all_departments_tool_schema = {
    "name": "get_all_departments",
    "description": "Retrieves a list of all unique departments in the company",
}
