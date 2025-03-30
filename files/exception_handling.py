'''

Exception handling in Python is a mechanism that allows you to manage errors gracefully without crashing your program. 
It enables you to write code that can respond to unexpected situations (like invalid input, file not found, etc.) in a controlled way.

##Basic Structure of Exception Handling
In Python, exception handling is typically done using the try, except, else, and finally blocks. Here’s a brief overview of each:

try block: 
This is where you write the code that might raise an exception. If an exception occurs, the rest of the code in the try block is skipped.

except block:
This block is executed if an exception occurs in the try block. You can specify the type of exception you want to catch.

else block: 
This block is optional and runs if the try block does not raise an exception.

finally block: 
This block is also optional and runs no matter what, whether an exception occurred or not.
It can be used for cleanup actions or to indicate that the function has finished executing.
'''

def divide_numbers():
    try:
        # Ask the user for two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        
        # Perform division
        result = num1 / num2
        
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except ValueError:
        print("Error: Please enter valid numbers.")
    except IOError: #when u try to open a file that doesnt exist or we dont have the permission to open the file
        print("Error: An input/output error occurred.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of {num1} divided by {num2} is {result}.")
    finally:
        print("Execution of the divide_numbers function is complete.")

# Call the function
divide_numbers()

'''
TypeError: Raised when an operation is performed on an object of an inappropriate type
(e.g., trying to add a string to an integer).

ValueError: Raised when a function receives an argument of the correct type
but an inappropriate value (e.g., trying to convert a non-numeric string to an integer).

except IOError: when u try to open a file that doesnt exist or we dont have the permission to open the file

"except Exception as e" is a syntax used in Python to catch all exceptions that inherit from the base Exception class
and assign the caught exception to the variable e for further handling or logging.

'''