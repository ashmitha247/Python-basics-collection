import tkinter as tk
from tkinter import ttk

class PizzaOrderSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Order System")

        # Create main frames
        self.order_frame = ttk.Frame(self.root)
        self.order_frame.pack(padx=10, pady=10)

        self.payment_frame = ttk.Frame(self.root)
        self.payment_frame.pack(padx=10, pady=10)

        # Order frame
        self.size_label = ttk.Label(self.order_frame, text="Select Pizza Size:")
        self.size_label.pack()

        self.size_var = tk.StringVar()
        self.size_var.set("Medium")

        self.size_radio = ttk.Radiobutton(self.order_frame, text="Small", variable=self.size_var, value="Small")
        self.size_radio.pack(side=tk.LEFT, padx=5)

        self.size_radio = ttk.Radiobutton(self.order_frame, text="Medium", variable=self.size_var, value="Medium")
        self.size_radio.pack(side=tk.LEFT, padx=5)

        self.size_radio = ttk.Radiobutton(self.order_frame, text="Large", variable=self.size_var, value="Large")
        self.size_radio.pack(side=tk.LEFT, padx=5)

        self.topping_label = ttk.Label(self.order_frame, text="Select Toppings:")
        self.topping_label.pack()

        self.topping_var1 = tk.IntVar()
        self.topping_var2 = tk.IntVar()
        self.topping_var3 = tk.IntVar()

        self.topping_check = ttk.Checkbutton(self.order_frame, text="Pepperoni", variable=self.topping_var1)
        self.topping_check.pack(side=tk.LEFT, padx=5)

        self.topping_check = ttk.Checkbutton(self.order_frame, text="Mushrooms", variable=self.topping_var2)
        self.topping_check.pack(side=tk.LEFT, padx=5)

        self.topping_check = ttk.Checkbutton(self.order_frame, text="Olives", variable=self.topping_var3)
        self.topping_check.pack(side=tk.LEFT, padx=5)

        # Payment frame
        self.payment_label = ttk.Label(self.payment_frame, text="Select Payment Method:")
        self.payment_label.pack()

        self.payment_var = tk.StringVar()
        self.payment_var.set("Cash")

        self.payment_radio = ttk.Radiobutton(self.payment_frame, text="Cash", variable=self.payment_var, value="Cash")
        self.payment_radio.pack(side=tk.LEFT, padx=5)

        self.payment_radio = ttk.Radiobutton(self.payment_frame, text="Card", variable=self.payment_var, value="Card")
        self.payment_radio.pack(side=tk.LEFT, padx=5)

        # Order button
        self.order_button = ttk.Button(self.root, text="Place Order", command=self.place_order)
        self.order_button.pack(pady=10)

    def place_order(self):
        size = self.size_var.get()
        toppings = []
        if self.topping_var1.get():
            toppings.append("Pepperoni")
        if self.topping_var2.get():
            toppings.append("Mushrooms")
        if self.topping_var3.get():
            toppings.append("Olives")
        payment_method = self.payment_var.get()

        print(f"Order Details:")
        print(f"Size: {size}")
        print(f"Toppings: {', '.join(toppings)}")
        print(f"Payment Method: {payment_method}")

if __name__ == "__main__":
    root = tk.Tk()  
    app = PizzaOrderSystem(root)
    root.mainloop()