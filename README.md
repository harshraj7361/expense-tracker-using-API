# Expense Tracker API

A simple REST API built with **FastAPI**, **Pydantic**, and **JSON** for managing personal expenses.

## 🚀 Features

- Create a new expense
- Get all expenses
- Get a single expense by ID
- Update an existing expense
- Delete an expense
- Search expenses by title
- Get expense summary:
  - Total expense
  - Average expense
  - Highest expense
  - Lowest expense
- Input validation using Pydantic
- Proper error handling using HTTPException
- Interactive API testing with Swagger UI

## 🛠️ Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- JSON
- Git & GitHub

## 📁 Project Structure

```text
Expense-Tracker/
│
├── main.py
├── expenses.json
├── README.md
├── .gitignore
└── myenv2/
```

> `myenv2/` is the local virtual environment and should not be uploaded to GitHub.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Expense-Tracker
```

### 2. Create a virtual environment

```bash
python -m venv myenv2
```

### 3. Activate the virtual environment

PowerShell:

```powershell
.\myenv2\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
pip install fastapi uvicorn pydantic
```

### 5. Make sure `expenses.json` exists

Start it with an empty JSON object:

```json
{}
```

## ▶️ Run the API

```bash
python -m uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## 📖 Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to test the API directly from your browser.

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check whether the API is running |
| POST | `/create` | Create a new expense |
| GET | `/expenses` | Get all expenses |
| GET | `/expenses/search?title=movie` | Search expenses by title |
| GET | `/expenses/summary` | Get expense summary |
| GET | `/expenses/{id}` | Get expense by ID |
| PUT | `/expenses/{id}` | Update an expense |
| DELETE | `/expenses/{id}` | Delete an expense |

> Static routes such as `/expenses/search` and `/expenses/summary` should be declared before `/expenses/{id}`.

## 🧾 Example Expense

```json
{
    "title": "Groceries",
    "amount": 850,
    "date": "2026-09-25",
    "payment_method": "UPI",
    "description": "Monthly grocery shopping"
}
```

### Allowed Payment Methods

```text
Cash
UPI
Card
Net Banking
```

## 📊 Example Summary Response

```json
{
    "total": 2919,
    "average": 583.8,
    "highest": 999,
    "lowest": 120
}
```

If there are no expenses, the summary endpoint returns:

```json
{
    "detail": "No expenses found"
}
```

with HTTP status code `404`.

## 🧠 Concepts Practiced

This project helped practice:

- FastAPI application and routing
- HTTP methods: GET, POST, PUT, DELETE
- Pydantic models and validation
- `Field()` and `Literal`
- Path parameters
- Query parameters
- JSON file handling
- CRUD operations
- `model_dump()`
- `HTTPException`
- Error handling
- Search and filtering logic
- Basic data calculations
- Swagger API documentation
- Git and GitHub workflow

## 🔄 Project Flow

```text
Client
  ↓
FastAPI Route
  ↓
Pydantic Validation
  ↓
Load JSON Data
  ↓
Create / Read / Update / Delete
  ↓
Save JSON Data
  ↓
API Response
```

## 🔮 Future Improvements

Possible future upgrades:

- Replace JSON storage with SQLite/PostgreSQL
- Add user authentication
- Add expense categories
- Add date-based filtering
- Add monthly expense reports
- Add frontend using Streamlit or React

## 👨‍💻 Author

**Harsh Raj**

Built as a learning project to practice FastAPI, Pydantic, API development, and backend fundamentals.
