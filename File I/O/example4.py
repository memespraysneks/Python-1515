def fileOpener(selection):
    with open(selection, "r") as file:
        file = file.readlines()
        return file

def wordLength(wordList):
    lengthDictionary = {}
    for i in wordList:
        if len(i)-1 not in lengthDictionary:
            lengthDictionary[len(i)-1] = 1
        else:
            lengthDictionary[len(i)-1] += 1
    return lengthDictionary

def main():
    file = fileOpener("File I\O\\new_words.txt")
    lengths = wordLength(file)
    print(lengths.items())
    print("%-10s %0s" % ("Length", "Count"))
    for item in lengths.items():
        print("%-10s %0s" % (item[0], item[1]))
    

if __name__ == "__main__":
    main()
