import tkinter as tk

def display_selection():
    selected_radio = f"Selected Option: {radio_var.get()}"
    selected_checks = []
    if check1_var.get(): selected_checks.append("Option A")
    if check2_var.get(): selected_checks.append("Option B")
    if check3_var.get(): selected_checks.append("Option C")
    result_label.config(
        text=selected_radio + "\nSelected Checkboxes: " + ", ".join(selected_checks)
    )

# Initialize the main window
root = tk.Tk()
root.title("Radio and Check Buttons Example")

# Variables for storing selections
radio_var = tk.StringVar(value="None")
check1_var = tk.IntVar()
check2_var = tk.IntVar()
check3_var = tk.IntVar()


# Add Radio Buttons
tk.Label(root, text="Choose one option:").pack()
radio1 = tk.Radiobutton(root, text="Option 1", variable=radio_var, value="Option 1")
radio2 = tk.Radiobutton(root, text="Option 2", variable=radio_var, value="Option 2")
radio3 = tk.Radiobutton(root, text="Option 3", variable=radio_var, value="Option 3")
radio1.pack()
radio2.pack()
radio3.pack()


# Add Check Buttons
tk.Label(root, text="Select multiple options:").pack()
check1 = tk.Checkbutton(root, text="Option A", variable=check1_var)
check2 = tk.Checkbutton(root, text="Option B", variable=check2_var)
check3 = tk.Checkbutton(root, text="Option C", variable=check3_var)
check1.pack()
check2.pack()
check3.pack()

# Display Result
result_label = tk.Label(root, text="")
result_label.pack()

# Add Button to Display Selection
submit_button = tk.Button(root, text="Submit", command=display_selection)
submit_button.pack()

# Run the main loop
root.mainloop()

