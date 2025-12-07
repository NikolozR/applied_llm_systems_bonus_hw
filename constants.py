from tools import add_employee, delete_employee, get_id_by_name
from schemas import add_employee_tool_schema, delete_employee_tool_schema, get_id_by_name_tool_schema



# This is tool mapping, so when LLM returns function name we can easily call it
TOOL_MAPPING = {
    'add_employee': add_employee,
    'delete_employee': delete_employee,
    'get_id_by_name': get_id_by_name
}

# Just list of tool schemas that LLM can use
LLM_TOOLS = [
    add_employee_tool_schema,
    delete_employee_tool_schema,
    get_id_by_name_tool_schema
]