# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""

import random

class oscilloscope_rf():
    """ Class to interface the Agilent Technologies DSO1024A to controll the RF voltage
    
        usage:
        to fill later
    """
    def __init__(self):

        print('started oscilloscope_rf')       
        
        
    def get_frequency(self):
        
        # return random number between 19 000 000 and 20 000 000
        a = 19000000
        b = 1000000*random.random()
        
        freq = a + b
        
        return freq
    
    def get_amplitude(self):
        
        # return random number between 400 and 800
        a = 400
        b = 400*random.random()
        
        ampl = a + b
        
        return ampl
        
    def get_peak_to_peak(self):
        
        # return random number between 400 and 800
        a = 400
        b = 400*random.random()
        
        ptp = a + b
        
        return ptp
        
    def get_rms(self):
        
        # return random number between 400 and 800
        a = 17
        b = 1*random.random()
        
        rms = a + b
        
        return rms
        
        
    def get_scale(self):
        
        # return random number between 0 and 1
        scale = random.random()
        
        return scale
        
    def quit_connection(self):
        
        print('closed osci connection')