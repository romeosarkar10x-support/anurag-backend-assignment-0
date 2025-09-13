from bson import ObjectId
from database import employees_collection
from models import Employee, UpdateEmployee
from fastapi import HTTPException
from datetime import datetime, date  

# -----------------------------
# Helper Function
# -----------------------------

def employee_helper(employee) -> dict:
    """
    Converts a MongoDB employee document into a JSON-serializable dictionary.
    Handles datetime conversion for the 'joining_date' field.
    """
    return {
        "employee_id": employee["employee_id"],
        "name": employee["name"],
        "department": employee["department"],
        "salary": employee["salary"],
        "joining_date": employee["joining_date"].date() if isinstance(employee["joining_date"], datetime) else str(employee["joining_date"]),
        "skills": employee["skills"],
    }

# -----------------------------
# 1. Create New Employee
# -----------------------------

async def create_employee(employee: Employee):
    """
    Inserts a new employee into the database.
    Validates that the employee_id is unique.
    """
    existing = await employees_collection.find_one({"employee_id": employee.employee_id})
    if existing:
        raise HTTPException(status_code=400, detail="Employee ID already exists")

    new_employee = employee.model_dump()

    # Convert date to datetime for MongoDB
    if isinstance(new_employee["joining_date"], date):
        new_employee["joining_date"] = datetime.combine(new_employee["joining_date"], datetime.min.time())

    await employees_collection.insert_one(new_employee)
    created = await employees_collection.find_one({"employee_id": employee.employee_id})
    return employee_helper(created)

# -----------------------------
# 2. Retrieve Employee by ID
# -----------------------------

async def get_employee(employee_id: str):
    """
    Retrieves an employee document based on the provided employee_id.
    """
    employee = await employees_collection.find_one({"employee_id": employee_id})
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_helper(employee)

# -----------------------------
# 3. Update Existing Employee
# -----------------------------

async def update_employee(employee_id: str, updates: UpdateEmployee):
    """
    Updates fields for an existing employee.
    Only updates fields that are provided (non-null).
    """
    update_data = {k: v for k, v in updates.model_dump().items() if v is not None}

    # Convert joining_date to datetime if present
    if "joining_date" in update_data and isinstance(update_data["joining_date"], date):
        update_data["joining_date"] = datetime.combine(update_data["joining_date"], datetime.min.time())

    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    result = await employees_collection.update_one(
        {"employee_id": employee_id}, {"$set": update_data}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")

    updated_employee = await employees_collection.find_one({"employee_id": employee_id})
    return employee_helper(updated_employee)

# -----------------------------
# 4. Delete Employee
# -----------------------------

async def delete_employee(employee_id: str):
    """
    Deletes an employee based on the provided employee_id.
    """
    result = await employees_collection.delete_one({"employee_id": employee_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}

# -----------------------------
# 5. List All Employees
# -----------------------------

async def list_employees():
    """
    Returns a list of all employees in the database.
    """
    employees_cursor = employees_collection.find()
    employees = []
    async for emp in employees_cursor:
        employees.append(employee_helper(emp))
    return employees

# -----------------------------
# 6. List Employees by Department
# -----------------------------

async def list_employees_by_department(department: str):
    """
    Returns employees from a specific department,
    sorted by joining date (newest first).
    """
    employees_cursor = employees_collection.find(
        {"department": department}
    ).sort("joining_date", -1)

    employees = []
    async for emp in employees_cursor:
        employees.append(employee_helper(emp))
    return employees

# -----------------------------
# 7. Average Salary by Department
# -----------------------------

async def average_salary_by_department():
    """
    Uses MongoDB aggregation to calculate average salary per department.
    Returns results sorted by department name.
    """
    pipeline = [
        {"$group": {
            "_id": "$department",
            "avg_salary": {"$avg": "$salary"}
        }},
        {"$project": {
            "department": "$_id",
            "avg_salary": {"$round": ["$avg_salary", 2]},
            "_id": 0
        }},
        {"$sort": {"department": 1}}  # Sort by department name (ascending)
    ]

    result = await employees_collection.aggregate(pipeline).to_list(length=100)
    return result

# -----------------------------
# 8. Search Employees by Skill
# -----------------------------

async def search_employees_by_skill(skill: str):
    """
    Finds employees who have a skill matching the given term (case-insensitive, whole word match).
    """
    regex_pattern = fr"\b{skill}\b"  # whole word, case-insensitive

    employees_cursor = employees_collection.find({
        "skills": {
            "$elemMatch": {
                "$regex": regex_pattern,
                "$options": "i"  # case-insensitive
            }
        }
    })

    employees = []
    async for emp in employees_cursor:
        employees.append(employee_helper(emp))
    return employees


# -----------------------------
# 9. Paginated List of Employees
# -----------------------------

async def list_employees_paginated(page: int = 1, limit: int = 20):
    """
    Returns a paginated list of employees, sorted by joining date (newest first).
    Limits are capped at 100 records per page.
    """
    if page < 1:
        page = 1
    if limit < 1:
        limit = 20
    if limit > 100:
        limit = 100  # Cap the limit to prevent overload

    skip = (page - 1) * limit

    cursor = employees_collection.find().sort("joining_date", -1).skip(skip).limit(limit)

    items = []
    async for emp in cursor:
        items.append(employee_helper(emp))

    total = await employees_collection.count_documents({})
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "items": items
    }
