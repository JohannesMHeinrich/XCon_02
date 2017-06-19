# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 13:55:29 2017

@author: Manip
"""

import visa

class oven_power_supply():
    """ Class to interface the coils current supply
    
        usage:
        to fill later
    """
    def __init__(self): 

        # open the connection to the oscilloscope
        self.rm = visa.ResourceManager()
        self.inst = self.rm.open_resource('USB0::0x05E6::0x2230::9104059::INSTR', write_termination = '\n', timeout=10000)


       
        # check if connection is working    
        try:
            tmp = self.inst.query("*IDN?")
            print('power_supply online: ' + str(tmp)[0:31])
        
        except visa.VisaIOError:         # check that for the right value
            
            print('power_supply OFFLINE!')
            

    # return name of device  
    def get_name(self):       
        tmp = self.inst.query('*IDN?')
        
        return tmp


    
    # ch is the channel to sleect: 1, 2 or 3            
    def select_channel(self,ch):                
        tmp = self.inst.write('INSTrument:SELect CH' + str(ch))
 


    # i is the current in mA        
    def set_current(self,i):
        tmp = self.inst.write('CURRent ' + str(i) + 'A')



    # i is the current in mA        
    def measure_current(self):
        tmp = self.inst.query('MEASure:CURRent?')
        return tmp
        
            
        
    # v is the voltage in V     
    def set_voltage(self,v):     
        tmp = self.inst.write('VOLTage ' + str(v) + 'V')



    # output status = ON or OFF: 
    def measure_voltage(self):     
        tmp = self.inst.query('MEASure:VOLTage?')
        return tmp



    # output status = ON or OFF: 
    def set_output(self,status):     
        tmp = self.inst.write('OUTPut ' + str(status))        



    # close the device 
    def close(self):
        self.inst.close()  


############################################# not used
    # v is the voltage in V     
    def set_voltage_def(self):     
        tmp = self.inst.write('VOLTage DEF')        



    # set volt range    
    def set_voltage_range_max(self):     
        tmp = self.inst.write('VOLTage:RANGe 5.5V')
   


    # set over voltage protection    
    def set_voltage_op(self):     
        tmp = self.inst.write('VOLT:PROT 6V')
        tmp2 = self.inst.write('VOLT:PROT:STAT 0')
        
        

    def ask_channel(self):                
        tmp = self.inst.query('INSTrument:SELect?')
            
        return tmp



    def clear_all(self):                
        tmp = self.inst.query('*CLS')
            
        return tmp