# import libraries
import sys
import os

# Global function definitions
def readFile(file_name):
    try:
        with open(file_name, "r") as file_handle:
            return file_handle.read()
    except FileNotFoundError:
        print(f"File not found: {file_name}")

def writeFile(file_name, contents):
    file_handle = open(file_name, "w")
    if file_handle:
        file_handle.write(contents + "\n")
        file_handle.close()
    else:
        print(f"File not found: {file_name}")

def appendFile(file_name, contents):
    file_handle = open(file_name, "a")
    if file_handle:        
        file_handle.write(contents)
        file_handle.close()
    else:
        print(f"File not found: {file_name}")

def deleteFile(file_name):
    try:
        os.remove(file_name)
        print(f"File deleted: {file_name}")
    except FileNotFoundError:
        print(f"File not found: {file_name}")

"""
# Entry point function
def main():
    file_name = input("Enter file name: ")

    while file_name:
        file_operation = input("Enter the file operation you wish to perform: (r for read, \
                               w for write, a for append, d for delete and e for exit): ")

        if file_operation == "a":   # Append operation
            appendFile(file_name)    
        elif file_operation == "w": # Write File
            writeFile(file_name)    
        elif file_operation == "r": # Read File
            readFile(file_name)
        elif file_operation == "d": # Delete File
            deleteFile(file_name)
        elif file_operation == "e": # Exit program
            break
        else:
            print("Invalid file operation. Please try again...")

    sys.exit(0)

# Call main()
main()
"""