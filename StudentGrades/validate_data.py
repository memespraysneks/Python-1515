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

def validate_data(input: list) -> list:
    file = input
    returnedFile = []
    for item in file:
        token = 0
        try:
            item[1] = item[1] + " " +  item[2]
            item.pop(2)
        except:
            print(f"warning: invalid data in record {item} discarded")
            token = 1
        try:
            if 0 <= int(item[2]) <= 100:
                item[2] = int(item[2])
            else:
                x = 10/0
        except:
            try:
                if item[2] == 'P' or item[2] == 'F' or item[2] == 'W':
                    pass
                else:
                    x = 10/0
            except:
                try:
                    print(f"warning: invalid data in record {item} discarded")
                    token = 1
                except:
                    pass
        try:
            item[3] = int(item[3])
        except:
            try:
                token = 1
                print(f"warning: invalid data in record {item} discarded")
            except:
                pass
        if len(item) != 5:
            print(f"warning: invalid data in record {item} discarded")
        elif token == 0:
            returnedFile.append(item)

    return returnedFile

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
    validate_data(allData)
    get_student_data(allData, StudentID)
    

if __name__ == "__main__":
    main()