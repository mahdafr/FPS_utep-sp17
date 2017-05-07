# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Debugged Contracts
"""
import Action

class HidingAction(Action): #subclass
    field = "" #Field: to apply this Action to
    isHidden = False #Field is (not) displayed: Boolean
    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    @classmethod
    def createAction(self,f,hide):
        """ Creates a HidingAction to this Field """
        self.isHidden = hide
        super(HidingAction,self).createAction(f,hide)
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    def deleteAction():
        """ Deletes the Action from this Rule """
		##todo idk boiz
        pass
    
    
    """ Contract 2: Manage Field Visualization """
    # @requires 
    # @ensures 
    @classmethod
    def hideField(self):
        """ Hides the Field currently displayed with this Action """
        super(HidingAction,self).hideField(self)
        return self.isHidden
        
    
    # @requires field is in the Protocol and not displayed
    # @ensures
    @classmethod
    def showField(self):
        """ Displays the Field currently hidden with this Action """
        super(HidingAction,self).showField(self)
        return self.isHidden
        
    pass ##end class definition

