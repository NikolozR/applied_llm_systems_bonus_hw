import sqlite3
from dotenv import load_dotenv
import os
from google import genai
from google.genai import types
from tools import add_employee, delete_employee, get_id_by_name
from schemas import add_employee_tool_schema, delete_employee_tool_schema, get_id_by_name_tool_schema

load_dotenv()

api_key = os.getenv("LLM_HW_API_KEY")

if not api_key:
    raise ValueError("API Key not set")

client = genai.Client(api_key=api_key)

tool_mapping = {
    'add_employee': add_employee,
    'delete_employee': delete_employee,
    'get_id_by_name': get_id_by_name
}

llm_tools = [
    add_employee_tool_schema,
    delete_employee_tool_schema,
    get_id_by_name_tool_schema
]

tools = types.Tool(function_declarations=llm_tools) # type: ignore

config = types.GenerateContentConfig(tools=[tools])

chat = client.chats.create(model="gemini-2.5-flash", config=config)

def execute_agent(raw_query):
    response = chat.send_message(raw_query)
    if response.candidates[0].content.parts[0].function_call: # type: ignore
        function_call = response.candidates[0].content.parts[0].function_call # type: ignore
        try:
            tool_to_call = tool_mapping[function_call.name] # type: ignore
            result = tool_to_call(**function_call.args) # type: ignore
            execute_agent(f"Tool used, result: {result}")
        except Exception as e:
            execute_agent(f"Error During Tool Usage: {e}")
    else:
        print(response.candidates[0].content.parts[0].text) # type: ignore


print("Hello Shota, What Can I do for you?")

while True:
    raw_query = input("=> ")

    if raw_query.lower() in ["exit", "quit", "bye", "q"]:
        print("Goodbye!")
        break

    execute_agent(raw_query)

