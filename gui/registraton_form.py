#AIM : Write a python program to create a registration form which uses a GUI by importing tkinter.

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText


# Function to handle form submission
def submit_form():
    name = entry_name.get()
    email = entry_email.get()
    gender = gender_var.get()
    country = combo_country.get()
    terms_accepted = terms_var.get()
    comments = scrolled_text.get("1.0", tk.END).strip()

    if not name or not email or not gender or not country:
        messagebox.showwarning("Incomplete Form", "Please fill all the mandatory fields.")
        return
    
    if not terms_accepted:
        messagebox.showwarning("Terms Not Accepted", "You must accept the terms and conditions.")
        return
    
    result = f"""
    Registration Details:
    Name: {name}
    Email: {email}
    Gender: {gender}
    Country: {country}
    Comments: {comments}
    """
    messagebox.showinfo("Form Submitted", result)

# Create main application window
root = tk.Tk()
root.title("Registration Form")
root.geometry("500x600")

# Text box: Name
tk.Label(root, text="Name:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
entry_name = tk.Entry(root, font=("Arial", 12), width=40)
entry_name.pack(padx=10, pady=5)

# Text box: Email
tk.Label(root, text="Email:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
entry_email = tk.Entry(root, font=("Arial", 12), width=40)
entry_email.pack(padx=10, pady=5)

# Radio button: Gender
tk.Label(root, text="Gender:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", font=("Arial", 12)).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", font=("Arial", 12)).pack(anchor="w", padx=20)
tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", font=("Arial", 12)).pack(anchor="w", padx=20)

# Combo box: Country
tk.Label(root, text="Country:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
combo_country = ttk.Combobox(root, values=["USA", "Canada", "UK", "India", "Australia"], font=("Arial", 12), width=38)
combo_country.pack(padx=10, pady=5)
combo_country.set("Select any one country")

# Check button: Terms and Conditions
terms_var = tk.BooleanVar()
tk.Checkbutton(root, text="I accept the Terms and Conditions", variable=terms_var, font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)

# Scrolled Text: Comments
tk.Label(root, text="Comments:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
scrolled_text = ScrolledText(root, width=45, height=5, font=("Arial", 12))
scrolled_text.pack(padx=10, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=submit_form)
submit_button.pack(pady=20)

# Run the main loop
root.mainloop()
