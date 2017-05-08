# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Debugged Contracts


RUN FOR TESTS
"""
import Action, Field

class HidingAction(Action): #subclass
    field = "" #Field: to apply this Action to
    isHidden = False #Field is (not) displayed: Boolean
    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    def createHidingAction(self, f: Field, hide):
        """ Creates a HidingAction to this Field """
        self.field = f
        self.isHidden = hide
        super(HidingAction,self).createHidingAction(f,hide)
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    def applyAction(self):
        """ Apply this Action to its Field """
        if self.isHidden==True:
            self.field.hide()
        else:
            self.field.unHide()
        super(HidingAction,self).applyAction()
        pass
    
    
    """ Contract 2: Manage Field Visualization """
    # @requires 
    # @ensures 
    @classmethod
    def hideField(self):
        """ Hides the Field currently displayed with this Action """
        self.isHidden = True
        super(HidingAction,self).hideField(self)
        return self.isHidden
        
    
    # @requires field is in the Protocol and not displayed
    # @ensures
    @classmethod
    def showField(self):
        """ Displays the Field currently hidden with this Action """
        self.isHidden = False
        super(HidingAction,self).showField(self)
        return self.isHidden
        
    pass ##end class definition

