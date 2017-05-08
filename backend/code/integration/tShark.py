#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author Juan Martinez
@created 04-18 T

@modified mafravi on 05-07 S 

RUN FOR TESTS
"""
import commands
import HistoricalCopy

class TShark():
    """ Contract 27: Convert PCAP to PDML """
    # @requires File extension of a file to be a pcap for the second parameter and a PDML for the third parameter
    # @ensures tShark returns no error on accepting the PDML file to parse
    def sendPCAP(self,pcapfilename,pdmlFilename):
        """ Receives a PCAP file to be parsed by the tShark tool """
        commands.getoutput('tshark -T pdml -r %r -V | tee %r' % {pcapfilename, pdmlFilename})
    
    # @requires tShark parsed the PDML with no errors
    # @ensures a new file type of PDML is stored on the file system to be opened by PFS
    def storePDML(self,pdml):
        """ Receives a parsed PDML file and stores it on the local file system """
        HistoricalCopy.storePDML(pdml)