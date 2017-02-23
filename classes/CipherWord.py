class CipherWord:

    def __init__(self, word,count):
        self.word 			= word    # instance variable unique to each instance
        self.changes 		= []
        self.letterChangePos= []
        self.unDoneChanges 	= []
        self.isAWord		= False
        self.decoded        = False
        self.count			= count


    def getWord(self):
    	return self.word


    def setWord(self,word):
    	self.word = word


    def changeWord(self,changeTo):
    	if len(changeTo) is not len(self.word):
    		return False
    	i = 0
    	while i < len(changeTo):
    		changed = self.changeCharacter(self.word[i],changeTo[i])
    		if changed is False:
    			return False	
    		i += 1
    	return True


    def isDecoded(self):
    	return self.decoded


    def setDecoded(self,isDecoded):
    	self.decoded = isDecoded	



    def recordChange(self,old,new):
    	self.changes.append((old,new))


    def checkIfAllLettersAreChangedAndSetDecoded(self):
    	if len(self.letterChangePos) == len(self.word):
    		self.decoded = True	


    def changeCharacter(self,oldChar,newChar):
    	if oldChar not in self.word or self.isKeyAChange(oldChar): 
    		return False
    	else:
    		self.recordChange(oldChar,newChar)
    		self.myReplace(oldChar,newChar)
    		self.checkIfAllLettersAreChangedAndSetDecoded()
    		return True

    def myReplace(self,old,newChar):
    	i = 0
    	letters = list(self.word)
    	empty   = ""
    	check   = False 

    	while i < len(letters):
    		 if old == letters[i]:
    		 	aKey = old+"."+str(i)
    		 	if aKey not in self.letterChangePos:
    		 		letters[i] = newChar
    		 		self.letterChangePos.append(newChar+"."+str(i))
    		 i += 1		 
    	self.word = empty.join(letters) 			
    			

    def isKeyAChange(self,aChange):
    	dictOfChanges = dict(self.changes)
    	if aChange in dictOfChanges:
    		return True
    	else:
    		return False

    def isValueAChange(self,aChange):
    	dictOfChanges	= dict(self.changes)
    	if aChange in dictOfChanges.values():
    		return True
    	else:
    		return False	 					


    def printChanges(self):
    	print("WORD: ")
    	i = 0
    	while i < len(self.word):
    		if self.isValueAChange(self.word[i]):
    			print(".",self.word[i],".",end='',sep="")
    		else:
    			print(self.word[i],end='',sep="")	
    		i += 1
    	print("\n")	

    def unDoChanges(self):
    	for i, v in enumerate(self.changes):
    		self.word = self.word.replace(v[1],v[0])
    		self.unDoneChanges.append(self.changes[i])
    	self.deleteChanges()	

    def deleteChanges(self):
    	del self.changes[:]		
    		
		
   		 		

    				
    		

