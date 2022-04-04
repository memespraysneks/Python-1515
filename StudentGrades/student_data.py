import sys
import csv

def load_csv_data(filename: str) -> list:
    file = open(filename)
    info = csv.reader(file)
    return list(info)

def get_student_list(data: list) -> list:
    IDs = []
    for student in data:
        IDs.append(student[0])
    IDs = set(IDs)
    IDs = list(IDs)
    IDs.sort()
    return IDs

def get_student_data(csv_data: list, student_id: str) -> list:
    for course in csv_data:
        if course[0] == student_id:
            print(course)

def main():
    try:
        allData = sys.argv[1]
        StudentID = sys.argv[2]
    except:
        print("\nEither the file name or student ID is missing please try again!\n")
        return
    try:
        allData = load_csv_data(allData)
    except:
        print(f"\nFile {sys.argv[1]} doesn't exist please try again!\n")
        return
    get_student_data(allData, StudentID)
    

if __name__ == "__main__":
    main()