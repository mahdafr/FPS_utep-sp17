# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T


@modified mafravi on 05-07 U made into a class
"""

class Expression:
    primitive = [] #Primitives
    
    """ Contract 4: Manage Primitives """
    # @requires primitive is in the Berkeley Packet Filter (BPF) syntax
    # @ensures 
    def addPrimitive(self,p,logicalExp):
        """ Receives a primitive and adds it to this expression """
        expressionSize = self.primitive.count(p)
        if expressionSize <= 1:
            self.primitive.append(logicalExp)
            self.primitive.append(p)
        else:
            self.primitive.append(p)

    # @requires the primitive exists in this expression
    # @ensures  
    def deletePrimitive(self,p):
        """ Deletes the primitive from the expression """
        expressionSize = self.primitive.count(self.primitive)
        if expressionSize <= 1:
            self.primitive.remove(p)
        else:
            primitiveIndex = self.primitive.index(p)
            self.expression.remove(p)
            self.expression.remove(primitiveIndex-2)
    
    # @requires the primitive exists in this expression
    # @ensures  
    def checkBPFsyntax(primitive):
        """ Deletes the primitive from the expression """
        pass

    pass