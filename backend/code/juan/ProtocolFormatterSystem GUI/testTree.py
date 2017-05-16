#!/usr/bin/python
import xml.etree.ElementTree as xml

root = xml.Element("rule")
filterElement = xml.Element("filter")
root.append(filterElement)

#ANNOTATION
actionElement = xml.SubElement(filterElement, "action")
actionElement.set("name", "num")
actionElement.set("value", "1")
actionElement.set("type", "annotation")

#HIDE
actionElement = xml.SubElement(filterElement, "action")
actionElement.set("type", "hide")

#HOOK
actionElement = xml.SubElement(filterElement, "action")
actionElement.set("type", "hook")
actionElement.set("path", "num")
actionElement.set("value", "1")
actionElement.set("input", "1")

#REMANE
actionElement = xml.SubElement(filterElement, "action")
actionElement.set("name", "num")
actionElement.set("value", "1")
actionElement.set("type", "rename")

tree = xml.ElementTree(root)
tree.write('output.xml')


 
