import asyncio
from database import employees_collection  # Assume Motor collection instance

async def test_connection():
    try:
        # Try finding one document to check connection
        employee = await employees_collection.find_one()
        print("Connection successful!")
        print("Sample document:", employee)

        employees = [
            {
            "employee_id": "E130",
            "name": "Employee 30",
            "department": "Engineering",
            "salary": 90000,
            "joining_date": "2025-09-12",
            "skills": ["Python", "Docker", "Kubernetes", "Git"]
            },
            {
            "employee_id": "E129",
            "name": "Employee 29",
            "department": "Data Scientist",
            "salary": 95000,
            "joining_date": "2025-09-11",
            "skills": ["Python", "R", "Machine Learning", "SQL"]
            },
            {
            "employee_id": "E128",
            "name": "Employee 28",
            "department": "HR",
            "salary": 60000,
            "joining_date": "2025-09-10",
            "skills": ["Communication", "Recruitment", "Conflict Resolution", "Interviewing"]
            },
            {
            "employee_id": "E127",
            "name": "Employee 27",
            "department": "Sales",
            "salary": 65000,
            "joining_date": "2025-09-09",
            "skills": ["Negotiation", "CRM", "Lead Generation", "Communication"]
            },
            {
            "employee_id": "E126",
            "name": "Employee 26",
            "department": "Marketing",
            "salary": 70000,
            "joining_date": "2025-09-08",
            "skills": ["SEO", "Content Creation", "Google Analytics", "Communication"]
            },
            {
            "employee_id": "E125",
            "name": "Employee 25",
            "department": "Engineering",
            "salary": 88000,
            "joining_date": "2025-09-07",
            "skills": ["Python", "Microservices", "REST APIs", "Git"]
            },
            {
            "employee_id": "E124",
            "name": "Employee 24",
            "department": "Data Scientist",
            "salary": 93000,
            "joining_date": "2025-09-06",
            "skills": ["Python", "TensorFlow", "Data Visualization", "SQL"]
            },
            {
            "employee_id": "E123",
            "name": "Employee 23",
            "department": "HR",
            "salary": 58000,
            "joining_date": "2025-09-05",
            "skills": ["Onboarding", "Payroll", "Interviewing", "Communication"]
            },
            {
            "employee_id": "E122",
            "name": "Employee 22",
            "department": "Sales",
            "salary": 64000,
            "joining_date": "2025-09-04",
            "skills": ["Salesforce", "Cold Calling", "Communication", "Lead Generation"]
            },
            {
            "employee_id": "E121",
            "name": "Employee 21",
            "department": "Marketing",
            "salary": 68000,
            "joining_date": "2025-09-03",
            "skills": ["Email Marketing", "Content Creation", "Google Ads", "SEO"]
            },
            {
            "employee_id": "E120",
            "name": "Employee 20",
            "department": "Engineering",
            "salary": 87000,
            "joining_date": "2025-09-02",
            "skills": ["Java", "Spring Boot", "Unit Testing", "Git"]
            },
            {
            "employee_id": "E119",
            "name": "Employee 19",
            "department": "Data Scientist",
            "salary": 92000,
            "joining_date": "2025-09-01",
            "skills": ["Python", "PyTorch", "Statistics", "Data Wrangling"]
            },
            {
            "employee_id": "E118",
            "name": "Employee 18",
            "department": "HR",
            "salary": 59000,
            "joining_date": "2025-08-31",
            "skills": ["Employee Relations", "Recruitment", "Compliance", "Communication"]
            },
            {
            "employee_id": "E117",
            "name": "Employee 17",
            "department": "Sales",
            "salary": 63000,
            "joining_date": "2025-08-30",
            "skills": ["Negotiation", "Lead Management", "CRM", "Communication"]
            },
            {
            "employee_id": "E116",
            "name": "Employee 16",
            "department": "Marketing",
            "salary": 67000,
            "joining_date": "2025-08-29",
            "skills": ["Content Strategy", "SEO", "Google Analytics", "Social Media"]
            },
            {
            "employee_id": "E115",
            "name": "Employee 15",
            "department": "Engineering",
            "salary": 86000,
            "joining_date": "2025-08-28",
            "skills": ["C++", "Linux", "Agile", "Git"]
            },
            {
            "employee_id": "E114",
            "name": "Employee 14",
            "department": "Data Scientist",
            "salary": 91000,
            "joining_date": "2025-08-27",
            "skills": ["R", "Data Mining", "Python", "Statistics"]
            },
            {
            "employee_id": "E113",
            "name": "Employee 13",
            "department": "HR",
            "salary": 57000,
            "joining_date": "2025-08-26",
            "skills": ["Payroll", "Onboarding", "Employee Engagement", "Communication"]
            },
            {
            "employee_id": "E112",
            "name": "Employee 12",
            "department": "Sales",
            "salary": 62000,
            "joining_date": "2025-08-25",
            "skills": ["Cold Calling", "Lead Gen", "Negotiation", "Communication"]
            },
            {
            "employee_id": "E111",
            "name": "Employee 11",
            "department": "Marketing",
            "salary": 66000,
            "joining_date": "2025-08-24",
            "skills": ["Social Media", "SEO", "Content Writing", "Email Marketing"]
            },
            {
            "employee_id": "E110",
            "name": "Employee 10",
            "department": "Engineering",
            "salary": 85000,
            "joining_date": "2025-08-23",
            "skills": ["Docker", "Kubernetes", "Python", "Git"]
            },
            {
            "employee_id": "E109",
            "name": "Employee 9",
            "department": "Data Scientist",
            "salary": 90000,
            "joining_date": "2025-08-22",
            "skills": ["TensorFlow", "Python", "Machine Learning", "Data Visualization"]
            },
            {
            "employee_id": "E108",
            "name": "Employee 8",
            "department": "HR",
            "salary": 56000,
            "joining_date": "2025-08-21",
            "skills": ["Recruitment", "Communication", "Conflict Resolution", "Compliance"]
            },
            {
            "employee_id": "E107",
            "name": "Employee 7",
            "department": "Sales",
            "salary": 61000,
            "joining_date": "2025-08-20",
            "skills": ["CRM", "Lead Generation", "Negotiation", "Communication"]
            },
            {
            "employee_id": "E106",
            "name": "Employee 6",
            "department": "Marketing",
            "salary": 65000,
            "joining_date": "2025-08-19",
            "skills": ["Google Ads", "SEO", "Content Creation", "Analytics"]
            },
            {
            "employee_id": "E105",
            "name": "Employee 5",
            "department": "Engineering",
            "salary": 84000,
            "joining_date": "2025-08-18",
            "skills": ["JavaScript", "React", "Node.js", "Git"]
            },
            {
            "employee_id": "E104",
            "name": "Employee 4",
            "department": "Data Scientist",
            "salary": 89000,
            "joining_date": "2025-08-17",
            "skills": ["R", "Python", "Statistics", "Machine Learning"]
            },
            {
            "employee_id": "E103",
            "name": "Employee 3",
            "department": "HR",
            "salary": 55000,
            "joining_date": "2025-08-16",
            "skills": ["Employee Engagement", "Onboarding", "Communication", "Recruitment"]
            },
            {
            "employee_id": "E102",
            "name": "Employee 2",
            "department": "Sales",
            "salary": 60000,
            "joining_date": "2025-08-15",
            "skills": ["Lead Management", "CRM", "Negotiation", "Communication"]
            },
            {
            "employee_id": "E101",
            "name": "Employee 1",
            "department": "Marketing",
            "salary": 64000,
            "joining_date": "2025-08-14",
            "skills": ["Email Marketing", "Content Writing", "SEO", "Social Media"]
            }
        ]


        result = await employees_collection.insert_many(employees)
        print(f"Inserted document IDs: {result.inserted_ids}")

    except Exception as e:
        print("Error during MongoDB operation:", e)

if __name__ == "__main__":
    asyncio.run(test_connection())


