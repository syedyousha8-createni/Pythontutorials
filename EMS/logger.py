# import libraries
import sys

# Global function definitions
def info(function_name, msg):
    if not function_name:
        print("Error: function_name is required for logging.")
        return(-1)
    
    if not msg:
        print("Error: message is required for logging.")
        return(-1)
        
    print(f"[INFO] {function_name}() -> {msg}")
    return(0)

def debug(function_name, msg):
    if not function_name:
        print("Error: function_name is required for logging.")
        return(-1)
    
    if not msg:
        print("Error: message is required for logging.")
        return(-1)
        
    print(f"[DEBUG] {function_name}() -> {msg}")
    return(0)

def error(function_name, msg):
    if not function_name:
        print("Error: function_name is required for logging.")
        return(-1)
    
    if not msg:
        print("Error: message is required for logging.")
        return(-1)
        
    print(f"[ERROR] {function_name}() -> {msg}")
    return(0)

"""
# Entry point function
def main():
    info("main", "Hello, World!!!")
    debug("main", "Hello, World!!!")
    error("main", "Hello, World!!!")
    sys.exit(0)

# Call the entry point function
if __name__ == "__main__":
    main()
"""