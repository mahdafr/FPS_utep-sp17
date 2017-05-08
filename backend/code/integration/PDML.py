# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Debugging
"""
import elementTree as et, pickle as p
import File

class PDML(File):
    formatter = [] #list of applied formatters
    fileName = "" #string: <name>.pdml
    rule = [] #list of Rule objects in this
    protocol = [] #list of the Protocols within the PDML
    pdml = "" #the PDML parsed by elementTree
    historicalCopy = fileName + "_historical.pdml"
    
    def __init__(self,name):
        self.fileName = name + ".pdml"
        self.pdml = et.parse(self.fileName)
    
    """ Contract 17: Apply Formatter """
    # @requires formatter is not being edited and the Protocol exists
    # @ensures HistoricalCopy remainds unedited
    def applyFormatter(self,f):
        """ Applies each rule to the current PDML """
        for r in self.rule: #go through every rule
            for proto in self.protocol:
                if proto==f.protocol: #check if the protocol should be examined
                    for filt in r.filter: #go through every filter in the rule
                        for actn in filt.action: #every action of the filter
                            actn.applyAction() #run/apply the action
        self.formatter.append(f)
    
    
    """ Contract 18: Revert to Historical Copy """
    # @requires the HistoricalCopy for this PDML exists within PFS
    # @ensures neither this PDML nor its HistoricalCopy will be modified
    def findChanges(self,historicalCopy):
        """ Returns a list of the Protocols changed from the HistoricalCopy """
        hist = et.parse(historicalCopy)
        hist = hist.getroot()
        root = self.pdml.getroot()
        protosInPDML = [] ; protosInHist = []
        differentProtos = []
        for pr in root:
            protosInPDML.append(pr)
        for pr in hist:
            protosInHist.append(pr)
        if ( protosInHist.size < protosInPDML.size ):
            differentProtos = protosInPDML - protosInHist
        return differentProtos
    
    
    # @requires the formatter has already been applied
    # @ensures 
    def acceptChanges(self):
        """ Saves the changes aplied to this PDML in the PFS """
        f = open(p, "w")
        f.write(self.pdml)
    

    # @requires the HistoricalCopy exists within the PFS
    # @ensures 
    def rejectChanges(self,historicalCopy):
        """ Reverts this PDML to its HistoricalCopy """
        self.pdml = et.parse(historicalCopy)
    
    
    pass #end PDML class