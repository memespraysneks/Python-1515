def getinput():
    selection = input("What letter would you like to chose? ")
    selection = selection.lower().strip()
    if selection.isalpha():
        return selection
    else:
        print("Please enter a valid letter! ")
        getinput()

def nameCheck(words):
    name = input("What is your name? ").lower().strip()
    count = 0
    firstThree = []
    for word in words:
        if name in word:
            count += 1
            if len(firstThree) < 3:
                firstThree.append(word)
    try:
        print(f"There are {count} words that contain {name} the first three are\n{firstThree[0]}{firstThree[1]}{firstThree[2]}")
    except:
        print(f"There are {count} words that contain {name}")
def fileOpener(selection):
    with open(selection, "r") as file:
        file = file.readlines()
        return file

def main():
    file = fileOpener("File I\O\\new_words.txt")
    nameCheck(file)

if __name__ == "__main__":
    main()
