# -*- coding: utf-8 -*-
"""
@author Ivonne Lopez
@created 04-18 T
"""

class Field:

    def __init__(self, name, hook, annotation):
        self.fieldDisplay = True
        self.name = name
        self.hook = ""
        self.hasHook = False
        self.annotation = ""
        self.hasAnnotation = False

    def getFieldName(self):
        print("Field name is:", self.name)
        return self.name

    def isFieldDisplayed(self):
        print("Field is displayed:", self.fieldDisplay)
        return self.fieldDisplay

    def getHook(self):
        if self.hasHook:
            print("Field has hook:", self.hook)
        else:
            print("Field has no hook")
        return self.hook

    def getAnnotation(self):
        if self.hasAnnotation:
            print("Field has annotation:", self.annotation)
        else:
            print("Field has no annotation")
        return self.annotation

    def hasHookField(self):
        return self.hasHook

    def hasAnnotationField(self):
        return self.hasAnnotation

    def showField(self):
        if self.fieldDisplay is False:
            self.fieldDisplay = True
            return True
        else:
            return False

    def hideField(self):
        if self.fieldDisplay is True:
            self.fieldDisplay = False
            return True
        else:
            return False

    def renameField(self, action, name):
        if action == "rename_field" :
            self.name = name

    def addHook(self, action, hook):
        if action == "add_hook":
            self.hook = hook
            self.hasHook = True

    def addAnnotation(self, action, annotation):
        if action == "add_annotation":
            self.annotation = annotation
            self.hasAnnotation = True

# Testing
field1 = Field("num", "", "")
field2 = Field("len", "", "")

field1.isFieldDisplayed()
field2.isFieldDisplayed()

field1.hideField()

field1.isFieldDisplayed()
field2.isFieldDisplayed()

field1.getFieldName()
field1.renameField("rename_field", "numchanged")
field1.getFieldName()

print("\nWorking with field2")
field2.getFieldName()
field2.getHook()
field2.addHook("add_hook", "bla_bla.script")
field2.getHook()
field2.getAnnotation()
field2.addAnnotation("add_annotation", "bla/bla2")
field2.getAnnotation()

print("\nWorking with field1")
field1.getFieldName()
field1.getAnnotation()
field1.addAnnotation("add_annotation", "bla/bla")
field1.getAnnotation()
