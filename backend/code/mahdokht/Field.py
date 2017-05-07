# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 04-18 T
Implemented Contracts 17 and 18
"""


class Field:
    hidden = True #optional: boolean
    longname = "" #required: string
    mask = 0 #optional: bytes
    name = "" #required: string
    pos = 0 #required: bytes
    show = False #required: boolean
    showdtl = "" #optional: string
    
    def __init__(self,name):
        self.fileName = name
    
    def getName(self):
        return self.name
    def isHidden(self):
        return self.hidden
    def getPos(self):
        return self.pos
    def getShow(self):
        return self.show
    
    pass #end Field class