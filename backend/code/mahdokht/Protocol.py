# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 04-18 T
Implemented Contracts 17 and 18
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
    
    def 
    
    pass #end Protocol class