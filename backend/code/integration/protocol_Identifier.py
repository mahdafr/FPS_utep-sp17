#!/usr/bin/python

#Search for the protocol names in the Caplture File
#@Requires a file with file extension .pdml
#@Ensures a list of non repited protoc3ols
def searchProtocols(self,filename):
	protocolList = []
	tree = ET.parse(filename)
	root = tree.getroot()
	for proto in root.iter('proto'):
		name = proto.get('name')
		if name not in protocolList:
			protocolList.append(name)
	return protocolList