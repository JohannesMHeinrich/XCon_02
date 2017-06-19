# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 15:41:48 2016

@author: JohannesMHeinrich
"""

import visa


class ion_pump_SPC():
    """ Class to interface the ion pump
    
        usage:
        to fill later
    """
    def __init__(self): 

        # open the connection to the oscilloscope
        self.rm = visa.ResourceManager()   
        self.inst = self.rm.open_resource('ASRL7::INSTR', read_termination = '\r', timeout=5000)
        
# working commands which might be useful        
#        print(self.inst.query('~ 01 01 22'))
#        print(self.inst.query('~ 01 0B 33'))
    
    
# check if connection is working    
#        try:
#            self.inst.query('~ 01 01 22')
#            print('ion_pump_SPC online')
#        
#        except visa.VisaIOError:         # check that for the right value
#            
#            print('ion_pump_SPC OFFLINE!')

      
    def read_pressure(self):
        
        p = self.inst.query('~ 01 0B 33')
        
        strip_first_part = p.replace("01 OK 00 ", "")      
        with_stripped_second_part = strip_first_part[:-6]      
        
        return float(with_stripped_second_part)



# this was used to find the right hex code -----------------------------------
#
#
#    def tryal_function(self):
#        print(self.inst.query('~ 01 0B '+self.try_thing))
#
#literals = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
#
#for i in range(len(literals)):
#    for j in range(len(literals)):
#        device.try_thing = str(literals[i]) + str(literals[j])
#        
#        print(device.try_thing)
#        try:
#            device.tryal_function()
#            
#            with open("testthingy.txt", "a") as myfile:
#                myfile.write(str(device.try_thing) + ',' + 'worked!' + '\n')                    
#            break
#        
#        except visa.VisaIOError:
#            
#            print('did not work')
#            with open("testthingy.txt", "a") as myfile:
#                myfile.write(str(device.try_thing) + ',' + '\n') 