# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""

class VoltUpdate():
    """ Class to output a single Voltage Update to an Analog Output Channel
    
    Usage:  dcvolt = VoltUpdate(volt(default = 0.0), aochannel(default = "Dev3/ao0"))
            dcvolt.start()
            dcvolt.clear()
    """
    
    def __init__(self, volt=0.0 , aochannel="Dev3/ao0"):
        print('starts connection analog output')
        self.start()
        self.clear()
    def start(self):
        print('sets value connection analog output')
    def clear(self):
        print('quits connection analog output')