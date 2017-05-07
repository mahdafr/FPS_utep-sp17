import sys
import fnmatch
import os.path
import os
import shutil

import PyQt5
from PyQt5.QtWidgets import *
#not sure imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# main window
import main_window_gui
#import tShark
import xml.etree.ElementTree as ET

class MainWindow(QMainWindow, main_window_gui.Ui_MainWindow):
    
    ### OPEN Controllers
    
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
        
        #TSHARK
        fileExtension = self.checkFileExtension(filename)
        if fileExtension == False:     
            isFileConverted = False
            #isFileConverted = self.Tshark.pcapToPDML(filename,"output.pdml")
            if  isFileConverted == False:
                print("PDML Could not be converted")
            else:         
                print("File Conveted and save as output.pdml")
        #PDML to List
        i = 0
        with f:
            for line in f:
                self.captureWindow_list.insertItem(i, line)
                i += 1
        
        #reads the packet and creates .xml files for unknown protocols    
        listOfProtocols = self.searchProtocols(filename)
        self.loadFormatters(listOfProtocols)
        listOfFormatters = self.getListOfFileNames(formatterFolderName,formatterFileExtension)
        self.createNonFoundFiles(listOfFormatters,listOfProtocols,formatterFolderName,formatterFileExtension)
        
        #creates a historical copy of a PDML file if is not created yet
        listOfPDMLfiles = self.getListOfPDMLfiles("pdml")
        listOfHistorical = self.getListOfFileNames(historicalFolderName,historicalFileExtension)
        self.createNonFoundFiles(listOfHistorical,listOfPDMLfiles,historicalFolderName,historicalFileExtension)
        
        self.createFolder(ScritpsFolderName)   
        f.close()
       
    #returns false of the file extension is not a pdml type
    def checkFileExtension(self,filename):
        result = True
        fileExtension = os.path.splitext(filename)[1]
        if fileExtension == ".pcap":
           result = False
        return result
        
    #Search for the protocol names in the Caplture File
    #@Requires a file with file extension .pdml
    #@Ensures a list of non repited protoc3ols
    def searchProtocols(self,filename):
        protocolList = []
        tree = ET.parse(filename)
        root = tree.getroot()
        for proto in root.iter('proto'):
            name = proto.get('name')
            if name not in protocolList:
                protocolList.append(name)
        return protocolList
        
    #Loads a list of formatters that can be applied to a capture file
    def loadFormatters(self,formatterList):
        i = 0
        for formatterFile in formatterList:
            self.FormatterWindow_formatterList.insertItem(i, formatterFile)
            i += 1
                
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
                
    #Action SAVE trigger
    def triggeredSaveButton(self):
        print ("Pressed Action Save")
    
    # Action RESTORE trigger
    def triggeredRestoreButton(self):
        try:
            shutil.copy("./historical/cubic.pdml",".")
            print("PDML File Successfully Restored")
        #eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        #eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
    
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
    
    #Action HISTORICAL COPY trigger
    def doubleClickedCaptureItem(self):
        #print ("Double Clicked Capture File")
        self.modeOfOperation_output.insertPlainText("EDIT MODE")
        
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

        ### FILE
        self.actionOpen.triggered.connect(lambda: self.triggeredOpenButton())
        self.actionSave.triggered.connect(lambda: self.triggeredSaveButton())
        self.actionRestore.triggered.connect(lambda: self.triggeredRestoreButton())
        self.actionClose.triggered.connect(lambda: self.triggeredCloseButton())
        
        ### EDIT
        self.actionUndo.triggered.connect(lambda: self.triggeredUndoButton())
        self.actionRedo.triggered.connect(lambda: self.triggeredRedoButton())
        self.actionCopy.triggered.connect(lambda: self.triggeredCopyButton())
        self.actionCut.triggered.connect(lambda: self.triggeredCutButton())
        self.actionPaste.triggered.connect(lambda: self.triggeredPasteButton())
        
        ### WINDOW
        self.actionFilter.triggered.connect(lambda: self.triggeredFilterButton())
        self.actionEditor.triggered.connect(lambda: self.triggeredEditorButton())
        self.actionScript.triggered.connect(lambda: self.triggeredScriptButton())
        self.actionHook.triggered.connect(lambda: self.triggeredHookButton())
        self.actionComand_Line.triggered.connect(lambda: self.triggeredCommandLineButton())
        self.actionHistorical_Copy.triggered.connect(lambda: self.triggeredHistoricalButton())
        
        ### List of Formatters
        self.captureWindow_list.itemDoubleClicked.connect(lambda: self.doubleClickedCaptureItem())


def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()