from tkinter import W
import passage01
import passage02
import string

def split(strings):
    wordList = strings.split()
    finishList = []
    for word in wordList:
        word = word.lower()
        letters = []
        for letter in word:
            if letter not in list(string.punctuation):
                letters.append(letter)
        word = ""
        for letter in letters:
            word += letter
        finishList.append(word)
    return(finishList)

def dictionary(wordList):
    wordDict = {}
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    return wordDict

def findCommon(wordDict):
    store = [0,0,0,0,0]
    storeword = ["","","","",""]
    for word in wordDict:
        for num in range(len(store)):
            token = 0
            if wordDict[word] > store[num] and token == 0 and word not in storeword:
                store[num] = wordDict[word]
                storeword[num] = word
                token = 1
    return storeword
            

def main():
    wordList = split(passage01.passage01)
    wordDict = dictionary(wordList)
    finalList = findCommon(wordDict)
    print(finalList)

if __name__ == "__main__":
    main()