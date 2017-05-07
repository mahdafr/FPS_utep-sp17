# -*- coding: utf-8 -*-
"""
Created on Sat May 06 17:28:05 2017

@author: Ivonne Lopez
"""

f = open("test1.txt",'r')
filedata = f.read()
f.close()

newdata = filedata.replace("something","num")

f = open("test1.txt",'w')
f.write(newdata)
f.close()
