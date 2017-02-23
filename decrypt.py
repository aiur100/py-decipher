from functions.decryption_tools import countLettersInText
from functions.decryption_tools import countWordsInText
from functions.user_interface 	import displayMenu
from functions.user_interface 	import displayLoadFilePrompt
from functions.user_interface 	import loadFileAndReturnContents
from functions.user_interface 	import clearScreen
from functions.user_interface	import displayLetterCounts
from functions.user_interface	import displayWordCounts
from functions.user_interface   import readUserInputForStringChange
from functions.decryption_tools import setChange
from functions.decryption_tools import getChangeTuples
from functions.decryption_tools import applyChanges
from classes.CipherWord			import CipherWord
from functions.decryption_tools import setListOfCipherWords
from functions.user_interface   import displayCipherWords
from functions.decryption_tools import getAlteredCiphers
from functions.decryption_tools import getDecodedCiphers
from functions.decryption_tools import checkAllWordsForLetters
from functions.decryption_tools import getAlmostDone
from functions.decryption_tools	import writeDecodedCiphersToFile
import time
import sys

clearScreen()
## the key that keeps the program running.
running 		= True

displayLoadFilePrompt()

## user input of file path.
pathToFile 		= input()

##loading file
fileAsString 	= loadFileAndReturnContents(pathToFile)

##lower case string used for counting letters, since 
##I don't want A and a to be counted separately. 
lowerCaseString = fileAsString
lowerCaseString.lower()

##remove new line from strings to match words easily.
removeNewLine   = fileAsString
removeNewLine   = removeNewLine.replace("\n","")
removeNewLine.lower()

##parsing file 
letterCount		= countLettersInText(removeNewLine.lower())
wordCount		= countWordsInText(lowerCaseString)
cipherWords     = setListOfCipherWords(wordCount)

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

clearScreen()

while(running):
	displayMenu()
	choice      = input()

	clearScreen()
	if RepresentsInt(choice) is False:
		print("Incorrect entry, reloading...")
		import time
		time.sleep(3)
		continue

	choice = int(choice)

	if choice 	== 1:
		displayLetterCounts(letterCount)
	elif choice == 2:
		displayWordCounts(wordCount)
	elif choice == 3:
		print(fileAsString)
	elif choice == 4:
		print(fileAsString)
	elif choice == 5:
		changes = readUserInputForStringChange()
		before  = len(cipherWords)
		cipherWords = setChange(changes,cipherWords)
		if before > len(cipherWords):
			print("A word was found and removed")
		print(getChangeTuples())
	elif choice == 6:
		print("Applying changes...")
		fileAsString = applyChanges(fileAsString)
	elif choice == 7:
		displayCipherWords(cipherWords)
	elif choice == 8:
		displayCipherWords(getAlteredCiphers())
	elif choice == 9:
		displayCipherWords(getDecodedCiphers())
	elif choice == 10:
		original = input("Enter a character: ")
		replace = input("Enter a replacement: ")
		if len(original) == 1 and len(replace) == 1:
			cipherWords = checkAllWordsForLetters([(original,replace)],cipherWords)
	elif choice == 11:
		print("Amount Decoded so far: ",len(getDecodedCiphers()))
	elif choice == 12:
		displayCipherWords(getAlmostDone())
	elif choice == 13:
		writeDecodedCiphersToFile()
			
					




	choice 	   = input("Continue? [y|n]: ")
	if  choice == "n":
		running = False
	else:
		clearScreen()	






