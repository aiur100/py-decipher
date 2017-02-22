from collections 		import Counter
from classes.CipherWord	import CipherWord

## list of changes
listOfChanges 			= []
appliedChanges			= []
previousTextVersions 	= []
alteredCiphers			= {}
decodedCiphers			= {}
appliedCiphers			= []

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
	listOfChanges.append(oldAndNewTuple)
	key = oldAndNewTuple[0]
	if key in cipherWordList:
		cipherWordList[key].changeWord(oldAndNewTuple[1])
		if cipherWordList[key].decoded:
			decodedCiphers[key] = cipherWordList.pop(key, None)
			cipherWordList = checkAllWordsForLetters(decodedCiphers[key].changes,cipherWordList)
		else:
			alteredCiphers[key] = cipherWordList[key]
			cipherWordList = checkAllWordsForLetters(alteredCiphers[key].changes,cipherWordList)				
	return cipherWordList

def checkAllWordsForLetters(changeTuples,cipherWordList):
    keys = list(cipherWordList.keys())
    for word in keys:
        for change in changeTuples:
        	if change[0] in word:
        		if cipherWordList[word].changeCharacter(change[0],change[1]):
        			if cipherWordList[word].decoded:
        				decodedCiphers[word] = cipherWordList.pop(word)
        			else:
        				alteredCiphers[word] = cipherWordList[word]
    return cipherWordList

def getAlmostDone():
	ciphersAlmostDone = {}
	for key in alteredCiphers:
		if alteredCiphers[key].decoded == False:
			percentage = int((len(alteredCiphers[key].letterChangePos)/len(alteredCiphers[key].word))*100)
			if percentage > 80:
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


## 
def getChangeTuples():
	return listOfChanges

def getAlteredCiphers():
	return alteredCiphers

def getDecodedCiphers():
	return decodedCiphers

def appliedCiphers():
	return appliedCiphers			


