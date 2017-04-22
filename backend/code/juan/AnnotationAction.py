# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T
"""

""" Contract 3: AnnotationAction """
# @requires action exists
# @ensures 
class AnnotaionAction: 
    
    def addAnnotation(annotation,rule):
    """ Receives an annotation and adds a new action to the rule """
    rule.annotation = annotation
       
    # @requires  annotation is the last action added to the rule
    # @ensures 
    def deleteAnnotation(annotation,rule):
        """ Receives an annotation and deletes it """
        del rule.annotation = annotation

