# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:39:20 2017

@author: admin
"""


class Hook:

    def __init__(self, field, path):
        self.field = field
        self.path = path

    def getField(self):
        #return self.field.getFieldName() <- returns the field NAME
        return self.field #returns the actual field
        
    def getPath(self):
        return self.path

    def runScript(self):
        execfile(self.path)

from Field import Field
field2 = Field("len", "", "")
field2.getFieldName()
hook1 = Hook(field2, "sample_script.py")
#print(hook1.getPath())
hook1.runScript()