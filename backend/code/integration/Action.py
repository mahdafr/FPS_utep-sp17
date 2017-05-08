# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Implemented Abstract-ness (assertions)


RUN FOR TESTS
"""
import abc as abc
import AnnotationAction, HidingAction, HookAction, RenameAction
import Hook, Field

class Action(metaclass=abc.ABCMeta): #this is the unimplementable abstract superclass
    previousName = "" #String: for RenameAction
    rename = "" #String: to rename this to
    field = "" #Field: to apply this Action to
    hook = "" #Hook: to link to this Field
    isHidden = False #Field is (not) displayed: boolean
    annotation = "" #String: for AnnotationAction

    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createAnnotationAction(self, f: Field,annotation):
        """ Creates an AnnotationAction to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createHidingAction(self, f: Field,hide):
        """ Creates a HidingAction to this FIeld """
        pass

    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createHookAction(self,f: Field, h: Hook):
        """ Creates a HookAction to this Field """
        pass

    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createRenameAction(self,f: Field,newName):
        """ Creates a RenameAction to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def applyAction(self):
        """ Apply this Action to its Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteAction(self):
        """ Deletes the Action from this Rule """
        pass
    
    
    """ Contract 2: Manage Field Visualization """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def hideField(self):
        """ Hides the Field currently displayed with this Action """
        pass
    
    # @requires field is in the Protocol and not displayed
    # @ensures
    @classmethod
    @abstractmethod 
    def showField(self):
        """ Displays the Field currently hidden with this Action """
        pass
    
    
    """ Contract 3: Manage Field Annotation """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def addAnnotation(self,annotation):
        """ Links the Annotation to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteAnnotation(self):
        """ Deletes the Annotation from this Field """
        pass
    
    
    """ Contract 4: Manage HookAction """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def applyHook(self):
        """ Applies the Hook attached to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteHook(self):
        """ Removes the Hook attached to this Field """
        pass
    
    
    """ Contract 5: Manage Field Renaming """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def renameField(self,newName):
        """ Receives a String to rename this Field """
        pass
    
    # @requires renameField(1) has been called before
    # @ensures 
    @classmethod
    @abstractmethod
    def restoreName(self):
        """ Restores the previousName to this Field, storing the current one
            as the now-old one """
        pass
    pass ##end abstract class definition


assert issubclass(tuple,Action) 
Action.register(tuple)
#subclasses
assert issubclass(AnnotationAction,Action) 
Action.register(AnnotationAction)
assert issubclass(HidingAction,Action) 
Action.register(HidingAction)
assert issubclass(HookAction,Action) 
Action.register(HookAction)
assert issubclass(RenameAction,Action) 
Action.register(RenameAction)


