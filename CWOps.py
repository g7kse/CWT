import pandas as pd

class CSVLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.csv_data = None

    def load_csv(self):
        try:
            # Load the CSV file
            self.csv_data = pd.read_csv(self.file_path, skiprows=8, header=None)

            # Remove any completely empty columns
            self.csv_data.dropna(axis=1, how='all', inplace=True)

            # Set proper column names based on the actual number of columns
            num_columns = self.csv_data.shape[1]
            if num_columns == 9:
                self.csv_data.columns = ["Paid Thru", "Callsign", "Number", "First or Nick Name", "Last Name", "DXCC", "W/VE", "Blog or Website", "Biography"]
            elif num_columns == 11:
                self.csv_data.columns = ["Paid Thru", "Callsign", "Number", "First or Nick Name", "Last Name", "DXCC", "W/VE", "Blog or Website", "Biography", "Extra Column 1", "Extra Column 2"]
            else:
                raise ValueError(f"Unexpected number of columns: {num_columns}")

            print("CSV file loaded and cleaned successfully!")
        except FileNotFoundError:
            print("Error: CSV file not found. Please ensure the file is in the correct directory.")
        except Exception as e:
            print(f"Error: Failed to load CSV file: {e}")

    def lookup_callsign(self, callsign):
        if not callsign.strip():
            print("Input Error: Please enter a valid callsign.")
            return

        # Search for the callsign in the DataFrame
        result = self.csv_data[self.csv_data["Callsign"].str.strip().str.upper() == callsign.upper()]

        if not result.empty:
            # Get the membership number and name from the result
            membership_number = result["Number"].values[0]
            first_name = result["First or Nick Name"].values[0]
            last_name = result["Last Name"].values[0]
            print(f"Name: {first_name} {last_name}, Membership Number: {membership_number}")
        else:
            print("Callsign not found.")

def main():
    file_path = 'Shareable CWops data - Roster.csv'  # Change this to your CSV file path
    csv_loader = CSVLoader(file_path)
    csv_loader.load_csv()

    while True:
        callsign = input("Enter a callsign to lookup (or type 'exit' to quit): ")
        if callsign.lower() == 'exit':
            break
        csv_loader.lookup_callsign(callsign)

if __name__ == "__main__":
    main()
