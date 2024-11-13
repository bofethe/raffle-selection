import pandas as pd
import tkinter as tk
from tkinter import ttk

# Initialize the main window
root = tk.Tk()
root.title("Raffle Selection")
root.geometry("400x400")

note_label = tk.Label(root, text="This GUI randomly selects n records from an xlsx\n based on a unique field.", justify="left")
note_label.pack(pady=10)

# Global variable to hold the loaded DataFrame
df = None

# File path variables
path_label = tk.Label(root, text="Enter path to name list:")
path_label.pack(pady=5)
path_entry = tk.Entry(root, width=30)
path_entry.pack(pady=5)

# Unique field variables
unique_fields_label = tk.Label(root, text="Enter unique field name:")
unique_fields_label.pack(pady=5)
unique_fields_entry = tk.Entry(root, width=30)
unique_fields_entry.pack(pady=5)

# Sample size variables
n_label = tk.Label(root, text="Enter selection size:")
n_label.pack(pady=5)
n_entry = tk.Entry(root, width=30)
n_entry.pack(pady=5)

# Output widget
output_text = tk.Text(root, width=40, height=5, wrap="word")
output_text.pack(pady=10)

# Show output
def display_message(message):
    output_text.insert(tk.END, message + "\n")
    output_text.see(tk.END)  # Automatically scroll to the bottom

# Load df
def load_data():
    output_text.delete(1.0, tk.END)
    global df
    path = path_entry.get()
    try:
        # Read data from the provided Excel path
        df = pd.read_excel(path)
        display_message(f"Data loaded successfully. \nNumber of records: {df.shape[0]}")
    except Exception as e:
        display_message(f"Error loading data: {e}")

# Make a selection
def make_selection():
    output_text.delete(1.0, tk.END)
    
    # Check if df is loaded
    global df
    if df is None:
        display_message("Please load data first.")
        return

    unique_field = unique_fields_entry.get()
    try:
        n = int(n_entry.get())
    except ValueError:
        display_message("Selection size must be a number.")
        return

    try:
        # Drop dups
        df.drop_duplicates(subset=[unique_field], inplace=True)

        # Select the sample rows
        selected_rows = df.sample(n)
        selected_names = selected_rows[unique_field].to_list()  # Extract only names
        display_message(f"Selected member(s):\n\t{', '.join(selected_names)}")

        # Drop selected rows from the df
        df.drop(selected_rows.index, inplace=True)
        display_message(f"Remaining records after selection: {df.shape[0]}")

    except Exception as e:
        display_message(f"Error: {e}")

# Button to load data
load_button = tk.Button(root, text="Load Data", command=load_data)
load_button.pack(pady=5)

# Button to trigger selection
select_button = tk.Button(root, text="Make a Selection", command=make_selection)
select_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
