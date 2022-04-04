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
    specificData = []
    for course in csv_data:
        if course[0] == student_id:
            specificData.append(course)
            print(course)
    return specificData

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

def calculate_gpa(student_data: list) -> int:
    gradePoints = 0
    creditCount = 0
    for course in student_data:
        if course[2] == "W":
            pass
        elif course[2] == "P":
            gradePoints += 100*course[3]
            creditCount += course[3]
        elif course[2] == "F":
            gradePoints+= 0*course[3]
            creditCount += course[3]
        else:
            gradePoints += course[2]*course[3]
            creditCount += course[3]
    gpa = gradePoints/creditCount
    return round(gpa)

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
    allData = validate_data(allData)
    print()
    studentData = get_student_data(allData, StudentID)
    gpa = calculate_gpa(studentData)
    print(f"\n Student {StudentID} has GPA {gpa}\n")
    

if __name__ == "__main__":
    main()