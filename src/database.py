from motor.motor_asyncio import AsyncIOMotorClient
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection URL
MONGO_URL = os.getenv("MONGO_URL")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URL)

# Reference to the specific database
db = client.assessment_db

# Reference to the 'employees' collection
employees_collection = db.employees

# -----------------------------
# Index Creation
# -----------------------------

async def create_indexes():
    """
    Creates a unique index on the 'employee_id' field
    to ensure no duplicate employee IDs are inserted.
    """
    await employees_collection.create_index("employee_id", unique=True)

# -----------------------------
# JSON Schema Validator for Employee Documents
# -----------------------------

# Define the expected schema for employee documents
employee_schema = {
    "bsonType": "object",
    "required": ["employee_id", "name", "department", "salary", "joining_date", "skills"],
    "properties": {
        "employee_id": {"bsonType": "string"},          # Unique identifier for the employee
        "name": {"bsonType": "string"},                 # Employee's full name
        "department": {"bsonType": "string"},           # Department name
        "salary": {"bsonType": "double"},               # Salary (must be a floating point number)
        "joining_date": {"bsonType": ["date", "string"]},  # Joining date (date or ISO string)
        "skills": {                                     # List of skills
            "bsonType": "array",
            "items": {"bsonType": "string"}
        }
    }
}

# -----------------------------
# Collection Validator Setup
# -----------------------------

async def ensure_collection_validator():
    """
    Ensures that the 'employees' collection has a JSON schema validator.
    If the collection already exists, attempts to modify it with the schema.
    If it doesn't exist, creates the collection with the schema validator.
    """
    cmd = {
        "collMod": "employees",  # Attempt to modify the existing collection
        "validator": {"$jsonSchema": employee_schema},
        "validationLevel": "moderate"  # Documents must conform to the schema if provided
    }
    try:
        await db.command(cmd)
    except Exception:
        # If the collection doesn't exist, create it with the schema validator
        await db.create_collection("employees", validator={"$jsonSchema": employee_schema})
