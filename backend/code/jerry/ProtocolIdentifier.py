#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Gerardo Fang
@created 04-18 T
@lastmod 04-21 F
"""

""" Contract 20: Scan PDML """
# @requires file type is of PDML and has been opened by PFS
# @ensures returns a list of all identified protocols from the file
import xml.etree.ElementTree as ET

class ProtocolIdentifier:

    def __init__(self, file):
        self.listOfProtocols = []
        self.file = file

    def identifyProtocols(self):
        Fh = open(self.file,'r')
        tree = ET.parse(self.file)
        root = tree.getroot()
        for proto in root.iter('proto'):
            name = proto.get('name')
            self.listOfProtocols.append(name)
        self.removeDuplicates()

    def printList(self):
        print (self.listOfProtocols)

    def removeDuplicates(self):
        newList = []
        for i in self.listOfProtocols:
            if i not in newList:
                newList.append(i)
        self.listOfProtocols = newList

object1 = ProtocolIdentifier('nameOfPDML.pdml')
object1.identifyProtocols()
object1.printList()
	

# @requires file type is of PDML and has been opened by PFS
# @ensures returns a list of all applied formatters from the file
def identifyFormatters(pdml):
    """ Receives a file and returns a list of all identified formatters """
	

# @requires the rule list is empty
# @ensures 
def createFormatter(rule):
	""" Receives a list of rules to build a new formatter """