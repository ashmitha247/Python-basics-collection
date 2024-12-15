'''


1. Import the Tkinter library to access GUI components.
2. Initialize a global variable exp to hold the current mathematical expression as a string.

3. Function Definitions:

a)press(n):
    Handles button presses for numbers and operators.
    Appends the pressed value to exp and updates the display.
b)equalpress():
    Evaluates the expression when the '=' button is pressed.
    Uses eval() to compute the result and updates the display.
    Handles errors if the evaluation fails.
c)clear():
    Resets the current expression and clears the display.
    Creating the Main Window

5. Set up the main GUI window with properties such as background color, title, and size.
6. Setting Up the Display

7. Create an entry widget to show the current expression, linked to the StringVar called equation.
8. Creating Number Buttons

9. Dynamically create buttons for numbers 1-9 using a loop.
10. Each button is linked to the press function.
11. Creating the '0' Button

Create a button for '0' and place it in the grid.
Creating Operation Buttons

Create buttons for basic operations: addition, subtraction, multiplication, and division.
Each button is linked to the press function.
Creating Special Buttons

Create buttons for the '=' operator (to evaluate the expression) and 'Clear' (to reset the expression).
Link these buttons to their respective functions (equalpress and clear).
Creating a Decimal Point Button

Create a button for the decimal point and link it to the press function.
Starting the GUI Event Loop

Call gui.mainloop() to start the Tkinter event loop, allowing the application to run and respond to user input.

'''













from tkinter import *  #This line imports ALL classes and functions from the tkinter module

#We initialize a global variable exp to hold the current mathematical expression as a string.
exp = ""


'''Overview: The press function handles the logic for when a number or operator button is pressed. 
It appends the button's value to the current expression and updates the display.

Why Convert to String?: The button's value (e.g., a number or operator) is received as an argument n, which may not always be a string.
To concatenate it with exp, which is a string, we convert n to a string using str(n). 
This ensures that we can safely append the new value to the existing expression without type errors. '''

# Function to handle button presses
def press(n): #The press function takes a parameter n, which represents the value of the button pressed.
    global exp
    exp = exp + str(n)  # Append the pressed button's value to the expression
    equation.set(exp)   # Update the display with the current expression


    ''' equation.set(exp):
    The set(value) method of StringVar is used to update the value of the variable. 
    When you call equation.set(value), it changes the value stored in the StringVar to whatever is passed as the argument (value).'''

# Function to evaluate the expression when '=' is pressed
def equalpress():
    global exp
    try:
        # Evaluate the expression and convert it to string
        t = str(eval(exp.replace('x', '*')))  # Replace 'x' with '*' for multiplication
        equation.set(t)  # Display the result
        exp = ""         # Reset the expression for the next calculation
    except:
        equation.set("error")  # Display error if evaluation fails
        exp = ""                # Reset expression to allow new input

# Function to clear the current expression
def clear():
    global exp
    exp = ""                # Reset the expression
    equation.set("")       # Clear the display

# Create the main window
gui = Tk()
gui.configure(background="light green")  # Set background color
gui.title("Simple Calculator")            # Set window title
gui.geometry("300x200")                   # Set a larger window size

# StringVar to hold the current expression for the display
equation = StringVar()
exp_field = Entry(gui, textvariable=equation)  # Create an entry widget for display
exp_field.grid(columnspan=4, ipadx=70)         # Place it in the grid

# Create number buttons
for i in range(1, 10):
    Button(gui, text=str(i), fg='black', bg='red', command=lambda x=i: press(x), height=1, width=7).grid(row=(i-1)//3 + 2, column=(i-1)%3)

b0 = Button(gui, text='0', fg='black', bg='red', command=lambda: press('0'), height=1, width=7)
b0.grid(row=5, column=0)

# Create operation buttons
add = Button(gui, text='+', fg='black', bg='red', command=lambda: press('+'), height=1, width=7)
add.grid(row=5, column=1)
sub = Button(gui, text='-', fg='black', bg='red', command=lambda: press('-'), height=1, width=7)
sub.grid(row=5, column=2)
mul = Button(gui, text='x', fg='black', bg='red', command=lambda: press('x'), height=1, width=7)
mul.grid(row=6, column=0)
div = Button(gui, text='/', fg='black', bg='red', command=lambda: press('/'), height=1, width=7)
div.grid(row=6, column=1)

# Create buttons for equal and clear
equal = Button(gui, text='=', fg='black', bg='red', command=equalpress, height=1, width=7)
equal.grid(row=6, column=2)
clear_button = Button(gui, text='Clear', fg='black', bg='red', command=clear, height=1, width=7)
clear_button.grid(row=7, column=0)

# Create a button for the decimal point
decimal = Button(gui, text='.', fg='black', bg='red', command=lambda: press('.'), height=1, width=7)
decimal.grid(row=7, column=1)

# Start the GUI event loop
gui.mainloop()
