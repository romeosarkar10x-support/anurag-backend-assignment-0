# routes/employees.py

from fastapi import APIRouter, Query, Depends
from models import Employee, UpdateEmployee
import crud
from auth import get_current_user

# Create router instance for employee-related routes
router = APIRouter()

# -----------------------------
# 1. Create New Employee (Protected)
# -----------------------------

@router.post("/", response_model=Employee, summary="Create a new employee")
async def create_employee(employee: Employee, user=Depends(get_current_user)):
    """
    Creates a new employee entry.
    Requires authentication.
    """
    return await crud.create_employee(employee)


# -----------------------------
# 5. List Employees (All, Filtered, or Paginated)
# -----------------------------

@router.get("/", summary="List employees (all, by department, or paginated)")
async def list_employees(
    department: str = None,
    page: int = Query(1, ge=1),
    limit: int = Query(20, ge=1, le=100)
):
    """
    Lists employees:
    - If 'department' is provided, filters by department.
    - Otherwise, returns paginated list (sorted by newest).
    """
    if department:
        return await crud.list_employees_by_department(department)
    return await crud.list_employees_paginated(page=page, limit=limit)

# -----------------------------
# 6. Average Salary by Department
# -----------------------------

@router.get("/avg-salary", summary="Average salary grouped by department")
async def avg_salary():
    """
    Returns the average salary for each department.
    """
    return await crud.average_salary_by_department()

# -----------------------------
# 7. Search Employees by Skill
# -----------------------------

@router.get("/search", summary="Search employees by skill")
async def search_employees(skill: str):
    """
    Searches for employees who have a given skill.
    """
    return await crud.search_employees_by_skill(skill)

# -----------------------------
# 2. Get Employee by ID
# -----------------------------

@router.get("/{employee_id}", response_model=Employee, summary="Get employee by ID")
async def get_employee(employee_id: str):
    """
    Retrieves an employee by their employee_id.
    """
    return await crud.get_employee(employee_id)

# -----------------------------
# 3. Update Employee (Protected)
# -----------------------------

@router.put("/{employee_id}", response_model=Employee, summary="Update an existing employee")
async def update_employee(employee_id: str, updates: UpdateEmployee, user=Depends(get_current_user)):
    """
    Updates fields of an existing employee.
    Requires authentication.
    """
    return await crud.update_employee(employee_id, updates)

# -----------------------------
# 4. Delete Employee (Protected)
# -----------------------------

@router.delete("/{employee_id}", summary="Delete an employee")
async def delete_employee(employee_id: str, user=Depends(get_current_user)):
    """
    Deletes an employee by their employee_id.
    Requires authentication.
    """
    return await crud.delete_employee(employee_id)
