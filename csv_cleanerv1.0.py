
import csv

def import_file():
    #------------------------
    # path changes with computer. fix this
    #------------------------
    file_path = r'\input\leads-100.csv'

    try:
        with open(file_path, 'r', newline="") as csv_file:
            read_csv = csv.reader(csv_file)

            # Move the following section to a new function later
            # Use loop to transfer csv_file to a variable that can survive
            # outside the 'with'
            #for row in read_csv:
            #    print(row)
    except FileNotFoundError:
        print("Error. File not found. Please check your file name and path.")
        read_csv = ""
    return read_csv

def print_file(read_csv):
    for row in read_csv:
        print(row)
    return
    


def main():
    read_csv = import_file()
    print_file(read_csv)
    return

if __name__ == "__main__":
    main()