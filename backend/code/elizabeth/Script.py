# -*- coding: utf-8 -*-
"""
@author Ivonne Lopez
@created 04-18 T
"""
import os.path
import os

class Script:

    def __init__(self, fileName):
        if(os.path.exists(fileName)):
            f = open(fileName, "r+")
        else:
            f = open(fileName, "w")
        self.file = f

    def printFile(self):
        file_contents = self.file.read()
        print (file_contents)
        

script1 = Script("lol.txt")
script1.printFile()
