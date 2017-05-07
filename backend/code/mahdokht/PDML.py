# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 04-18 T
Implemented Contracts 17 and 18
"""
import elementTree as et, pickle as p

class PDML:
    formatter = [] #list of applied formatters
    fileName = "" #string: <name>.pdml
    rule = [] #list of Rule objects in this
    protocol = [] #list of the Protocols within the PDML

    
    def __init__(self,name):
        self.fileName = name
    
    """ Contract 17: Apply Formatter """
    # @requires formatter is not being edited and the Protocol exists
    # @ensures HistoricalCopy remainds unedited
    def applyFormatter(f):
        """ Applies each rule to the current PDML """
        for r in rule: #go through every rule
            for p in protocol: #check if the protocol should be examined
                if p==f.protocol:
                    for filt in rule.filter:
                        for a in filt.action:
                            
                    

    # @requires field exists in the Protocol
    # @ensures only this field will be modified according to its action
    def updateField(action,field):
        """ Receives an Action to be applied to this Field """
        
    
    """ Contract 18: Revert to Historical Copy """
    # @requires the HistoricalCopy for this PDML exists within PFS
    # @ensures neither this PDML nor its HistoricalCopy will be modified
    def findChanges(historicalCopy):
        """ Receives the matching HistoricalCopy to compare changes to """
    	
    
    # @requires the formatter has already been applied
    # @ensures 
    def acceptChanges():
        """ Saves the changes aplied to this PDML in the PFS """
    	
    
    # @requires the HistoricalCopy exists within the PFS
    # @ensures 
    def rejectChanges(historicalCopy):
        """ Reverts this PDML to its HistoricalCopy """
    	
    
    """ Priavte Responsibilities """
    def saveChanges():
        """ """
        
    pass #end PDML class