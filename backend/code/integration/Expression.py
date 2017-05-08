# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T
"""

""" Contract 4: Manage Primitives """
class Expression:
    expression = []
#Expression Constructor
def __init__(self):
    self.expression = []
# @requires primitive is in the Berkeley Packet Filter (BPF) syntax
# @ensures 
def addPrimitive(primitive,logicalExp):
    """ Receives a primitive and adds it to this expression """
    expressionSize = expression.count(expression)
    if expressionSize <= 1:
        expression.append(logicalExp)
        expression.append(primitive)
    else:
        expression.append(primitive)
# @requires the primitive exists in this expression
# @ensures  
def deletePrimitive(primitive):
    """ Deletes the primitive from the expression """
    expressionSize = expression.count(expression)
    if expressionSize <= 1:
        expression.remove(primitive)
     else:
        primitiveIndex = Expression.index(primitive)
        logicalExp = 
        expression.remove(primitive)
        expression.remove(primitiveIndex-2)
# @requires the primitive exists in this expression
# @ensures  
def checkBPFsyntax(primitive):
    """ Deletes the primitive from the expression """