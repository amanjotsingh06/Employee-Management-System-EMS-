employees = {
    101: {'name': 'Satya', 'age': 27, 'department': 'HR', 'salary': 50000},
    102: {'name': 'Aman', 'age': 20, 'department': 'IT', 'salary': 45000}
}

def main_menu():
    while True:
        print("\n====== Employee Management System ======")
        print("1. Add Employee")
        print("2. View All Employees")
        print("3. Search Employee")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            print("Thank you for using EMS!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

def add_employee():
    try:
        emp_id = int(input("Enter Employee ID: "))
    except ValueError:
        print("Invalid ID! Only numbers allowed.")
        return

    if emp_id in employees:
        print("Employee ID already exists! Try another ID.")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    employees[emp_id] = {
        'name': name,
        'age': int(age),
        'department': department,
        'salary': int(salary)
    }

    print("Employee added successfully!")

def view_employees():
    if not employees:
        print("\nNo employees available.")
        return

    print("\n===== All Employees =====")
    print("{:<10} {:<15} {:<10} {:<15} {:<10}".format("ID", "Name", "Age", "Department", "Salary"))
    print("-" * 60)

    for emp_id, details in employees.items():
        print("{:<10} {:<15} {:<10} {:<15} {:<10}".format(
            emp_id,
            details['name'],
            details['age'],
            details['department'],
            details['salary']
        ))

def search_employee():
    try:
        emp_id = int(input("Enter Employee ID to search: "))
    except ValueError:
        print("Invalid ID! Only numbers allowed.")
        return

    if emp_id in employees:
        emp = employees[emp_id]
        print("\nEmployee Found:")
        print("Name:", emp['name'])
        print("Age:", emp['age'])
        print("Department:", emp['department'])
        print("Salary:", emp['salary'])
    else:
        print("Employee not found.")
main_menu()

