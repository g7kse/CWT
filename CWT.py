import pandas as pd
import customtkinter as ctk
from tkinter import Tk, messagebox, ttk

class YourApplicationClass:
    def __init__(self, master):
        self.master = master
        self.master.title("CSV Loader App")
        self.master.geometry("600x500")
        self.master.configure(bg="black")

        # Create a frame for the Treeview and scrollbar
        self.frame = ctk.CTkFrame(master)
        self.frame.pack(pady=10)

        # Create a Treeview widget
        self.tree = ttk.Treeview(self.frame, columns=("Callsign", "Number", "First or Nick Name"), show="headings")
        self.tree.heading("Callsign", text="Callsign")
        self.tree.heading("Number", text="Number")
        self.tree.heading("First or Nick Name", text="First or Nick Name")
        self.tree.pack(side="left")

        # Add a scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.frame, orientation="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Create a button to load CSV
        self.load_button = ctk.CTkButton(master, text="Load CSV", command=self.load_csv)
        self.load_button.pack(pady=20)

        # Entry for callsign lookup
        self.callsign_entry = ctk.CTkEntry(master)
        self.callsign_entry.pack(pady=10)

        # Button to perform lookup
        self.lookup_button = ctk.CTkButton(master, text="Lookup Callsign", command=self.lookup_callsign)
        self.lookup_button.pack(pady=10)
        
        # Bind the Return key to the lookup_callsign method
        self.callsign_entry.bind("<Return>", self.on_return)

        # Label to display lookup results
        self.result_label = ctk.CTkLabel(master, text="", bg_color="black", text_color="white")
        self.result_label.pack(pady=10)

    def on_return(self, event):
        """Method to handle Return key press."""
        self.lookup_callsign()

    def load_csv(self):
        try:
            # Open file dialog to select the CSV file
            file_path = 'Shareable CWops data - Roster.csv'  # Change this line if you want to use a file dialog
            self.csv_data = pd.read_csv(file_path, skiprows=8, header=None)

            # Print the structure of the DataFrame for debugging
            print(self.csv_data.head())
            print(self.csv_data.columns)

            # Remove any completely empty columns
            self.csv_data.dropna(axis=1, how='all', inplace=True)

            # Check the number of columns
            num_columns = self.csv_data.shape[1]
            print(f"Number of columns in CSV: {num_columns}")

            # Set proper column names based on the actual number of columns
            if num_columns == 9:
                self.csv_data.columns = ["Paid Thru", "Callsign", "Number", "First or Nick Name", "Last Name", "DXCC", "W/VE", "Blog or Website", "Biography"]
            elif num_columns == 11:
                self.csv_data.columns = ["Paid Thru", "Callsign", "Number", "First or Nick Name", "Last Name", "DXCC", "W/VE", "Blog or Website", "Biography", "Extra Column 1", "Extra Column 2"]
            else:
                raise ValueError(f"Unexpected number of columns: {num_columns}")

            # Clear the Treeview
            self.tree.delete(*self.tree.get_children())

            # Insert cleaned data into the Treeview
            for index, row in self.csv_data.iterrows():
                self.tree.insert("", "end", values=(row["Callsign"], row["Number"], row["First or Nick Name"]))

            messagebox.showinfo("Success", "CSV file loaded and cleaned successfully!")

        except FileNotFoundError:
            messagebox.showerror("Error", "CSV file not found. Please ensure the file is in the same directory.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load CSV file: {e}")

    def lookup_callsign(self):
        callsign = self.callsign_entry.get().strip()
        if not callsign:
            messagebox.showwarning("Input Error", "Please enter a callsign.")
            return

        # Search for the callsign in the DataFrame
        result = self.csv_data[self.csv_data["Callsign"].str.strip().str.upper() == callsign.upper()]

        if not result.empty:
            # Get the membership number and name from the result
            membership_number = result["Number"].values[0]
            first_name = result["First or Nick Name"].values[0]
            last_name = result["Last Name"].values[0]
            # Display the result in the label
            self.result_label.config(text=f"Name: {first_name} {last_name}, Membership Number: {membership_number}")
        else:
            self.result_label.config(text="Callsign not found.")
    def lookup_callsign(self):
        callsign = self.callsign_entry.get().strip()
        if not callsign:
            messagebox.showwarning("Input Error", "Please enter a callsign.")
            return

        # Search for the callsign in the DataFrame
        result = self.csv_data[self.csv_data["Callsign"].str.strip().str.upper() == callsign.upper()]

        if not result.empty:
            # Get the membership number and name from the result
            membership_number = result["Number"].values[0]
            first_name = result["First or Nick Name"].values[0]
            last_name = result["Last Name"].values[0]
            # Display the result in the label
            self.result_label.configure(text=f"Name: {first_name} {last_name}, Membership Number: {membership_number}")
        else:
            self.result_label.configure(text="Callsign not found.")

# Create the main application window
if __name__ == "__main__":
    root = Tk()
    app = YourApplicationClass(root)
    root.mainloop()
