# Todo-App Constitution

## Core Principles

### I. In-Memory Storage
**Principle:** The application must store data solely in memory (e.g., Python lists or dictionaries).
**Constraint:** Do not use any external databases, file I/O for storage, or persistence layers for this phase. Data is lost when the app exits.

### II. Console Interface Only
**Principle:** The application is a pure Command Line Interface (CLI).
**Constraint:** Use standard `print()` for output and `input()` for user interaction. Do not use web frameworks (FastAPI/Flask) or GUI libraries.

### III. Python Standard Library
**Principle:** Use pure Python 3.13+.
**Constraint:** Avoid external dependencies unless strictly necessary for the CLI styling (like `rich` or `typer`), but standard library is preferred for "Core Essentials".

### IV. Clean Architecture
**Principle:** Maintain clear separation of concerns even in a simple app.
**Constraint:** Separate the Data Model (Task class) from the Logic (Manager) and the Presentation (Menu/Input loop).