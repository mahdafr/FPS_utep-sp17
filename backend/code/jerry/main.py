import sys
import fnmatch
import os.path
import os
import shutil
import json
from bs4 import BeautifulSoup

import PyQt5
from PyQt5.QtWidgets import *
#not sure imports
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from pathlib import Path
from lxml import etree
from formatter import Formatter


# main window
import main_window_gui
#import tShark
import xml.etree.ElementTree as ET

class MainWindow(QMainWindow, main_window_gui.Ui_MainWindow):
    
    ### OPEN Controllers
    #ACTION OPNE TRIGGERED
    def setLineFormat(self, lineNumber, format):
        cursor = QTextCursor(self.textEdit.document().findBlockByNumber(lineNumber))
        cursor.setBlockFormat(format)
        format = QTextBlockFormat()
        format.setBackground(Qt.yellow)
        # or
        #format.clearBackground() 

    def triggeredOpenButton(self):
        captureList = []
        formatterFolderName = "formatters"
        historicalFolderName = "historical"
        ScritpsFolderName = "scritps"
        formatterFileExtension = "xml"
        historicalFileExtension = "pdml"
        self.createFolder(ScritpsFolderName)
        self.createFolder(historicalFolderName)
        
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
                #If it is a packet rename it as packet id i
                self.captureWindow_list.insertItem(i, line)
                captureList.append(line)
                self.Historical_CaptureText.insertPlainText(line)
                i += 1
                
        #HISTORICAL
        hf = open(filename,'r')
        with hf:
            for line in hf:
                self.Historical_CaptureText.insertPlainText(line)
         
        #reads the packet and creates .xml files for unknown protocols    
        listOfProtocols = self.searchProtocols(filename)
        self.loadFormatters(listOfProtocols)
        listOfFormatters = self.getListOfFileNames(formatterFolderName,formatterFileExtension)
        self.createNonFoundFiles(listOfFormatters,listOfProtocols,formatterFolderName,formatterFileExtension)
        #creates a historical copy of a PDML file if is not created yet
        self.createHistorical(filename)
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
        print("Formatter Files Successfully Created")
    
    #Checks wether the a historical copy under the same name is already stored in
    #the historical folder otherwise create a copy
    #@Requires
    #@Ensures
    def createHistorical(self,filename):
        fileExists = os.path.isfile('./historical/%r' %filename)
        print(fileExists)
        if fileExists == False:
            try:
                shutil.copy2("./cubic.pdml","./historical/")
                print("Historical Copy Successfully Created")
            #eg. src and dest are the same file
            except shutil.Error as e:
                print('Error: %s' % e)
            #eg. source or destination doesn't exist
            except IOError as e:
                print('Error: %s' % e.strerror)
     
    #Checks wether the folder is already created of not it creates it
    #under the same working directory
    #@Requires
    #@Ensures
    def createFolder(self,folderName):
        if not os.path.exists(folderName):
            os.makedirs(folderName)
    
    #Search for the protocol names in the Caplture File
    #@Requires a file with file extension .pdml
    #@Ensures a list of non repited protoc3ols
    def FilterProtocol(self,filename,protocolName):
        self.modeOfOperation_output.setDisabled(False)
        self.modeOfOperation_output.clear()
        self.modeOfOperation_output.insertPlainText("FILTER MODE")
        self.modeOfOperation_output.setDisabled(True)
        captureList = []
        fp = open(filename)
        shouldPrint = False
        #target = open(filename, 'w')
        target = open("testing.pdml", 'w')
        for line in fp:
            protoStarts = '<proto name="' + protocolName
            if protoStarts in line:
                shouldPrint = True
                target.write(line)
            elif "</proto>"in line and shouldPrint == True:
                target.write(line)
                shouldPrint = False
            elif shouldPrint == True or "<packet" in line or "<pdml" in line or "</packet" in line or "</pdml"in line or "<?xml" in line:
                target.write(line)
            else:
                shouldPrint = False
        i = 0
        f = open("testing.pdml",'r') 
        with f:
            for line in f:
                self.captureWindow_list.insertItem(i, line)
                captureList.append(line)
                self.Historical_CaptureText.insertPlainText(line)
                i += 1
        fp.close()
                                
    #Action SAVE trigger
    def triggeredSaveButton(self):
        print ("Pressed Action Save")
    
    # Action RESTORE trigger
    def triggeredRestoreButton(self):
        try:
            shutil.copy2("./historical/cubic.pdml",".")
            print("PDML File Successfully Restored")
        #eg. src and dest are the same file
        except shutil.Error as e:
            print('Error: %s' % e)
        #eg. source or destination doesn't exist
        except IOError as e:
            print('Error: %s' % e.strerror)
    
    #Action CLOSE trigger
    def triggeredCloseButton(self):
        print ("Pressed Action Closed")
    
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
        fieldTextLine = self.captureWindow_list.currentItem().text()
        soup = BeautifulSoup(fieldTextLine, "lxml") 
        soupstring = str(soup)
        if "value=" in soupstring:
            field = soup.field
            print (field['name'])
            print (field['value'])
            self.getFieldPressed = field['name']
            self.Edit_Window_FiledList.insertItem(0, field['name'])
            self.Edit_Window_filedValue.clear()
            self.Edit_Window_filedValue.insertPlainText(field['value'])
            self.getValueofField = field['value']
            #self.modeOfOperation_output.insertPlainText("EDIT MODE")
            formatter = Formatter()
            formatter.appendHide(field['name'],field['value'])
            formatter.createFormatter()
        self.modeOfOperation_output.clear()
        self.modeOfOperation_output.insertPlainText("EDIT MODE")
        self.modeOfOperation_output.setDisabled(True)  
          
    def clickedfilterBarButton(self):
        protocolName = self.Filter_Bar_input.toPlainText()
        self.FilterProtocol("cubic.pdml",protocolName)
    
    def clickedEditChangeValueButton(self):
        self.modeOfOperation_output.setDisabled(False)
        self.modeOfOperation_output.clear()
        captureList = []
        self.modeOfOperation_output.insertPlainText("EDIT MODE")
        self.modeOfOperation_output.setDisabled(True)
        fp = open("cubic.pdml", 'r')
        target = open("testing.pdml", 'w')
        for line in fp:
            if self.getFieldPressed in line:
                line = line.replace(self.getValueofField, 'almostthere')
                target.write(line)
            else:
                target.write(line)
        i = 0
        f = open("testing.pdml",'r') 
        with f:
            for line in f:
                self.captureWindow_list.insertItem(i, line)
                captureList.append(line)
                self.Historical_CaptureText.insertPlainText(line)
                i += 1
        fp.close()
    
    def clickedAnnotateButton(self):
        self.modeOfOperation_output.setDisabled(False)
        self.modeOfOperation_output.clear()
        captureList = []
        self.modeOfOperation_output.insertPlainText("EDIT MODE")
        self.modeOfOperation_output.setDisabled(True)
        fp = open("cubic.pdml", 'r')
        target = open("testing.pdml", 'w')
        annotateField = self.Edit_Window_filedAnnotation.toPlainText()
        annotationString = '>\n' + '\t<annotation id = '+ self.getFieldPressed +'>' + annotateField + '</annotation>'
        for line in fp:
            if self.getFieldPressed in line:
                line = line.replace( ">", annotationString)
                target.write(line)
            else:
                target.write(line)
        i = 0
        f = open("testing.pdml",'r') 
        with f:
            for line in f:
                self.captureWindow_list.insertItem(i, line)
                captureList.append(line)
                self.Historical_CaptureText.insertPlainText(line)
                i += 1
        fp.close()
        print("annotation added") 
    #added code here--------------------------------------------------------
    def clickedHideFiledButton(self):
        self.modeOfOperation_output.setDisabled(False)
        self.modeOfOperation_output.clear()
        captureList = []
        self.modeOfOperation_output.insertPlainText("EDIT MODE")
        self.modeOfOperation_output.setDisabled(True)
        fp = open("cubic.pdml", 'r')
        target = open("testing.pdml", 'w')
        for line in fp:
            if self.getFieldPressed in line:
                line = line.replace('field', 'field hide = "true"')
                target.write(line)
            else:
                target.write(line)
        i = 0
        f = open("testing.pdml",'r') 
        with f:
            for line in f:
                self.captureWindow_list.insertItem(i, line)
                captureList.append(line)
                self.Historical_CaptureText.insertPlainText(line)
                i += 1
        fp.close()
        
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        
        self.Filter_Bar_Button.clicked.connect(lambda: self.clickedfilterBarButton())
        
        ### EDIT WINDOW
        self.Edit_Window_changeValueButton.clicked.connect(lambda: self.clickedEditChangeValueButton())
        self.Edit_Window_AnnotateButton.clicked.connect(lambda: self.clickedAnnotateButton())
        self.Edit_Window_hideFiledButton.clicked.connect(lambda: self.clickedHideFiledButton())

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
        self.modeOfOperation_output.setDisabled(False)
        self.modeOfOperation_output.clear()
        self.modeOfOperation_output.insertPlainText("NO PDML")
        self.modeOfOperation_output.setDisabled(True)
        self.getFieldPressed = "nothing"
        self.getValueofField = "nothing"
        self.getAnnotationofField = "nothing"


def main():
    # a new app instance
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
