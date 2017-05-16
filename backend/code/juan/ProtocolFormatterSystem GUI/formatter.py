#!/usr/bin/python
import xml.etree.ElementTree as xml

class Formatter:
	
	root = xml.Element("rule")
	filterElement = xml.Element("filter")
	root.append(filterElement)
	
	def __init__(self):
		Formatter.root = xml.Element("rule")
		Formatter.filterElement = xml.Element("filter")
		Formatter.root.append(Formatter.filterElement)
		
	def appendAnnotation(self,name,value,annotation):
		#ANNOTATION
		actionElement = xml.SubElement(Formatter.filterElement, "action")
		actionElement.set("type", "annotation")
		actionElement.set("name",name)
		actionElement.set("value",value)
		actionElement.set("annotation",annotation)
		
	def appendHide(self,name,value):
		#HIDE
		actionElement = xml.SubElement(Formatter.filterElement, "action")
		actionElement.set("type", "hide")
		actionElement.set("name",name)
		actionElement.set("value",value)
		
	def appendHook(self,path,name,value):
		#HOOK
		actionElement = xml.SubElement(Formatter.filterElement, "action")
		actionElement.set("type", "hook")
		actionElement.set("path", path)
		actionElement.set("name",name)
		actionElement.set("value", value)
		
	def appendRename(self,name,value):
		#REMANE
		actionElement = xml.SubElement(Formatter.filterElement, "action")
		actionElement.set("type", "rename")
		actionElement.set("name",name)
		actionElement.set("value",value)
		
	def createFormatter(self):
		tree = xml.ElementTree(Formatter.root)
		#tree.write('./formatter/%r.xml' % formatterName)
		tree.write('temporalFormatter.xml')

