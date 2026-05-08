
import csv

def import_file():
    file_path = r'c:\users\dominus\code\csv-data-cleaner\input\leads-100.csv'

    try:
        with open(file_path, 'r', newline="") as csv_file:
            read_csv = csv.reader(csv_file)

            # Move the following section to a new function later
            # Use loop to transfer csv_file to a variable that can survive
            # outside the 'with'
            for row in read_csv:
                print(row)
    except FileNotFoundError:
        print("Error. File not found. Please check your file name and path.")
        read_csv = ""

    


def main():
    import_file()
    return

if __name__ == "__main__":
    main()