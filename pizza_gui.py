# TODO: Complete GUI Integration
#
# Current Status:
# - GUI only functions on initial main.py call
# - Not properly integrated into overall application flow

import tkinter as tk
from tkinter import ttk
from data_analyzer import analyze_best_prices
from config import OUTPUT_FILE

class PizzaPriceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Pizza Price Comparison")
        self.root.geometry("800x600")

        # Create main frames
        self.create_frames()
        self.create_input_section()
        self.create_results_section()

    def create_frames(self):
        # Input frame
        self.input_frame = ttk.Frame(self.root, padding="10")
        self.input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Results frame
        self.results_frame = ttk.Frame(self.root, padding="10")
        self.results_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    def create_input_section(self):
        # Pizza type label and entry
        ttk.Label(self.input_frame, text="Pizza Type:").grid(row=0, column=0, padx=5)
        self.pizza_entry = ttk.Entry(self.input_frame, width=30)
        self.pizza_entry.grid(row=0, column=1, padx=5)

        # Button frame for better spacing
        button_frame = ttk.Frame(self.input_frame)
        button_frame.grid(row=0, column=2, padx=5)

        # Search button
        ttk.Button(button_frame, text="Search",
                   command=self.search_pizzas).grid(row=0, column=0, pady=5)

        # Reset button
        ttk.Button(button_frame, text="Reset",
                   command=self.reset_form).grid(row=0, column=1, padx=5, pady=5)

        # Status label
        self.status_label = ttk.Label(self.input_frame, text="")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=5)

    def create_results_section(self):
        # Create treeview for results
        columns = ("Restaurant", "Pizza", "Price")
        self.tree = ttk.Treeview(self.results_frame, columns=columns, show="headings")

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=200)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        # Grid the tree and scrollbar
        self.tree.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

    def search_pizzas(self):
        pizza_type = self.pizza_entry.get()
        if not pizza_type:
            self.status_label.config(text="Please enter a pizza type", foreground="red")
            return

        try:
            # Clear previous results
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Analyze prices
            results = analyze_best_prices(OUTPUT_FILE, pizza_type)

            # Insert results into treeview
            for _, row in results.iterrows():
                self.tree.insert("", "end", values=list(row))

            self.status_label.config(text=f"Found {len(results)} results",
                                     foreground="green")

        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", foreground="red")

    def reset_form(self):
        # Clear entry field
        self.pizza_entry.delete(0, tk.END)

        # Clear treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Clear status message
        self.status_label.config(text="")

# Main function (outside the class)
def main():
    root = tk.Tk()
    app = PizzaPriceGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()