import sys
import datetime
import os

def expiredFiles(file, date):
    expiredFiles = []
    for item in file:
        time = convert(os.path.getmtime(item))
        if time < date:
            print("File Path:",item, "Last Modified:",time, "Bytes:",os.path.getsize(item))
            expiredFiles.append(item)
    return expiredFiles

def convert(timestamp):
    return datetime.date.fromtimestamp(timestamp)

def getdirectory(directory):
    try:
        tempstore = os.listdir(directory)
        finalFileList = []
        for item in tempstore:
            currentFile = os.path.join(directory, item)
            if os.path.isdir(currentFile):
                finalFileList = finalFileList + getdirectory(currentFile)
            else:
                finalFileList.append(currentFile)
    except:
        print("You need to input a proper directory please try again!")
    return finalFileList

def getdate(date):
    try: 
        tempdate = date.split("-")
        numbers = []
        for i in tempdate:
            numbers.append(int(i))
        return numbers
    except:
        print("You need to put in a date please try again!")

def main():
    allFiles = getdirectory(sys.argv[1])
    datesTemp = getdate(sys.argv[2])
    expiryDate = datetime.date(datesTemp[0],datesTemp[1],datesTemp[2])
    print("Files to be deleted\n")
    expiredList = expiredFiles(allFiles, expiryDate)
    answer = input("\nWould you like to delete these Files? ")
    if answer.lower().strip() == "yes":
        for file in expiredList:
            print(file)
            if os.path.exists(file):
                os.remove(file)
            else:
                print("The file does not exist")
        for directory in os.listdir(sys.argv[1]):
            directory = os.path.join(sys.argv[1], directory)
            if not os.listdir(directory):
                os.rmdir(directory)
                print("Deleting", os.path.abspath(directory))

if __name__ == "__main__":
    main()

