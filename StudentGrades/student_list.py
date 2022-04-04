import sys
import csv

def load_csv_data(filename: str) -> list:
    file = open(filename)
    info = csv.reader(file)
    return list(info)

def get_student_list(data: list) -> set:
    IDs = []
    for student in data:
        IDs.append(student[0])
    IDs = set(IDs)
    IDs = list(IDs)
    IDs.sort()
    return IDs

def main():
    allData = load_csv_data(sys.argv[1])
    students = get_student_list(allData)
    print(students[:5])

if __name__ == "__main__":
    main()