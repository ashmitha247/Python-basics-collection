import tkinter as tk
from tkinter import messagebox, filedialog, ttk

class GreenKiranaApp:
    def __init__(self, root):
        self.setup_root(root)
        self.build_tabs()

    def setup_root(self, root):
        root.title("Green Kirana Centers")
        root.geometry("900x700")
        root.configure(bg="#f0f5f0")

    def build_tabs(self):
        self.notebook = ttk.Notebook()
        self.notebook.pack(pady=10, expand=True, fill='both')

        tabs = {
            "Registration": self.registration_tab,
            "Waste Classification": self.classification_tab,
            "Location Mapping": self.locations_tab,
            "QR Code": self.qr_code_tab,
            "Contribution Log": self.contributions_tab,
            "Achievements": self.achievements_tab,
            "Rewards": self.rewards_tab
        }

        for title, content_creator in tabs.items():
            frame = ttk.Frame(self.notebook, padding=10)
            content_creator(frame)
            self.notebook.add(frame, text=title)

    def registration_tab(self, frame):
        self.create_section_title(frame, "Registration Form")

        self.entries = {
            "Name": self.create_entry(frame, "Name"),
            "Phone": self.create_entry(frame, "Phone Number"),
            "Email": self.create_entry(frame, "Email"),
            "Aadhaar": self.create_entry(frame, "Aadhaar Number"),
        }
        self.address_box = self.create_text_area(frame, "Address")

        ttk.Button(frame, text="Submit Registration", command=self.register_user).pack(pady=20)

    def classification_tab(self, frame):
        self.create_section_title(frame, "Waste Classification")

        ttk.Label(frame, text="Select or Upload Image:", font=("Arial", 12)).pack(pady=5)
        ttk.Button(frame, text="Upload Image", command=self.upload_image).pack(pady=10)

        self.category_selector = ttk.Combobox(frame, state="readonly",
                                               values=["Recyclable", "Organic", "Hazardous"])
        self.category_selector.set("Choose Waste Category")
        self.category_selector.pack(pady=10)

        ttk.Button(frame, text="Classify", command=self.classify_waste).pack(pady=20)

    def locations_tab(self, frame):
        self.create_section_title(frame, "Drop-off Locations")

        locations = ["Location 1: 9 AM - 5 PM", "Location 2: 10 AM - 6 PM", "Location 3: 8 AM - 4 PM"]
        for loc in locations:
            ttk.Label(frame, text=loc, font=("Arial", 12)).pack(pady=5)

    def qr_code_tab(self, frame):
        self.create_section_title(frame, "QR Code Generation")

        ttk.Label(frame, text="Generate a unique QR Code for your waste contributions.", font=("Arial", 12)).pack(pady=5)
        ttk.Button(frame, text="Generate QR Code", command=self.generate_qr_code).pack(pady=20)

    def contributions_tab(self, frame):
        self.create_section_title(frame, "Contribution Log")

        ttk.Label(frame, text="Track your waste contributions.", font=("Arial", 12)).pack(pady=5)
        ttk.Button(frame, text="Log Contribution", command=self.log_contribution).pack(pady=20)

    def achievements_tab(self, frame):
        self.create_section_title(frame, "Achievements")

        ttk.Label(frame, text="View your progress and eco-milestones!", font=("Arial", 12)).pack(pady=5)
        ttk.Button(frame, text="View Achievements", command=self.view_achievements).pack(pady=20)

    def rewards_tab(self, frame):
        self.create_section_title(frame, "Rewards and Benefits")

        rewards = [
            "Discounts on utility bills",
            "Coupons for local businesses",
            "Recognition badges for milestones"
        ]
        for reward in rewards:
            ttk.Label(frame, text=f"- {reward}", font=("Arial", 12)).pack(pady=5)

    def create_section_title(self, frame, title):
        ttk.Label(frame, text=title, font=("Arial", 16, "bold"), foreground="#1e7c1e").pack(pady=10)

    def create_entry(self, frame, placeholder):
        ttk.Label(frame, text=placeholder, font=("Arial", 12)).pack(pady=5)
        entry = ttk.Entry(frame, width=50)
        entry.pack(pady=5)
        return entry

    def create_text_area(self, frame, label):
        ttk.Label(frame, text=label, font=("Arial", 12)).pack(pady=5)
        text_area = tk.Text(frame, height=3, width=50)
        text_area.pack(pady=5)
        return text_area

    def register_user(self):
        missing_fields = [key for key, entry in self.entries.items() if not entry.get()]
        address = self.address_box.get("1.0", tk.END).strip()

        if missing_fields or not address:
            messagebox.showwarning("Incomplete Form", f"Please fill in the missing fields: {', '.join(missing_fields)}")
        else:
            messagebox.showinfo("Registration Complete", "Thank you for registering with Green Kirana Centers!")

    def upload_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            messagebox.showinfo("Upload Successful", f"File selected: {file_path}")

    def classify_waste(self):
        category = self.category_selector.get()
        if category == "Choose Waste Category":
            messagebox.showwarning("Classification Error", "Please select a valid category.")
        else:
            messagebox.showinfo("Classification Complete", f"Waste classified as: {category}")

    def generate_qr_code(self):
        messagebox.showinfo("QR Code", "QR Code generated successfully!")

    def log_contribution(self):
        messagebox.showinfo("Contribution Log", "Your contribution has been logged.")

    def view_achievements(self):
        messagebox.showinfo("Achievements", "View your eco-milestones and progress here.")

if __name__ == "__main__":
    root = tk.Tk()
    app = GreenKiranaApp(root)
    root.mainloop()
