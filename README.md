# **Python + MongoDB Assessment (Django/FastAPI)**

A FastAPI-based backend server implementing a comprehensive employee management system with CRUD operations, querying, aggregation, and JWT authentication using MongoDB.

## Assignment PDF

📄 [Assignment Document (View)](https://drive.google.com/viewerng/viewer?embedded=true&url=https://raw.githubusercontent.com/romeosarkar10x-support/anurag-backend-assignment-0/main/assets/task.pdf) | [Download PDF](https://raw.githubusercontent.com/romeosarkar10x-support/anurag-backend-assignment-0/main/assets/task.pdf)

## Prerequisites

- Python 3.11
- MongoDB (local instance)
- Database name: `assessment_db`
- Collection name: `employees`

## Setup Instructions

### 1. Clone and Navigate to Project

```bash
cd backend
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/macOS:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Setup Environment Variables

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` file and add your configuration:
   ```
   SECRET_KEY=your-secret-key-here
   MONGO_URL=mongodb://localhost:27017/assessment_db
   ```

### 6. Start the Server

```bash
python src/main.py
```

The server will start on `http://localhost:8000`

## API Endpoints

### Authentication
- **POST** `/token` - JWT authentication endpoint

### Employee Management
- **POST** `/employees` - Create a new employee
- **GET** `/employees/{employee_id}` - Get employee by ID
- **PUT** `/employees/{employee_id}` - Update employee (partial updates supported)
- **DELETE** `/employees/{employee_id}` - Delete employee
- **GET** `/employees?department=Engineering` - List employees by department (sorted by joining_date)
- **GET** `/employees/avg-salary` - Get average salary by department (aggregation)
- **GET** `/employees/search?skill=Python` - Search employees by skill

### Sample Employee Document Structure
```json
{
  "employee_id": "E123",
  "name": "John Doe", 
  "department": "Engineering",
  "salary": 75000,
  "joining_date": "2023-01-15",
  "skills": ["Python", "MongoDB", "APIs"]
}
```

## Development

The server runs with auto-reload enabled. Make changes to the code and the server will automatically restart.

## Project Structure

```
backend/
├── src/
│   ├── main.py          # Main application entry point
│   ├── auth.py          # Authentication logic
│   ├── crud.py          # Database operations
│   ├── database.py      # Database configuration
│   ├── models.py        # Data models
│   └── routes/
│       └── employees.py # Employee routes
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
└── README.md           # This file
```