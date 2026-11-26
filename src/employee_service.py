import json
from employee import Employee

FILE_PATH = "data/employee.json"

def load_employees():
    try:
        with open(FILE_PATH,"r") as file:
            return json.load(file)
    except:
        return []

def save_employees(employee):
    with open(FILE_PATH,"w") as file:
        return json.dump(employee,file,indent=4)

def add_employee():
    emp_id = input("Enter Emp id ")
    department = input("Enter department ")
    salary = float(input("Enter salary "))
    name = input("Enter name ")

    employee = Employee(emp_id,name,department,salary)
    employees = load_employees()
    employees.append(employee.to_dict())
    save_employees(employees)

    print("\n Employee Data added successfully")
    

