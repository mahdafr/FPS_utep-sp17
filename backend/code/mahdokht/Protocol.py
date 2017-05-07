# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-06 S
Implemented attributes, mutators, and getters
"""


class Protocol:
    longname = "" #optional: string
    name = "" #required: string
    size = 0 #required: byes
    pos = 0 #required: bytes
    field = [] #list of Fields in this Protocol
    
    def __init__(self,n,s,p,l,f):
        self.name = n
        self.size = s
        self.pos = p
        self.longname = l
        self.field.append(f)
    
    def getName(self):
		return self.name
	
	def getSize(self):
		return self.size
	
	def getPos(self):
		return self.pos
	
	def getFields(self):
		return self.field
	
	def getLongname(self):
		return self.longname
    
    pass #end Protocol class