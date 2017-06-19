# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""


import random

class AnalogInput():
    """
    Reads several analog channels of NI6010 card defined as a tuple like
    (0,) for channel 0 only
    (1,2,3) for channels 1,2 and 3
     
    voltage_range can only be +/- 5 V, +/- 1 V and +/- 0.2 V     

    coupling
    referenced single ended mode : DAQmx_Val_RSE in CreateAIVoltageChan
    differential  (default value): DAQmx_Val_Cfg_Default
                                   this couples inputs 0-8, 1-9, ... 7-15
    """

    def __init__(self, device_list, voltage_range = 5,coupling = 0):

        number_channel = len(device_list)
        n2 = voltage_range
        n3 = coupling
        
        print('AnalogInput: ' + str(number_channel) + '   ' + str(n2) + '   ' + str(n3))



     
    def read(self):
        
        # return random number between -5 and 5
        a = -5
        b = 10*random.random()
        
        volt = a + b
        
        return [volt]
        
        
    def clear(self):
        print('closed connection AnalogInput')