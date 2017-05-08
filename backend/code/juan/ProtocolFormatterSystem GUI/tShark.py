#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author Juan Martinez
@created 04-18 T
"""
import commands
import os
class Tshark:
	""" Contract 27: Convert PCAP to PDML """
# @requires File extension of a file to be a pcap for the second parameter and a PDML for the third parameter
# @ensures tShark returns no error on accepting the PDML file to parse
	def pcapToPDML(self,pcapfilename,pdmlFile):
		isFileConverted = False
		""" Receives a PCAP file to be parsed by the tShark tool """
		commands.getoutput('tshark -T pdml -r %r -V | tee %r' % {pcapfilename, pdmlFile})
		isFileConverted = os.path.isfile('./%r' % convertedFilename)
		return isFileConverted