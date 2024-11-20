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
            self.result_label.config(text="Call
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

# Create the main application window
if __name__ == "__main__":
    root = Tk()
    app = YourApplicationClass(root)
    root.mainloop()
