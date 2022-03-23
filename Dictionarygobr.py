from tkinter import W
import passage01
import passage02
import string

def split(strings:str) -> list:
    """
    We start splitting the full text into individual words (or more specifically splitting on whitespace i.e. spaces and new lines)

    Next we begin looping over each word in our new list
    First we set all words to all lower case to make sure capital letters make words count as a different word (Example: Give and give would be considered different)
    We then create a new list for letters

    After this we begin looping over each letter in each word
    We then check to make sure that the letter isn't actually puncuation
    If it passes this check it is added to our letter list
    The reason we do this is to ensure that things that end with commas are not counted different (Example: Give, and Give would be counted different without this)

    We then make our word variable a blank string and loop over each letter to add it back and recreate the word
    Finally we append our lower-case no punction word to our finished list

    Once the looping is finished it will return finishList containing all the words

    ***There is an issue with this code that words like "it's" and "its" will be counted as the same I do not want to fix this
    """
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

def dictionary(wordList:list) -> dict:
    """
    We start by creating a new dictionary to store each word
    We then loop over each word in our word list and check if it is in the dictionary already

    If it is not in the dictionary already it will create a new key to the dictionary and set the value to 1
    However if it is already in the dictionary it will simply just add 1 to the current value of that word

    Finally we will return the dictionary
    """
    wordDict = {}
    for word in wordList:
        if word not in wordDict:
            wordDict[word] = 1
        else:
            wordDict[word] += 1
    return wordDict

def findCommon(wordDict: dict) -> list:
    """
    ***THIS FUNCTION IS A COMPLETE MESS AND THERE ARE MUCH MUCH BETTER WAYS OF DOING THIS BUT I AM LAZY***

    In this function we start by setting up a store list and a storeword list
    This lists will store the count of the words (store)
    And the actual word itself (storeword)

    We then begin to loop over each word in the word dictionary
    As well as this we loop over each item in our store list 

    We check if the current item in the store list has a smaller number than the count of the word we are on (example: the value of the store is 10 and we are looking at the word "the" with a value of 20)
    If this is true we change the value of store and change which word is stored in storeword

    Finally we return storeword
    """
    store = [0,0,0,0,0]
    storeword = ["","","","",""]
    for word in wordDict:
        for num in range(len(store)):
            if wordDict[word] > store[num] and word not in storeword:
                store[num] = wordDict[word]
                storeword[num] = word
    return storeword
            

def main():
    wordList = split(passage01.passage01)
    wordDict = dictionary(wordList)
    finalList = findCommon(wordDict)
    print(finalList)

if __name__ == "__main__":
    main()