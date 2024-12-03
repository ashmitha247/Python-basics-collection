import tkinter as tk  # Import the tkinter library for GUI
from tkinter import ttk, messagebox  # Import ttk for themed widgets and messagebox for alerts

class PythonLearningRoadmapApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Python Learning Roadmap")  # Set the window title
        self.root.geometry("700x500")  # Set the window size
        self.root.configure(bg="#f7f7f7")  # Set background color

        # Create a main frame for the application
        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title Label
        self.title_label = ttk.Label(
            self.main_frame,
            text="Python Learning Roadmap",
            font=("Helvetica", 18, "bold"),
            foreground="#333",
        )
        self.title_label.grid(row=0, column=0, columnspan=3, pady=15)

        # Experience Level Selection
        self.experience_label = ttk.Label(self.main_frame, text="Select Your Experience Level:")
        self.experience_label.grid(row=1, column=0, sticky=tk.W, pady=5)

        # Variable to hold the selected experience level
        self.experience_var = tk.StringVar(value="Beginner")
        self.experience_combobox = ttk.Combobox(self.main_frame, textvariable=self.experience_var)
        self.experience_combobox["values"] = ("Beginner", "Intermediate", "Advanced")  # Options for experience levels
        self.experience_combobox.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Specialization Selection
        self.specialization_label = ttk.Label(self.main_frame, text="Select Your Specialization:")
        self.specialization_label.grid(row=2, column=0, sticky=tk.W, pady=5)

        # Variable to hold the selected specialization
        self.specialization_var = tk.StringVar(value="")
        self.specialization_combobox = ttk.Combobox(self.main_frame, textvariable=self.specialization_var)
        self.specialization_combobox["values"] = ("Web Development", "Data Science", "Game Development")  # Options for specializations
        self.specialization_combobox.grid(row=2, column=1, sticky=(tk.W, tk.E))

        # Generate Roadmap Button
        self.generate_button = ttk.Button(
            self.main_frame, text="Generate Roadmap", command=self.generate_roadmap  # Button to generate the roadmap
        )
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=15)

        # Reset Button
        self.reset_button = ttk.Button(
            self.main_frame, text="Reset Selections", command=self.reset_selections  # Button to reset selections
        )
        self.reset_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Roadmap Output Frame
        self.roadmap_frame = ttk.LabelFrame(self.main_frame, text="Your Roadmap", padding="10")
        self.roadmap_frame.grid(row=6, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))

        # Text area to display the generated roadmap
        self.roadmap_text = tk.Text(self.roadmap_frame, height=10, width=60, bg="#eef", wrap=tk.WORD)
        self.roadmap_text.pack()

    def generate_roadmap(self):
        # Generate a learning roadmap based on user selections
        specialization = self.specialization_var.get()  # Get selected specialization
        experience = self.experience_var.get()  # Get selected experience level
        roadmap = []  # Initialize an empty roadmap list

        # Determine roadmap based on specialization and experience level
        if specialization == "Web Development":
            if experience == "Beginner":
                roadmap = [
                    "1. Learn Python Basics",
                    "2. Understand HTML & CSS",
                    "3. Learn Flask or Django",
                    "4. Build a Simple Web App",
                    "5. Deploy Your Application",
                    "6. Explore Frontend Technologies (JavaScript, React)",
                ]
            elif experience == "Intermediate":
                roadmap = [
                    "1. Master Flask or Django",
                    "2. Learn about RESTful APIs",
                    "3. Work with Databases (SQL, NoSQL)",
                    "4. Build Full-Stack Applications",
                    "5. Learn Deployment Strategies (Docker, Heroku)",
                    "6. Explore Frontend Frameworks (React, Angular)",
                ]
            elif experience == "Advanced":
                roadmap = [
                    "1. Contribute to Open Source Web Projects",
                    "2. Learn about Microservices Architecture",
                    "3. Explore Cloud Services (AWS, Azure)",
                    "4. Optimize Performance and Security",
                    "5. Learn about DevOps Practices",
                    "6. Build Scalable Applications",
                ]

        elif specialization == "Data Science":
            if experience == "Beginner":
                roadmap = [
                    "1. Learn Python Basics",
                    "2. Understand Data Structures",
                    "3. Learn NumPy and Pandas",
                    "4. Data Visualization with Matplotlib",
                    "5. Introduction to Machine Learning",
                    "6. Work on Simple Datasets",
                ]
            elif experience == "Intermediate":
                roadmap = [
                    "1. Deepen Your Understanding of Machine Learning Algorithms",
                    "2. Learn about Data Wrangling Techniques",
                    "3. Explore Advanced Visualization Tools (Seaborn, Plotly)",
                    "4. Work on Real-World Datasets",
                    "5. Study Statistics and Probability for Data Science",
                    "6. Build and Deploy Machine Learning Models",
                ]
            elif experience == "Advanced":
                roadmap = [
                    "1. Contribute to Open Source Data Science Projects",
                    "2. Explore Deep Learning Frameworks (TensorFlow, PyTorch)",
                    "3. Work with Big Data Technologies (Hadoop, Spark)",
                    "4. Specialize in a Domain (NLP, Computer Vision)",
                    "5. Optimize Models and Conduct A/B Testing",
                    "6. Publish Your Findings and Models",
                ]

        elif specialization == "Game Development":
            if experience == "Beginner":
                roadmap = [
                    "1. Learn Python Basics",
                    "2. Understand Game Design Principles",
                    "3. Learn Pygame Library",
                    "4. Build a Simple Game (e.g., Pong or Snake)",
                    "5. Explore Game Art and Sound Basics",
                    "6. Share Your Game with Friends for Feedback",
                ]
            elif experience == "Intermediate":
                roadmap = [
                    "1. Master Pygame and Explore Other Game Engines (Unity, Unreal)",
                    "2. Learn about Game Physics and AI",
                    "3. Work on More Complex Games (2D and 3D)",
                    "4. Understand Game Monetization Strategies",
                    "5. Collaborate with Artists and Designers",
                    "6. Publish Your Game on Platforms (Steam, itch.io)",
                ]
            elif experience == "Advanced":
                roadmap = [
                    "1. Contribute to Open Source Game Projects",
                    "2. Learn Advanced Game Development Techniques (Networking, VR)",
                    "3. Explore Game Marketing and Community Building",
                    "4. Create a Portfolio of Your Work",
                    "5. Attend Game Jams and Competitions",
                    "6. Network with Industry Professionals and Seek Job Opportunities",
                ]
        else:
            # Show a warning if no specialization is selected
            messagebox.showwarning("Selection Error", "Please select a specialization.")
            return

        # Clear the text area and insert the new roadmap
        self.roadmap_text.delete(1.0, tk.END)  # Clear existing text
        for line in roadmap:
            self.roadmap_text.insert(tk.END, line + "\n")  # Insert each line of the roadmap

    def reset_selections(self):
        # Reset the selections to default values
        self.experience_var.set("Beginner")  # Reset experience level to Beginner
        self.specialization_var.set("")  # Clear specialization selection
        self.roadmap_text.delete(1.0, tk.END)  # Clear the roadmap text area

# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = PythonLearningRoadmapApp(root)  # Instantiate the application class
    root.mainloop()  # Start the GUI event loop