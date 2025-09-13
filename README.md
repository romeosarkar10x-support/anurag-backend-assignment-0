# **Python + MongoDB Assessment (Django/FastAPI)**

A FastAPI-based backend server with JWT authentication and employee management functionality using MongoDB.

## Assignment PDF

📄 [Assignment Document](https://example.com/assignment-document.pdf) *(URL to be updated)*

## Prerequisites

- Python 3.11
- MongoDB (local or cloud instance)

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
   MONGO_URL=mongodb://localhost:27017/your-database-name
   ```

### 6. Start the Server

```bash
python src/main.py
```

The server will start on `http://localhost:8000`

## API Endpoints

- **POST** `/token` - Authentication endpoint
- **Employees routes** - Available under `/employees` prefix

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