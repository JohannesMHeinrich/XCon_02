# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:55:29 2017

@author: Manip
"""

import random

class oven_power_supply():
    """ Class to interface the coils current supply
    
        usage:
        to fill later
    """
    def __init__(self): 

        print('started oven_power_supply')       
            

    # return name of device  
    def get_name(self):       
        tmp = 0
        return tmp


    
    # ch is the channel to sleect: 1, 2 or 3            
    def select_channel(self,ch):                
        ch = 1
 


    # i is the current in mA        
    def set_current(self,i):
        i = 1

    # i is the current in mA        
    def measure_current(self):
        tmp = 1
        return tmp
        
            
        
    # v is the voltage in V     
    def set_voltage(self,v):     
        v = 1



    # output status = ON or OFF: 
    def measure_voltage(self):     
        tmp = 1
        return tmp



    # output status = ON or OFF: 
    def set_output(self,status):     
        tmp = 1



    # close the device 
    def close(self):
        tmp = 1


############################################# not used
    # v is the voltage in V     
    def set_voltage_def(self):     
        tmp = 1


    # set volt range    
    def set_voltage_range_max(self):     
        tmp = 1

    # set over voltage protection    
    def set_voltage_op(self):
        tmp = 1

    def ask_channel(self):
        tmp = 1
        return tmp



    def clear_all(self):                
        tmp = 1
        return tmp