# -*- coding: utf-8 -*-
"""
@author Ivonne Lopez
@created 04-18 T
"""

class Formatter:

    def __init__(self, rules, file):
        self.rules = rules
        self.file = file
    
#def applyRules(self, rules, file)

    def addRule(self, rule):
        self.rules.append(rule)

    def deleteRule(self):
        del self.rules[-1]

    def printListOfRules(self) :
        print(self.rules)


# Testing
formatter1 = Formatter(["rule1", "rule2"], "cubic.pdml")
formatter1.addRule("rule3")
formatter1.printListOfRules()
formatter1.deleteRule()
formatter1.printListOfRules()

