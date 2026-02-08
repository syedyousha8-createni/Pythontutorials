# Import libraries
import sys
import FileHandling as fh
import logger as log

# Set log level
INFO = 1
DEBUG = 2
ERROR = 3
log_level = DEBUG  # Options: "INFO", "DEBUG", "ERROR"

# Global function definitions
def AddEmployeeRecord(file_name):
    global log_level

    if log_level:
        log.info("AddEmployeeRecord", "Adding a new employee record.")
    
    emp = dict()
    emp["name"] = input("Enter employee name: ")
    emp["id"] = int(input("Enter employee ID: "))
    emp["salary"] = float(input("Enter employee salary: "))
    emp["designation"] = input("Enter employee designation: ")
    record = f"{emp['id']}, {emp['name']}, {emp['salary']}, {emp['designation']}\n"
    if log_level == DEBUG: 
        log.debug("AddEmployeeRecord", f"New employee record: {record.strip()}")
    
    fh.appendFile(file_name, record)

def ShowEmployeeRecords(file_name):
    global log_level

    employee_records = list()

    if log_level:
        log.info("ShowEmployeeRecords", "Loading employee records.")

    if file_name:
        employee_records = LoadEmployeeRecords(file_name)
        log.debug("ShowEmployeeRecords", f"Loaded {len(employee_records)} employee records.") if log_level == DEBUG else None

    if not employee_records:
        print("No employee records found.")
    else:
        print(employee_records)
        print("Employee Records:")
        for emp in employee_records:
            print(f"Name: {emp['name']}\nID: {emp['id']}\nSalary: {emp['salary']}\nDesignation: {emp['designation']}")
            print("-" * 20)

def UpdateEmployeeRecord(employee_id, file_name):
    global log_level

    employee_records = list()
    log.info("UpdateEmployeeRecord", f"Updating employee record with ID: {employee_id}") if log_level else None

    if file_name:
        employee_records = LoadEmployeeRecords(file_name)
        log.debug("UpdateEmployeeRecord", f"Loaded {len(employee_records)} employee records.") if log_level == DEBUG else None
    
    if employee_records:
        for emp in employee_records:
            log.debug("UpdateEmployeeRecord", f"Checking employee ID: {emp['id']}") if log_level == DEBUG else None

            if int(emp["id"]) == int(employee_id):
                print("Enter new details for the employee (leave blank to keep current value):")
                new_name = input(f"Enter new name (current: {emp['name']}): ") or emp['name']
                new_salary = input(f"Enter new salary (current: {emp['salary']}): ") or emp['salary']
                new_designation = input(f"Enter new designation (current: {emp['designation']}): ") or emp['designation']
                
                emp['name'] = new_name
                emp['salary'] = float(new_salary)
                emp['designation'] = new_designation
                print(f"Employee record with ID {employee_id} updated.")
                break
        else:
            log.error("UpdateEmployeeRecord", f"No employee record found with ID {employee_id}.")
    else:
        log.error("UpdateEmployeeRecord", "No employee records found.")
    
    # Rewrite the file after update
    if employee_records:
        contents = ""
        for emp in employee_records:
            record = f"{emp['id']}, {emp['name']}, {emp['salary']}, {emp['designation']}\n"
            log.debug("UpdateEmployeeRecord", f"Writing record: {record.strip()}") if log_level == DEBUG else None
            contents = contents + record
        fh.writeFile(file_name, contents)

def DeleteEmployeeRecord(employee_id, file_name):
    global log_level

    employee_records = list()
    log.info("DeleteEmployeeRecord", f"Deleting employee record with ID: {employee_id}") if log_level else None

    if file_name:
        employee_records = LoadEmployeeRecords(file_name)
        log.debug("DeleteEmployeeRecord", f"Loaded {len(employee_records)} employee records.") if log_level == DEBUG else None
    
    if employee_records:
        for emp in employee_records:
            if int(emp["id"]) == int(employee_id):
                employee_records.remove(emp)
                log.info("DeleteEmployeeRecord", f"Employee record with ID {employee_id} deleted.") if log_level else None
                break
        else:
            log.error("DeleteEmployeeRecord", f"No employee record found with ID {employee_id}.")
    else:
        log.error("DeleteEmployeeRecord", "No employee records found.")
    
    # Rewrite the file after deletion
    if employee_records:
        contents = ""
        for emp in employee_records:
            record = f"{emp['id']}, {emp['name']}, {emp['salary']}, {emp['designation']}\n"
            log.debug("DeleteEmployeeRecord", f"Writing record: {record.strip()}") if log_level == DEBUG else None
            contents = contents + record
        fh.writeFile(file_name, contents)
    else:
        log.info("DeleteEmployeeRecord", "No records left. Deleting the file contents.") if log_level else None
        fh.writeFile(file_name, "")

def LoadEmployeeRecords(file_name):
    global log_level
    employee_records = list()
    log.info("LoadEmployeeRecords", f"Loading employee records from file: {file_name}") if log_level else None
    if file_name:
        content = fh.readFile(file_name)
        if content:            
            for record in content.splitlines():
                emp = dict()                
                if record.strip():
                    emp['id'], emp['name'], emp['salary'], emp['designation'] = record.split(', ')
                    log.debug("LoadEmployeeRecords", f"Loaded record: {record.strip()}") if log_level == DEBUG else None
                    employee_records.append(emp)
    else:
        log.error(f"File not found: {file_name}")
    return employee_records

# Entry point function
def main():
    global employee_records
    global file_name
    file_name = "employee_records.txt"
    print("Employee Records Management System")

    choose = None
    employee_records = list() # List to store employee records

    while choose != 0:
        print("\nMenu:")
        print("1. Add Employee Record")
        print("2. Show records")
        print("3. Delete Employee Record")
        print("4. Update Employee Record")
        print("5. Delete All Records")
        print("0. Exit")

        choose = int(input("Choose an operation: "))

        if choose == 1: # Add Employee Record
            AddEmployeeRecord(file_name)            
        elif choose == 2: # Show records
            ShowEmployeeRecords(file_name)
        elif choose == 3: # Delete Employee Record
            employee_id = int(input("Enter employee ID to delete: "))
            DeleteEmployeeRecord(employee_id, file_name)  
        elif choose == 4: # Update Employee Record
            employee_id = int(input("Enter employee ID to update: "))
            UpdateEmployeeRecord(employee_id, file_name)
        elif choose == 5: # Delete All Records
            fh.deleteFile(file_name)
            print("All employee records deleted.")
        elif choose == 0: # Exit
            print("Exiting the program.")
            break
        else:
            print("Invalid operation selected. Please try again...")       

    sys.exit(0)

## Call main()
if __name__ == "__main__":
    main()