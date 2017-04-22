# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18""

""" Contract 24: Manage Script """
# @requires 
# @ensures the script python file will be created if it does not already exist
def createScript(hook):
    """ Creates a script for this hook """
	

# @requires the script is associated with hook
# @ensures the script file is not deleted
def deleteScript(hook):
    """ Deletes the script from this hook """
	

""" Contract 25: Modify Script """
# @requires the script python file exists
# @ensures 
def updateAlgorithm(algorithm):
    """ Overwrites the existing algorithm to contain this string """
	

# @requires the string is a valid file system path to this algorithm
# @ensures the script is not deleted
def updatePath(path):
    """ Sets the new path to this script """
	

""" Contract 26: Run Script """
# @requires the script has completed execution and has a return value
# @ensures 
def getReturnValue():
    """ Gets the return value from the script's execution """
	

# @requires the script's return value type matches the field's value type
# @ensures 
def updateField(field):
    """ Updates the field associated with this hook """
	
