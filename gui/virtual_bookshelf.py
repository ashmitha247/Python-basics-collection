import tkinter as tk
from tkinter import messagebox, Scrollbar, StringVar, font

class VirtualBookshelf:
    def __init__(self, root):
        self.root = root
        self.root.title("Virtual Bookshelf")
        self.root.geometry("800x500")  # Adjusted window size for better layout
        self.root.configure(bg="#f7f7f7")

        # Create a title label
        self.title_label = tk.Label(root, text="Virtual Bookshelf", font=("Arial", 20, "bold"), bg="#f7f7f7", fg="#333")
        self.title_label.pack(pady=20)

        # Create input fields for book title and author
        self.title_label = tk.Label(root, text="Book Title:", bg="#f7f7f7", font=("Arial", 12))
        self.title_label.pack(pady=5)
        self.title_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.title_entry.pack(pady=5)

        self.author_label = tk.Label(root, text="Author:", bg="#f7f7f7", font=("Arial", 12))
        self.author_label.pack(pady=5)
        self.author_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.author_entry.pack(pady=5)

        # Create a dropdown for rating
        self.rating_label = tk.Label(root, text="Rating (1-5):", bg="#f7f7f7", font=("Arial", 12))
        self.rating_label.pack(pady=5)
        self.rating_var = StringVar(root)
        self.rating_var.set("1")  # Default value
        self.rating_menu = tk.OptionMenu(root, self.rating_var, "1", "2", "3", "4", "5")
        self.rating_menu.config(font=("Arial", 12), bg="#e0e0e0")
        self.rating_menu.pack(pady=5)

        # Create an input field for review
        self.review_label = tk.Label(root, text="Review:", bg="#f7f7f7", font=("Arial", 12))
        self.review_label.pack(pady=5)
        self.review_entry = tk.Text(root, height=4, width=40, font=("Arial", 12))
        self.review_entry.pack(pady=5)

        # Create buttons to add and remove books
        self.button_frame = tk.Frame(root, bg="#f7f7f7")
        self.button_frame.pack(pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Book", command=self.add_book, bg="#4CAF50", fg="white", font=("Arial", 12))
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(self.button_frame, text="Remove Selected Book", command=self.remove_book, bg="#F44336", fg="white", font=("Arial", 12))
        self.remove_button.pack(side=tk.LEFT, padx=10)

        # Create a Listbox to display book information
        self.bookshelf_display = tk.Listbox(root, height=15, width=70, font=("Arial", 12), bg="#ffffff", selectbackground="#c0e0ff", selectforeground="#000000")  # Custom styles
        self.bookshelf_display.pack(pady=10)

        # Create a Scrollbar for the Listbox
        self.scrollbar = Scrollbar(root, command=self.bookshelf_display.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bookshelf_display.config(yscrollcommand=self.scrollbar.set)

        # Initialize an empty list to store books
        self.books = []

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()
        rating = self.rating_var.get()
        review = self.review_entry.get("1.0", tk.END).strip()  # Get the review text

        # Check if title and author fields are filled
        if not title or not author:
            messagebox.showwarning("Input Error", "Please enter both title and author.")
            return

        # Create book info string
        book_info = f"Title: {title}, Author: {author}, Rating: {rating}, Review: {review if review else 'No Review'}"

        # Add the book to the list and update the Listbox
        self.books.append(book_info)
        self.bookshelf_display.insert(tk.END, book_info)

        # Clear the input fields
        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)
        self.review_entry.delete("1.0", tk.END)  # Clear the review text

    def remove_book(self):
        try:
            selected_index = self.bookshelf_display.curselection()[0]
            self.bookshelf_display.delete(selected_index)
            del self.books[selected_index]  # Remove the book from the list
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a book to remove.")

if __name__ == "__main__":
    root = tk.Tk()
    virtual_bookshelf = VirtualBookshelf(root)
    root.mainloop()