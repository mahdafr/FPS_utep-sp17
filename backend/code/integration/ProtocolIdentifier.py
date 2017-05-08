#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Gerardo Fang
@created 04-18 T
@lastmod 04-21 F
"""
import xml.etree.ElementTree as ET

class ProtocolIdentifier:

    """ Contract 20: Scan PDML """
    
    def __init__(self, file, fileF):
        self.listOfProtocols = []
        self.file = file
        self.listOfFormatters = []
        self.listOfNoFormatters = []
        self.fileFormatters = fileF
        

    # @requires file type is of PDML and has been opened by PFS
    # @ensures returns a list of all identified protocols from the file
    def identifyProtocols(self):
        tree = ET.parse(self.file)
        root = tree.getroot()
        for proto in root.iter('proto'):
            name = proto.get('name')
            self.listOfProtocols.append(name)
        self.removeDuplicates()
        self.identifyFormatters()
        
    def printList(self):
        print (self.listOfProtocols)
        print (self.listOfFormatters)
        print (self.listOfNoFormatters)

    def removeDuplicates(self):
        newList = []
        for i in self.listOfProtocols:
            if i not in newList:
                newList.append(i)
        self.listOfProtocols = newList
        
    # @requires file type is of PDML and has been opened by PFS
    # @ensures returns a list of all applied formatters from the file
    def identifyFormatters(self):
        """ Receives a file and returns a list of all identified formatters """
        formatterListFound = ['geninfo', 'randomFormatter', 'tcp', 'xml']
        for val in self.listOfProtocols:
            if val in formatterListFound:
                self.listOfFormatters.append(val)
            if val not in formatterListFound:
                self.listOfNoFormatters.append(val)
        
        
    
    # @requires the rule list is empty
    # @ensures 
    def createFormatter(rule):
    	""" Receives a list of rules to build a new formatter """

object1 = ProtocolIdentifier('cubic.pdml', 'formatters.txt')
object1.identifyProtocols()
object1.printList()


    


