#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author Juan Martinez
@created 04-18 T
"""
import commands
""" Contract 27: Convert PCAP to PDML """
# @requires the tile has not been opened by PFS before
# @ensures tShark returns no error on accepting the PDML file to parse
def sendPCAP(pcap,pdmlName):
	""" Receives a PCAP file to be parsed by the tShark tool """
	pcapFile = '27.pcap'
	pdmlFile = 'untitled1.pdml'
	commands.getoutput('tshark –r %r -T %r')

# @requires tShark parsed the PDML with no errors
# @ensures a new file type of PDML is stored on the file system to be opened by PFS
def storePDML(pdml):
	""" Receives a parsed PDML file and stores it on the local file system """