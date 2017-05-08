# -*- coding: utf-8 -*-
"""
@author Ivonne Lopez
@created 04-18 T


@modified mafravi on 05-07 U added missing operations and attributes


RUN FOR TESTS
"""
import os.path
import os

class Script:
    path = "" #String: path of this Script in the system
    file = "" #File: r/w by the Script
    returnValue = "" #

    def __init__(self, p):
        if(os.path.exists(p)):
            f = open(p, "r+")
        else:
            f = open(p, "w")
        self.path = p
        self.file = f
    
    def setPath(self,p):
        self.path = p

    def run(self):
        exec(self.returnValue = open(self.path).read()) #run the script
        pass

    def getReturnValue(self):
        return self.returnValue

    def getPath(self):
        return self.path

    def printFile(self):
        file_contents = self.file.read()
        print (file_contents)

"""
script1 = Script("lol.txt")
script1.printFile()
"""