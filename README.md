# "No-SQL" Database Agent

A conversational AI agent capable of managing a SQLite database purely through natural language. This tool bridges the gap between unstructured English requests (e.g., "Hire Alice as a Manager") and structured SQL operations.

## Overview

This project implements an AI backend for a hypothetical HR department. Instead of writing SQL queries, a manager can chat with a bot to manage employees. The system uses **Google's Gemini API** to interpret user intents and executes Python functions to modify a local SQLite database (`company.db`).

## Features

- **Natural Language Interface**: Speak to the database in plain English.
- **Data Persistence**: Uses a local SQLite database (`company.db`).
- **Function Calling**: The LLM determines which specific tools to call to ensure safe and structured database modifications.
- **Capabilities**:
    - **Initialization**: Create the employees table automatically.
    - **Insertion**: Add new employee records (Name, Role, Department, Salary).
    - **Deletion**: Remove employees by ID.
    - **Retrieval**: 
        - Find employees by name.
        - Get top K highest-paid employees.

## Prerequisites

- Python 3.9+
- A Google Cloud Project with the Gemini API enabled.
- An API Key for the Gemini API.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   pip install google-genai python-dotenv
   ```

3. **Set up environment variables:**
   Create a `.env` file in the root directory and add your API key:
   ```env
   LLM_HW_API_KEY=your_google_api_key_here
   ```

## Usage

1. **Start the Agent:**
   Run the main script:
   ```bash
   python agent.py
   ```

2. **Interact with the Agent:**
   You will see a prompt where you can enter commands.
   
   **Examples:**
   - "Initialize the database."
   - "Hire John Doe as a Senior Engineer in IT making $120,000."
   - "Who is the highest paid employee?"
   - "Find John Doe."
   - "Fire employee with ID 1."

3. **Exit:**
   Type `exit`, `quit`, `bye`, or `q` to stop the program.

## Project Structure

- `agent.py`: Main entry point. Handles the chat loop and interaction with the Gemini API.
- `tools.py`: Contains the actual Python functions that execute SQL commands against `company.db`.
- `schemas.py`: JSON schemas defining the tools for the LLM.
- `constants.py`: Configuration constants like system prompts and tool mappings.
- `company.db`: The SQLite database file (created after initialization).

## How It Works

1. **Input**: User types a request (e.g., "Add Alice").
2. **Decision**: The LLM analyzes the request and decides which tool (Python function) to call.
3. **Execution**: The system executes the corresponding function in `tools.py` to modify `company.db`.
4. **Feedback**: The function's result is sent back to the LLM.
5. **Response**: The LLM generates a natural language confirmation for the user.

