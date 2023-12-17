import tkinter as tk
from tkinter import messagebox

class PizzaOrderingSystem:
    def __init__(self, root):
        # Initialize the main window
        self.main_window = root
        self.main_window.title("Pizza Ordering System")

        # Variables to store user selections and order information
        self.selected_pizza_size = tk.StringVar()
        self.selected_pizza_size.set("")  # Set an initial empty value
        self.selected_toppings = []  # Use a list for multiple selections
        self.order_summary_text = tk.StringVar()

        # First Window - Pizza Size Selection
        self.create_pizza_size_window()

    def create_pizza_size_window(self):
        # Destroy any existing windows (e.g., from a previous run)
        for widget in self.main_window.winfo_children():
            if isinstance(widget, tk.Toplevel):
                widget.destroy()

        # Use the main window for pizza size selection
        self.pizza_size_window = self.main_window
        self.pizza_size_window.title("Select Pizza Size")

        # Widgets for pizza size selection
        label_size = tk.Label(self.pizza_size_window, text="Select Pizza Size:")
        label_size.pack()

        # Radio buttons for pizza size options
        size_options = ["Small", "Medium", "Large"]
        for size in size_options:
            radio_button = tk.Radiobutton(self.pizza_size_window, text=size, variable=self.selected_pizza_size, value=size)
            radio_button.pack()

        # Button to proceed to toppings selection
        next_button = tk.Button(self.pizza_size_window, text="Next", command=self.open_toppings_window)
        next_button.pack()

        # Button to exit the program
        exit_button = tk.Button(self.pizza_size_window, text="Exit", command=self.exit_all_windows)
        exit_button.pack()

    def open_toppings_window(self):
        # Create a new window for toppings selection
        self.toppings_window = tk.Toplevel(self.main_window)
        self.toppings_window.title("Select Toppings")

        # Widgets for toppings selection
        label_toppings = tk.Label(self.toppings_window, text="Select Toppings:")
        label_toppings.pack()

        # Checkbuttons for toppings options
        toppings_options = ["Pepperoni", "Mushrooms", "Onions", "Sausage", "Olives", "Cheese"]
        for topping in toppings_options:
            checkbox = tk.Checkbutton(self.toppings_window, text=topping, variable=tk.BooleanVar(), onvalue=True, offvalue=False, command=lambda t=topping: self.toggle_topping(t))
            checkbox.pack()

        # Button to place the order
        order_button = tk.Button(self.toppings_window, text="Place Order", command=self.place_order)
        order_button.pack()

        # Button to exit the program
        exit_button = tk.Button(self.toppings_window, text="Exit", command=self.exit_all_windows)
        exit_button.pack()

    def toggle_topping(self, topping):
        # Toggle the topping in the list based on checkbox state
        if topping in self.selected_toppings:
            self.selected_toppings.remove(topping)
        else:
            self.selected_toppings.append(topping)

    def place_order(self):
        # Process the order and display a summary
        selected_size = self.selected_pizza_size.get()

        # Check if pizza size and toppings are selected
        if not selected_size or not self.selected_toppings:
            messagebox.showerror("Error", "Please select pizza size and toppings.")
            return

        # Create a summary string
        toppings_str = ', '.join(self.selected_toppings)
        order_summary_text = f"Order Summary:\nSize: {selected_size}\nToppings: {toppings_str}"
        self.order_summary_text.set(order_summary_text)

        # Display the order summary in a new window
        self.display_order_summary_window()

    def display_order_summary_window(self):
        # Create a new window to display the order summary
        self.summary_window = tk.Toplevel(self.main_window)
        self.summary_window.title("Order Summary")

        # Widget to display the order summary
        label_summary = tk.Label(self.summary_window, textvariable=self.order_summary_text)
        label_summary.pack()

        # Button to exit the program
        exit_button = tk.Button(self.summary_window, text="Exit", command=self.exit_all_windows)
        exit_button.pack()

    def exit_all_windows(self):
        # Destroy all Toplevel windows and the main window
        for window in self.main_window.winfo_children():
            if isinstance(window, tk.Toplevel):
                window.destroy()
        self.main_window.destroy()

# Main Application
root = tk.Tk()
app = PizzaOrderingSystem(root)
root.mainloop()
