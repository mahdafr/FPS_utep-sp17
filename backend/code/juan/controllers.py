#!/usr/bin/python

#ACTION OPNE TRIGGERED
def triggeredOpenButton(self):
	formatterFolderName = "formatters"
	historicalFolderName = "historical"
	ScritpsFolderName = "scritps"
	formatterFileExtension = "xml"
	historicalFileExtension = "pdml"
	
	# Search for a file and display it to captureWindow_captureFile
	filename = QFileDialog.getOpenFileName(self, 'Open file', 
	'',"PDML or PCAP files (*.pdml *.pcap *.txt)")[0]
	f = open(filename,'r')
	#CHECK IF IT IS A PCAP OR PDML

	with f:
		data = f.read()
		self.captureWindow_captureFile.insertPlainText(data)
	
	#reads the packet and creates .xml files for unknown protocols    
	listOfProtocols = self.searchProtocols(filename)
	listOfFormatters = self.getListOfFileNames(formatterFolderName,formatterFileExtension)
	self.createNonFoundFiles(listOfFormatters,listOfProtocols,formatterFolderName,formatterFileExtension)
	
	#creates a historical copy of a PDML file if is not created yet
	listOfPDMLfiles = self.getListOfPDMLfiles("pdml")
	listOfHistorical = self.getListOfFileNames(historicalFolderName,historicalFileExtension)
	self.createNonFoundFiles(listOfHistorical,listOfPDMLfiles,historicalFolderName,historicalFileExtension)
	
	self.createFolder(ScritpsFolderName)   
	f.close()
			
#Action SAVE trigger
def triggeredSaveButton(self):
	print ("Pressed Action Save")

# Action RESTORE trigger
def triggeredRestoreButton(self):
	print ("Pressed Action Restore")

#Action CLOSE trigger
def triggeredCloseButton(self):
	print ("Pressed Action Open")

### EDIT Controllers

#Action UNDO trigger
def triggeredUndoButton(self):
	print ("Pressed Action Undo")
	
#Action REDO trigger
def triggeredRedoButton(self):
	print ("Pressed Action Redo")

#Action COPY trigger
def triggeredCopyButton(self):
	print ("Pressed Action Copy")

#Action CUT trigger
def triggeredCutButton(self):
	print ("Pressed Action Cut")

#Action PASTE trigger
def triggeredPasteButton(self):
	print ("Pressed Action Paste")

### WINDOW Controllers

#Action FILTER trigger
def triggeredFilterButton(self):
	print ("Pressed Action Filter")
	
#Action EDITOR trigger
def triggeredEditorButton(self):
	print ("Pressed Action Editor")

#Action SCRIPT trigger
def triggeredScriptButton(self):
	print ("Pressed Action Script")

#Action HOOK trigger
def triggeredHookButton(self):
	print ("Pressed Action Hook")

#Action COMMAND LINE trigger
def triggeredCommandLineButton(self):
	print ("Pressed Action CommandLine")

#Action HISTORICAL COPY trigger
def triggeredHistoricalButton(self):
	print ("Pressed Action Historical Copy")