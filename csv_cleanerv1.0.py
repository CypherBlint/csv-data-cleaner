
import csv
import pathlib as pl

def import_file():
    project_home_path = pl.Path(__file__).parent
    file_path = project_home_path / "input"

    print("Files Available:\n")
    for f in file_path.iterdir():
        print(f.name)

    file_selection = input("\n\nPlease name the file you would like to run. ")
    file_path = file_path / file_selection

    try:
        with open(file_path, 'r', newline="") as csv_file:
            read_csv = list(csv.reader(csv_file))

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