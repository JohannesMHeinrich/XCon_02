# -*- coding: utf-8 -*-
"""
Created on Sat May 04 15:41:48 2017

@author: JohannesMHeinrich
"""

import random

class piezo_fiber_laser():
    """ Class to interface piezo_fiber_laser
    
        usage:
        to fill later
    """
    def __init__(self): 


        print('thorlabs piezo_fiber_laser online:')
        print('piezo_fiber_laser at 0.0 Volt')
                  



      
    def read_voltage(self):
        
        tmp = 150*random.random()
        
        return tmp



    def set_voltage(self,voltage):      
        blub = voltage



#    def __del__(self):
#        self.inst.close()
        
     
     
     
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