# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:39:20 2017

@author: admin


@modified mafravi on 05-07 U added missing methods


RUN FOR TESTS
"""
import Field, Script

class Hook:
    field = ""
    script = ""

    def __init__(self, f: Field, s: Script):
        self.field = f
        self.script = s

    def getField(self):
        #return self.field.getFieldName() <- returns the field NAME
        return self.field #returns the actual field
        
    def getPath(self):
        return self.script.getPath()
    
    def setPath(self, p):
        self.script.setPath(p)

    def runScript(self):
        self.script.run()
    
    def getReturnValue(self):
        return self.script.getReturnValue()

"""
from Field import Field
field2 = Field("len", "", "")
field2.getFieldName()
hook1 = Hook(field2, "sample_script.py")
#print(hook1.getPath())
hook1.runScript() """