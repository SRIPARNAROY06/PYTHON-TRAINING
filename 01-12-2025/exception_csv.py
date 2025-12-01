import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: You do not have permission to read '{filename}'.")
    except csv.Error:
        print(f"Error: The file '{filename}' is not a valid CSV format.")


read_csv_file("data.csv")
