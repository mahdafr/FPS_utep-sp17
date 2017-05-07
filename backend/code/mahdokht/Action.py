# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 04-18 T
Implemented Contracts 1-5
"""
import abc as abc
import AnnotationAction, HidingAction, HookAction, RenameAction

class Action(metaclass=abc.ABCMeta): #this is the unimplementable abstract superclass
    previousName = "" #String: for RenameAction
    field = "" #Field: to apply this Action to
    hook = "" #Hook: to link to this Field
    isHidden = False #Field is (not) displayed: boolean
    
    """ Contract 1: Manage Action """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createAction(f,annotation):
        """ Creates an AnnotationAction to this Field """
        pass
    
    ## FIXME: idk if we can have multiple constructors in py?
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createAction(f,hide):
        """ Creates a HidingAction to this FIeld """
        pass

    ## FIXME: idk if we can have multiple constructors in py?
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createAction(f,hook):
        """ Creates a HookAction to this Field """
        pass

    ## FIXME: idk if we can have multiple constructors in py?
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def createAction(f,newName):
        """ Creates a RenameAction to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteAction():
        """ Deletes the Action from this Rule """
        pass
    
    
    """ Contract 2: Manage Field Visualization """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def hideField():
        """ Hides the Field currently displayed with this Action """
        pass
    
    # @requires field is in the Protocol and not displayed
    # @ensures
    @classmethod
    @abstractmethod 
    def showField():
        """ Displays the Field currently hidden with this Action """
        pass
    
    
    """ Contract 3: Manage Field Annotation """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def addAnnotation(annotation):
        """ Links the Annotation to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteAnnotation():
        """ Deletes the Annotation from this Field """
        pass
    
    
    """ Contract 4: Manage HookAction """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def applyHook():
        """ Applies the Hook attached to this Field """
        pass
    
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def deleteHook():
        """ Removes the Hook attached to this Field """
        pass
    
    
    """ Contract 5: Manage Field Renaming """
    # @requires 
    # @ensures 
    @classmethod
    @abstractmethod
    def renameField(newName):
        """ Receives a String to rename this Field """
        pass
    
    # @requires renameField(1) has been called before
    # @ensures 
    @classmethod
    @abstractmethod
    def restoreName():
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


