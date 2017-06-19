# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 15:41:48 2016

@author: JohannesMHeinrich
"""

import random


class ion_pump_SPC():
    """ Class to interface the ion pump
    
        usage:
        to fill later
    """
    def __init__(self): 

        print('started ion_pump_SPC')
    


      
    def read_pressure(self):
        
        # return random number between 8e-10 and 9e-10
        a = 8*1e-10
        b = 1e-10*random.random()
        
        pressure = a + b
        
        return pressure
