# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T
"""

""" Contract 5: Visualize Field """
# @requires field belongs to the protocol and is not hidden
# @ensures 
def showField(field):
    """ Receives a field currently hidden and displays it """
	

# @requires field belongs to the protocol and is hidden
# @ensures 
def hideField(field):
	""" Receives a field currently displayed and hides it """
	

""" Contract 6: Modify Field """
# @requires field is editable by this formatter
# @ensures 
def renameField(name,action,field):
	""" Receives a string and adds to the action the renaming of this field """
	

# @requires field exists within the protocol
# @ensures 
def addHook(name,action,field):
	""" Adds a hook to the field within the action """
	

# @requires action is an annotation
# @ensures 
def addAnnotation(action,annotation):
	""" Receives an annotation and adds it to the action """
	

# @requires field exists within the protocol
# @ensures 
def updateField(toUpdate,field):
	""" Receives either a string or boolean and updates the field value """
	

