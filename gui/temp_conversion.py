import tkinter as tk

def convert_temperature():
    try:
        temp = float(entry.get())
        if var.get() == "C to F":
            result = (temp * 9/5) + 32
            result_label.config(text=f"{temp}°C = {result:.2f}°F")
        else:
            result = (temp - 32) * 5/9
            result_label.config(text=f"{temp}°F = {result:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Main application window
root = tk.Tk()
root.title("Temperature Converter")

# Entry widget for temperature input
tk.Label(root, text="Enter Temperature:").grid(row=0, column=0, padx=10, pady=5)
entry = tk.Entry(root, width=10)
entry.grid(row=0, column=1, padx=10, pady=5)

# Radio buttons for conversion direction
var = tk.StringVar(value="C to F")
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value="C to F").grid(row=1, column=0, columnspan=2)
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value="F to C").grid(row=2, column=0, columnspan=2)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

# Result label
result_label = tk.Label(root, text="Result will appear here", font=("Helvetica", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the main loop
root.mainloop()