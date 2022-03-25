def getinput():
    selection = input("What letter would you like to chose? ")
    selection = selection.lower().strip()
    if selection.isalpha():
        return selection
    else:
        print("Please enter a valid letter! ")
        getinput()

def split(file):
    return file.split()


def fileopener(file):
    file = open(file, "r")
    file = file.read()
    file = split(file)
    return file

def main():
    file = fileopener("File I\O\\new_words.txt")
    selection = getinput()
    count = 0
    for word in file:
        if word[0].lower() == selection:
            count += 1
    print(count)



if __name__ == "__main__":
    main()
