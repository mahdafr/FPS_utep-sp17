#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from code.eric import Tshark
from jerry import HistoricalCopy

"""
@author Gerardo Fang
@created 04-18 T
@lastmod 05-07 S
""" 
class File:
""" Contract 7: Create Historical Copy """
# @requires the file is of type PCAP
# @ensures 
def convertPCAP(pcap):
    """ Receives a PCAP file to be parsed by the tShark tool """
    Tshark.sendPCAP(pcap)
    return "true"
	
# @requires the file is of type PDML
# @ensures 
def createHistoricalCopy(pdml):
    """ Receives a PDML file and creates a historical copy of the PDML file """
    HistoricalCopy.createHistoricalCopy(pdml)
    return "true"

# @requires the file does not already exist in the folder
# @ensures 
def createFile(file_name, folderName, compareFormatters, currentList):
    """ Creates a new file instance for non existent formatters"""
	if not os.path.exists(folderName):
			os.makedirs(folderName)
			self.createFolder(folderName)
		for protocol in currentList:
			if protocol not in compareFormatters:
				f= open("%s/%s.%s" %(folderName,protocol,fileExtension),"w+")
		print("File successfully created")
    	f.close() 
	