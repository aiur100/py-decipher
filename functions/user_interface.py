import os
import platform
from classes.CipherWord	import CipherWord
from functions.decryption_tools import getSessionStart

decrypter   = """   
  _______  __________  _____  ______
  / __/ _ )/ ___/ _ \ \/ / _ \/_  __/
 _\ \/ _  / /__/ , _/\  / ___/ / /   
/___/____/\___/_/|_| /_/_/    /_/    
                                     """
menu 		= """ 
1. View letter counts\n 
2. View word counts \n 	
3. View entire text in current \n 
4. View entire text (original) \n 
5. Replace string (word). \n 
6. Apply changes \n
7. View word details \n
8. View altered word details \n
9. View decoded word details\n
10. Replace a character \n
11. How many words have been decoded?\n
12. Show words that are almost decoded\n
13. Write decoded ciphers to file\n
					"""
loadFile 	= "Please enter the file to process: "
divider		= "==================================="


## displays the decrypter header
## along with platform that the program
## is running on. 
def displayAppHeader():
	print(decrypter)
	print("Running on: ",platform.system())
	print("Session-Time-Stamp, all files will be saved with this stamp: ",getSessionStart())

## TODO - make a function that prints the menu that appears after a file is loaded
## in the terminal
def displayMenu():
	displayAppHeader()
	print(divider)
	print(menu)
	print(divider)
	print("Enter Option Number: ")

## clears the screen
def clearScreen():
	if platform.system() == "Windows":
		os.system('cls')
	else:
		os.system('clear')		

##displays the prompt to the user to enter file
def displayLoadFilePrompt():
	displayAppHeader()
	print(divider)
	print(loadFile)	

## loads the file at the given pathToFile
## and returns its contents
def loadFileAndReturnContents(pathToFile):
	file   = open(pathToFile,"r")
	return file.read()

##displays letter counts
def displayLetterCounts(listOfLetterCountTuples):
	length = len(listOfLetterCountTuples)
	for i in range(1,length):
		print(listOfLetterCountTuples[i][0],": ",listOfLetterCountTuples[i][1])

##displays word counts
##@param <list-of-tuples>
def displayWordCounts(listOfWordCountTuples):
	length = len(listOfWordCountTuples)
	for i in range(0,length):
		print(listOfWordCountTuples[i][0],": ",listOfWordCountTuples[i][1])

def readUserInputForStringChange():
	old = input("Please enter the encrypted string you want to change (can be a letter): ")	
	new = input("Please enter what string to change that encrypted string to: ")
	return (old,new)

def displayCipherWords(dictOfCipherWords):
	for key in dictOfCipherWords:
		print(divider)
		print("Orig-Word:",key,"Changes:",dictOfCipherWords[key].changes,end='')
		print("\n")
		print("Word-Count:",dictOfCipherWords[key].count,"Decoded:",dictOfCipherWords[key].decoded,end='')
		print("\n")
		print("Current-Word:")
		dictOfCipherWords[key].printChanges()
		print(divider)




