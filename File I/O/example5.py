import string

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

def hasPunction(words):
    listOfWords = []
    count = 0
    for word in words:
        token = 0
        for i in word:
            if i in string.punctuation and token == 0:
                listOfWords.append(word)
                count += 1
                token = 1
            
    stringOfWords = ""
    for i in listOfWords:
        stringOfWords += i
    print(f"There are {count} words with punctuation, they are:\n{stringOfWords}")

def findAndWrite(wordList):
    for letter in string.ascii_lowercase:
        specificLetterList = fourLetters(letter, wordList)
        fileWriter(letter, specificLetterList)

def fourLetters(letter, wordList):
    newList = []
    for word in wordList:
        if word.lower()[0] == letter:
            newList.append(word)
    return newList

def fileWriter(letter, wordList):
    with open(f"{letter}_words.txt", "x") as file:
        file.write(f"{wordList}")


def main():
    file = fileOpener("File I\O\\new_words.txt")
    findAndWrite(file)
    
    

if __name__ == "__main__":
    main()
