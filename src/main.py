from employee_service import add_employee

while True:
    print("\n Employee Management System")
    print("1. Add Employee")
    print("2. Exit")

    choice = int(input("Enter your Choice"))

    if choice==1:
        add_employee()
    elif choice==2:
        break