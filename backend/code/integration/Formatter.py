# -*- coding: utf-8 -*-
"""
@author Ivonne Lopez
@created 04-18 T


@modified mafravi on 05-07 S made into a class and added Protocol
"""
import Rule

class Formatter:
    rule = [] #Rule: the set of Rules for
    file = "" #String: file name
    protocol = "" #String: the procol this Formatter is for
    
    def __init__(self, file, pName):
        self.rule = []
        self.file = file
        self.protocol = pName

    def addRule(self, r: Rule):
        self.rule.append(r)

    def deleteRule(self):
        del self.rule[-1]

    def printListOfRules(self) :
        print(self.rule)
    
    """
    # Testing
    formatter1 = Formatter(["rule1", "rule2"], "cubic.pdml")
    formatter1.addRule("rule3")
    formatter1.printListOfRules()
    formatter1.deleteRule()
    formatter1.printListOfRules()
    """