#!/usr/bin/env python3
"""
@author Gerardo Fang
@created 04-18 T
@lastmod 04-21 F

@modified 05-07 U 


RUN FOR TESTS
"""
import glob, os, shutil

class HistoricalCopy():
    
    """ Contract 12: Manage Historical Copy """
    # @requires the file to be of type PDML
    # @ensures 
    def createHistoricalCopy(self,pdml):
        """ Receives a PDML file and creates a historical copy"""
        #Useful for the GUI maybe?    
        ##from tkinter import filedialog
        #root = tk.Tk()
        #root.withdraw()
        #file_path = filedialog.askopenfilename()
        
        dst = "where the PDML historicals will be stored"
        shutil.copy2(pdml,dst)
         
        for filename in glob.iglob(os.path.join(dst,'*.pdml')):
            historicalname = '_historical.pdml'
            if historicalname not in filename:
                os.rename(filename, filename[:-5] + '_historical.pdml')
                return True
    
    
    # @requires the file has not been opened by PFS before
    # @ensures 
    def storePDML(self,pdml):
        """ Receives a PDML file and stores it on the local system """
        dst = "where the modified PDMLs will be stored"
        shutil.copy2(pdml,dst)
        return True