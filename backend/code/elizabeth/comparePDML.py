# -*- coding: utf-8 -*-
"""
Created on Sat May 06 16:52:00 2017

@author: Ivonne Lopez

Method to compare a PDML and its historical copy.
@returns list of lines that contain differences
"""

import difflib

def comparePDML(file):
    lines = []
    filename = file.split(".")
    filename = filename[0] + "_historical.pdml"
    with open(file,'r') as f1, open(filename,'r') as f2:
        diff = difflib.ndiff(f1.readlines(),f2.readlines())    
        for i,line in enumerate(diff):
            if line.startswith('-'):
                #sys.stdout.write('My count: {}, text: {}'.format(i,line))
                lines.append(i)
        #print(lines)
        return lines

listOfDifferences = comparePDML("cubic.pdml")
print(listOfDifferences)
