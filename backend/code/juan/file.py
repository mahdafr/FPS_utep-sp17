#!/usr/bin/python
	
	# Searches file names with extension X and retrieves a list
	#@Requires folder name is in the same working directory
	#@Ensures a list of non repited file names
	def getListOfFileNames(self,folderName,fileExtension):
		listOfFiles = []
		self.createFolder(folderName)
		for file in os.listdir('./%s' % folderName):
			if fnmatch.fnmatch(file, '*.%s' % fileExtension):
				if file not in listOfFiles:
					listOfFiles.append(os.path.splitext(file)[0])                
		return listOfFiles
	
	# Searches file names with extension X and retrieves a list
	#@Requires folder name is in the same working directory
	#@Ensures a list of non repited file names
	def getListOfPDMLfiles(self,fileExtension):
		listOfFiles = []
		for file in os.listdir('./'):
			if fnmatch.fnmatch(file, '*.%s' % fileExtension):
				if file not in listOfFiles:
					listOfFiles.append(os.path.splitext(file)[0])                
		return listOfFiles
	
	#Description creates a formatter files
	#@Requires a list of non empty protocol list and formatter list
	#@Ensures
	def createNonFoundFiles(self,compareAgainstList,listToBeCreated,folderName,fileExtension):
		self.createFolder(folderName)
		for protocol in listToBeCreated:
			if protocol not in compareAgainstList:
				f= open("%s/%s.%s" %(folderName,protocol,fileExtension),"w+")
		print("Folder & files successfully created")
		
	#Checks wether the folder is already created of not it creates it
	#under the same working directory
	#@Requires
	#@Ensures
	def createFolder(self,folderName):
		if not os.path.exists(folderName):
			os.makedirs(folderName)