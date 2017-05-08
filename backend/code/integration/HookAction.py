# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Debugged Contracts


RUN FOR TESTS
"""
import Action, Hook, Field

class HookAction(Action): #subclass
    field = "" #Field: to apply this Action to
    hook = "" #Hook to this class
    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    @classmethod
    def createHookAction(self,f: Field, h: Hook):
        """ Creates a HidingAction to this Field """
        self.field = f
        self.hook = h
        super(HookAction,self).createHookAction(self,f,h)
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    def applyAction(self):
        """ Apply this Action to its Field """
        self.hook.run()
        super(HookAction,self).applyAction(self)
        pass
    
    
    """ Contract 4: Manage Hook Action """
    # @requires 
    # @ensures 
    @classmethod
    def applyHook(self):
        """ Applies the Hook attached to this Field """
        self.hook.run()
        ## todo getReturnValue() and apply it to the Field
        super(HookAction,self).applyHook(self)
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    def deleteHook(self):
        """ Removes the Hook attached to this Field """
        self.hook = ""
        super(HookAction,self).deleteHook(self)
        pass
        
    pass ##end subclass definition

