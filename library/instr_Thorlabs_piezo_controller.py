# -*- coding: utf-8 -*-
"""
Created on Sat May 04 15:41:48 2017

@author: JohannesMHeinrich
"""

import visa
import time

class piezo_fiber_laser():
    """ Class to interface piezo_fiber_laser
    
        usage:
        to fill later
    """
    def __init__(self): 

        self.rm = visa.ResourceManager()   
        self.inst = self.rm.open_resource('ASRL5::INSTR', read_termination='\r', write_termination='\r', timeout=1000)

        # check if connection is working    
        try:
            tmp = self.read_voltage()
            print('thorlabs piezo_fiber_laser online:')
            print('piezo_fiber_laser at ' + str(tmp) + 'Volt')
            
        except visa.VisaIOError:         # check that for the right value
            
            print('piezo_fiber_laser OFFLINE!')        



      
    def read_voltage(self):
        
        tmp = self.inst.query('xvoltage?')
        
        strip_first_part = tmp.replace("[ ", "")      
        with_stripped_second_part = strip_first_part.replace("]", "")    
        with_stripped_third_part = with_stripped_second_part.replace(">", "")
        with_stripped_fourth_part = with_stripped_third_part.replace("[", "")
        
        return with_stripped_fourth_part



    def set_voltage(self,voltage):      
        self.inst.write('%s%f'%('xvoltage=',voltage))



    def __del__(self):
        self.inst.close()
        
     
     
     
#test = piezo_fiber_laser()
#
#eins = test.read_voltage()
#print(eins)
#
#time.sleep(3)
#
#test.set_voltage(80.15)
#
#time.sleep(3)
#
#zwei = test.read_voltage()
#print(zwei)