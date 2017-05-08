# -*- coding: utf-8 -*-
"""
@author Mahdokht Afravi
@created 04-18 T

@modified 05-07 U
Implemented mutators and accessors and field attributes
"""
class Field:
    hidden = False #optional: boolean
    longname = "" #required: string
    mask = 0 #optional: bytes
    name = "" #required: string
    pos = 0 #required: bytes
    show = "" #required: string
    showdtl = "" #optional: string
    
    def __init__(self,n,p,s,sd,h,l):
        self.name = n
        self.hidden = h
        self.pos = p
        self.show = s
        self.showdtl = sd
        self.longname = l
    
    def getName(self):
        return self.name
    def isHidden(self):
        return self.hidden
    def getPos(self):
        return self.pos
    def getShow(self):
        return self.show

    """ Updating the Field (done only by the Formatter) """
    def setName(self,n):
        self.name = n
    def hide(self):
        self.hidden = True
    def unHide(self):
        self.hidden = False
    def setMask(self,m):
        self.mask = m
    def setPos(self,p):
        self.pos = p
    def setShow(self,s):
        self.show = s
    def setShowdtl(self,sd):
        self.showdtl = sd
    def setLongname(self,l):
        self.longname = l
    
    pass #end Field class