# -*- coding: utf-8 -*-
"""
Created on Sat May 20 14:59:49 2017

@author: JohannesMHeinrich
"""

from time import localtime, strftime
from ctypes import *

import time

dll_HF = windll.LoadLibrary("C:\\Windows\\System32\\wlmData.dll")

    
#import numpy as np
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
    
class HighFinesse_WM():
    """ Class to interface the HighFinesse_WM
    
        usage:
        to fill later
    """
    def __init__(self):
            
        print('HighFinesse WM initialized')
        
        # the ControlWLM/Ex functions start, hide or terminate the WL server application
#        Action = 'cCtrlWLMHide'
#        control_show = dll_HF.ControlWLM(Action, None, None)
#        
#        print(control_show)

        
    def get_frequency(self):

        dll_HF.GetFrequency.restype=c_double
        
        frequency = c_double()
        frequency = dll_HF.GetFrequency(frequency)
   
        print(frequency)

        return frequency

        
        
        
    def get_wavelength(self):

        dll_HF.GetWavelength.restype=c_double
        
        wavelength = c_double()
        wavelength = dll_HF.GetWavelength(wavelength)

        return wavelength

              
              
    def get_temperature(self):
        
        dll_HF.GetTemperature.restype=c_double
        
        temperature = c_double()
        temperature = dll_HF.GetTemperature(temperature)

        return temperature






#wv = HighFinesse_WM()
#a = []
#for i in range(50):
#    b = wv.get_frequency()
#    time.sleep(0.1)
#    a.append(b)
#    
#import numpy as np
#import matplotlib.pyplot as plt
#
#x = np.arange(0, 50, 1);
#
#plt.plot(x, a)
#plt.show()