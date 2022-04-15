# Import these packages first to start

from random import randint
import requests
#TODO Run 'pip install PyDictionary' to install PyDictionary.
from PyDictionary import PyDictionary
import time


# Get Random Word

# This URL consists of a words that are present in 'words' file which is present in Linux at this address '/usr/share/dict/'
url = 'https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words'


# Declaring variables

getData = requests.get(url)             # Getting data from URL
getText = getData.text                  # Converting the data in textual format
getWords = getText.split()              # Splitiing textual data in words
dictionary = PyDictionary()             # Creating an instance for PyDictionary
wordToPlay = ''
hiddenList = []


print("Let's Start The Game!!!")
time.sleep(2)
print("\nGetting A Word For You. \nPlease Wait...")
time.sleep(2)


# Function to get a random word from the URL

def getWordToPlay():
    validWord = False
    while(not validWord):
        getRandomNumber = randint(0, len(getWords))
        randomWord = getWords[getRandomNumber]
        if(randomWord[0].islower() and len(randomWord) > 2 and randomWord[-2] != "'"):
            validWord = True
            wordToPlay = randomWord
            return wordToPlay


# Function to get the definition of selected word by using PyDictionary

def wordDefinition(wordToPlay):
        wordToDefine = wordToPlay
        if(dictionary.meaning(wordToDefine, disable_errors = True)):
            print("Word is '" + wordToDefine + "'")
            definition = dictionary.meaning(wordToDefine)
            for key, value in definition.items():
                print(str(key) + ": " + str(value)[1:-1])


# Function to play game

def playGame():
    # Executing getWordToPlay() func & storing its value to variable 'wordToPlay'.
    wordToPlay = getWordToPlay()
    turns = len(wordToPlay) - 2         # 6 turns are assigned. (Customizable)
    hideIcon = "#"                      # To hide words
    usedLetters = []                    # To store used letters
    
    # Generating hiddenword with same length of generated word.
    hiddenWord = hideIcon * len(wordToPlay)
    
    print("\nHere Is Your Word")
    time.sleep(2)
    
    # Converting hidden word into List for further operations.
    hiddenList[0:] = hiddenWord

    # Loop will run continuously until either player gets out of turns or the word matches.
    while (hiddenWord != wordToPlay and turns != 0):
        
        # This will show how many turns are left.
        print("\nYou have {} TURNS left".format(turns))
        
        print("It will take only first letter as INPUT if multiple inputs given")
        
        # This will show all the letters which are already used.
        print("Used Letters: ",", ".join(usedLetters))

        # User-Input of letter to match with word
        findLetter = input("{}\nEnter a letter to find the word: ".format(hiddenWord)).lower()
        notNumeric = findLetter.isalpha()
        
        if notNumeric == True:
            findLetter = findLetter[0]
            usedLetters.append(findLetter)

        if notNumeric == False:
            print("\nWARNING: Please enter an ALPHABET.")
        elif findLetter in wordToPlay:
            for char in range(len(hiddenList)):
                if wordToPlay[char] == findLetter:
                    hiddenList[char] = findLetter
                    hiddenWord = "".join(hiddenList)
            if hiddenWord == wordToPlay:
                print("\nYou WON!!!\n")
                wordDefinition(wordToPlay)
                playAgain = input("\nDo You Want To PLAY AGAIN?\n(y/n)").lower()
                if playAgain[0] == 'y':
                    playGame()
        else:
            turns-=1
            if turns == 0:
                print("\nYou LOST!!!\n")
                wordDefinition(wordToPlay)
                playAgain = input("\nDo You Want To PLAY AGAIN?\n(y/n)").lower()
                if playAgain[0] == 'y':
                    playGame()
    
playGame()                              # Executing function to play game.