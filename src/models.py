from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# -----------------------------
# Employee Schema for Input/Output
# -----------------------------

class Employee(BaseModel):
    """
    Schema for creating or retrieving an employee record.
    """
    employee_id: str             # Unique identifier for the employee
    name: str                    # Full name of the employee
    department: str              # Department the employee belongs to
    salary: float                # Salary as a floating-point number
    joining_date: date          # Date the employee joined
    skills: List[str]           # List of skills the employee has

# -----------------------------
# Schema for Updating Employee Fields
# -----------------------------

class UpdateEmployee(BaseModel):
    """
    Schema for updating an existing employee.
    All fields are optional to allow partial updates.
    """
    name: Optional[str] = None             # Updated name
    department: Optional[str] = None       # Updated department
    salary: Optional[float] = None         # Updated salary
    joining_date: Optional[date] = None    # Updated joining date
    skills: Optional[List[str]] = None     # Updated list of skills
