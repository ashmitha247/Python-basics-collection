from tkinter import *

# Initialize an empty string to hold the expression
exp = ""

# Function to handle button presses
def press(n):
    global exp
    exp = exp + str(n)  # Append the pressed button's value to the expression
    equation.set(exp)   # Update the display with the current expression

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
