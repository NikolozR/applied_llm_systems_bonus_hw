from tools import add_employee, delete_employee, get_employee_by_name, get_top_k_employees_salary, init_employee_table
from schemas import add_employee_tool_schema, delete_employee_tool_schema, get_employee_by_name_tool_schema, get_top_k_employees_salary_tool_schema, init_employee_table_tool_schema



# This is tool mapping, so when LLM returns function name we can easily call it
TOOL_MAPPING = {
    'add_employee': add_employee,
    'delete_employee': delete_employee,
    'get_employee_by_name': get_employee_by_name,
    'get_top_k_employees_salary': get_top_k_employees_salary,
    'init_employee_table': init_employee_table
}

# Just list of tool schemas that LLM can use
LLM_TOOLS = [
    add_employee_tool_schema,
    delete_employee_tool_schema,
    get_employee_by_name_tool_schema,
    get_top_k_employees_salary_tool_schema,
    init_employee_table_tool_schema
]

SYSTEM_PROMPT = """
You are assistant for a company's manager.
Currency in this company is USD. 
Please use $ sign and number formatting when necessary."""