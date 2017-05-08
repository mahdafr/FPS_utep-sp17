# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Debugged Contracts


RUN FOR TESTS
"""
import Action, Field

class RenameAction(Action): #subclass
    field = "" #Field: to apply this Action to
    previousName = "" #String: the previous name for restoration
    rename = "" #String: to rename this field to
    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    @classmethod
    def createRenameAction(self,f: Field,newName):
        """ Creates a RenameAction to this Field """
        self.rename = newName
        self.previousName = f.getName()
        super(RenameAction,self).createRenameAction(f,newName)
    
    # @requires 
    # @ensures 
    @classmethod
    def applyAction(self):
        """ Apply this Action to its Field """
        self.previousName = self.field.getName()
        self.setName(self.rename)
        super(RenameAction,self).applyAction(self)
        pass
    
    
    """ Contract 5: Manage Field Renaming """
    # @requires 
    # @ensures 
    @classmethod
    def renameField(self,newName):
        """ Receives a String to rename this Field """
        self.rename = newName
        pass
    
    # @requires renameField(1) has been called before
    # @ensures 
    @classmethod
    def restoreName(self):
        """ Restores the previousName to this Field, storing the current one
            as the now-old one """
        pass
        
    pass ##end subclass definition

