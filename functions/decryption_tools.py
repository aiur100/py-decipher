from collections 		import Counter
from classes.CipherWord	import CipherWord
import csv
import time
import os.path
import re


## list of changes
listOfChanges 			= []
appliedChanges			= []
previousTextVersions 	= []
alteredCiphers			= {}
decodedCiphers			= {}
appliedCiphers			= []
letterChangesFileName   = "letterchanges"
decodedCipherFileName   = "decoded_words"
decryptedFileName		= "decrypted"
sessionStart			= time.strftime("%m_%d_%Y_%I_%M_%S")

def writeToFile(aListOfChanges,fileName):
	fileName 		= fileName+"_"+sessionStart+".csv"
	file_exists 	= os.path.isfile(fileName)
	with open(fileName, 'a') as csvfile:
		fieldnames 	= ['original', 'changed_to']
		writer 		= csv.DictWriter(csvfile, fieldnames=fieldnames)
		
		if not file_exists:
			writer.writeheader()  # file doesn't exist yet, write a header
		for i, v in enumerate(aListOfChanges):
			print("Writing: ",v)
			writer.writerow({'original': v[0], 'changed_to': v[1]})

def writeDecryptionTextToFile(textToWrite):
	fileName  = decryptedFileName+"_"+sessionStart+".txt"
	text_file = open(fileName, "w")
	text_file.write(textToWrite)
	text_file.close()
	print("Decrypted data written")			

## counts the occurence of each letter in text
## and returns tuples of each letter, and the letter's
## frequency count
def countLettersInText(text):
	textCounter      = Counter(text)
	return textCounter.most_common()

## counts the occurence of words in text
## and returns tuples of each word, and the word's
## frequency count
def countWordsInText(text):
	text            = text.replace("\n","")
	words 			= text.split(" ")
	wordsData 		= Counter(words)
	return wordsData.most_common()

## sets a change from old string to new string
def setChange(oldAndNewTuple,cipherWordList):
	##listOfChanges.append(oldAndNewTuple)
	key = oldAndNewTuple[0]
	if key in cipherWordList:
		cipherWordList[key].changeWord(oldAndNewTuple[1])
		if cipherWordList[key].decoded:
			decodedCiphers[key] = cipherWordList.pop(key, None)
			cipherWordList = checkAllWordsForLetters(decodedCiphers[key].changes,cipherWordList)
		else:
			alteredCiphers[key] = cipherWordList[key]
			cipherWordList = checkAllWordsForLetters(alteredCiphers[key].changes,cipherWordList)
	##writeToFile(oldAndNewTuple,letterChangesFileName)						
	return cipherWordList

def checkAllWordsForLetters(changeTuples,cipherWordList):
    keys = list(cipherWordList.keys())
    listOfChanges.append(changeTuples)
    for word in keys:
        for change in changeTuples:
        	if change[0] in word:
        		if cipherWordList[word].changeCharacter(change[0],change[1]):
        			if cipherWordList[word].decoded:
        				decodedCiphers[word] = cipherWordList.pop(word)
        			else:
        				alteredCiphers[word] = cipherWordList[word]	  				
    writeToFile(changeTuples,letterChangesFileName)	    				
    return cipherWordList

def getAlmostDone():
	ciphersAlmostDone = {}
	for key in alteredCiphers:
		if alteredCiphers[key].decoded == False:
			percentage = int((len(alteredCiphers[key].letterChangePos)/len(alteredCiphers[key].word))*100)
			if percentage > 70 and percentage < 100:
				ciphersAlmostDone[key] = alteredCiphers[key]
	return ciphersAlmostDone		


## applys all changes to text.
def applyChanges(stringIt):
	for i, v in enumerate(listOfChanges):
		previousTextVersions.append(stringIt)
		stringIt = stringIt.replace(v[0],v[1])
		del	listOfChanges[i]

	return stringIt		

def setListOfCipherWords(wordCountTuple):
    length 		= len(wordCountTuple)
    cipherWords = {}
    for i in range(0,length):
    	aCipherWord = CipherWord(wordCountTuple[i][0],wordCountTuple[i][1])
    	cipherWords[wordCountTuple[i][0]] = aCipherWord
    return cipherWords

def writeDecodedCiphersToFile():
	afilename = decodedCipherFileName+"_"+sessionStart+".csv"
	for key in decodedCiphers:
		changeTuple = (key,decodedCiphers[key].word)
		writeToFile([changeTuple],afilename)

def readInCsv(fileName):
	file_exists 	= os.path.isfile(fileName)
	csvChangeList   = []
	if file_exists is False:
		return False

	with open(fileName) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			csvChangeList.append((row['original'],row['changed_to']))
	return csvChangeList	    

def replaceTextWithDecodedCiphers(fileText):
	for key in decodedCiphers:
		match 		= "(?<![\w\d])"+key+"(?![\w\d])"
		fileText 	= re.sub(match,decodedCiphers[key].word,fileText)
	return fileText

def replaceTextWithAlteredCiphers(fileText):
	for key in alteredCiphers:
		match 		= "(?<![\w\d])"+key+"(?![\w\d])"
		fileText 	= re.sub(match,alteredCiphers[key].word,fileText)
	return fileText

def replaceEachLetterWithDecodedLetter(fileText):
	i 			= 0 
	stringList 	= list(fileText)
	empty   	= ""
	while i < len(stringList):
		stringList[i] 	 = getDecodedLetter(stringList[i])
		i 				+= 1
	return empty.join(stringList)	



def getDecodedLetter(char):
	print(listOfChanges)
	if len(listOfChanges) == 1:
	    aChangeDict = dict(listOfChanges[0])
	else:
	    aChangeDict = dict(listOfChanges)

	if char in aChangeDict:
		return aChangeDict[char]
	return char


## 
def getChangeTuples():
	return listOfChanges

def getAlteredCiphers():
	return alteredCiphers

def getDecodedCiphers():
	return decodedCiphers

def appliedCiphers():
	return appliedCiphers	

def getSessionStart():
	return sessionStart			


