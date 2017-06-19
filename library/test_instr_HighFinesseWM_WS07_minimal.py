# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:59:49 2017

@author: JohannesMHeinrich
"""

import time
from time import localtime, strftime

# to make usage of the ATMCD32D.DLL
from ctypes import *

# import library ATMCD32D.DLL
dll_HF = windll.LoadLibrary("C:\\Windows\\System32\\wlmData.dll")
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
    
class HighFinesse_WM():
    """ Class to interface the HighFinesse_WM
    
        usage:
        to fill later
    """
    def __init__(self):
#        control_show = dll_HF.ControlWLM('cCtrlWLMStartSilent', 0, 0)
#        print(control_show)
        
        blub = dll_HF.Instantiate('blu2b', 0, 0, 0)     
        print(blub)
        
#        temp = self.get_temperature()       
#        print(temp)

        blu2b = c_long()
        blub = dll_HF.GetWLMVersion(blu2b)     
        print(blub)
        print(blu2b)

        
        
        
    ###########################################################################
    # my own function initialize. starts the camera and puts it into a loop ### 
    ###########################################################################        

    def my_initialize(self):
        
        self.initialize()
        
        self.set_read_mode(self.read_mode)
        self.set_image()
        self.set_acquisition_mode(self.acquisition_mode)
        
        self.set_temperature(self.wanted_temperature)
        self.set_shutter_ex()
        
        self.cooler_on()
              
    #          
    def get_temperature(self):
        # declare ctype c_int for later use?
        temperature = c_double()
        status = dll_HF.GetTemperature(temperature)

        return temperature
        
new_wm = HighFinesse_WM()