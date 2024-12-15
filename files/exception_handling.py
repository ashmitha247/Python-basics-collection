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
It is often used for cleanup actions (like closing files). '''

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
Explanation of the Program

Function Definition:
def divide_numbers():
We define a function called divide_numbers that encapsulates the logic for dividing two numbers.


Try Block:
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
Inside the try block, we prompt the user to enter two numbers. We convert the input to float to allow decimal numbers.
We then attempt to divide num1 by num2.
Except Blocks:

ZeroDivisionError:
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")
This block catches the specific case where the user tries to divide by zero. If this happens, it prints an error message.

ValueError:
except ValueError:
    print("Error: Please enter valid numbers.")
This block catches cases where the user inputs something that cannot be converted to a float (like letters or special characters).
It prints an appropriate error message.

General Exception:
except Exception as e:
    print(f"An unexpected error occurred: {e}")
This block catches any other exceptions that were not specifically handled above.
It prints a generic error message along with the exception message.

Else Block:
else:
    print(f"The result of {num1} divided by {num2} is {result}.")
If no exceptions were raised in the try block, this block executes and prints the result of the division.

Finally Block:
finally:
    print("Execution of the divide_numbers function is complete.")
This block runs regardless of whether an exception occurred or not.
 It can be used for cleanup actions or to indicate that the function has finished executing.

Function Call:
divide_numbers()
Finally, we call the divide_numbers function to execute the code.


Example Usage
Valid Input:

If the user inputs 10 and 2, the output will be:


The result of 10.0 divided by 2.0 is 5.0.
Execution of the divide_numbers function is complete.


Division by Zero:
If the user inputs 10 and 0, the output will be:

Error: You cannot divide by zero.
Execution of the divide_numbers function is complete.

Invalid Input:
If the user inputs a non-numeric value, such as abc for the first number, the output will be:
Error: Please enter valid numbers.
Execution of the divide_numbers function is complete.
In this case, the ValueError exception is raised when trying to convert the input abc to a float, and the corresponding error message is printed.

Multiple Invalid Inputs:
If the user inputs a valid number for the first input (e.g., 10) and then inputs a non-numeric value for the second input (e.g., xyz), the output will be:
Enter the first number: 10
Enter the second number: xyz
Error: Please enter valid numbers.
Execution of the divide_numbers function is complete.
General Exception Handling:

If an unexpected error occurs
(for example, if the user inputs a very large number that causes an overflow),
 the program will catch it in the general except Exception as e block:

An unexpected error occurred: <error message>
Execution of the divide_numbers function is complete.

Summary of Exception Handling
Graceful Error Management: The program demonstrates how to handle different types of exceptions gracefully. 
Instead of crashing, it provides informative messages to the user, allowing them to correct their input.

Specific vs. General Exceptions:
By catching specific exceptions like ZeroDivisionError and ValueError, the program can provide tailored feedback.
The general Exception catch-all allows for handling any unforeseen errors.

Control Flow: The use of else and finally blocks allows for clear control flow.
The else block executes only when no exceptions occur, while the finally block always executes,
making it useful for cleanup or final messages.'''