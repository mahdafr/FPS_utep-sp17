# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified mafravi on 05-07 U: subclassed it
"""

""" Contract 3: AnnotationAction """
# @requires action exists
# @ensures 
import Action

class AnnotationAction(Action):
    annotation = "" #String: for AnnotationAction
    field = "" #Field: to apply this Action to
    
    @classmethod
    def createAnnotationAction(self,f,a):
        """ Receives an annotation and adds this annotation to this field """
        self.field = f
        self.annotation = a
        super(AnnotationAction,self).createAnnotationAction(self,f,a)
        
    # @requires 
    # @ensures 
    @classmethod
    def applyAction(self):
        """ Apply this Action to its Field """
        self.field.addAnnotation(self.annotation)
        super(AnnotationAction,self).applyAction(self)
        pass
    
    """ Contract 3: Manage Field Annotation """
    # @requires 
    # @ensures 
    @classmethod
    def addAnnotation(self,f,a):
        """ Links the Annotation to this Field """
        self.field = f
        self.annotation = a
        super(AnnotationAction,self).createAnnotationAction(self,f,a)
    
    
    # @requires 
    # @ensures
    @classmethod 
    def deleteAnnotation(self):
        """ Deletes the annotation """
        self.annotation = ""
        super(AnnotationAction,self).deleteAnnotationAction(self)
    
    pass #end of subclass

