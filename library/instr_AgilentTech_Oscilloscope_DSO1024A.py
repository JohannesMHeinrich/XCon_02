# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""

import visa


class oscilloscope_rf():
    """ Class to interface the Agilent Technologies DSO1024A to controll the RF voltage
    
        usage:
        to fill later
    """
    def __init__(self):

        # open the connection to the oscilloscope
        self.rm = visa.ResourceManager()   
        self.inst = self.rm.open_resource('USB0::0x0957::0x0588::CN49181139::INSTR', write_termination = '\n', timeout=10000)


        # check if connection is working    
        try:
            tmp = self.inst.query("*IDN?")
            print('oscilloscope_rf online: ' + str(tmp)[0:29])
            
            self.inst.write(":CHANnel2:PROBe 10X")
            self.inst.write(":CHANnel2:SCALe 10")
            self.inst.write(":CHANnel2:OFFSet 0.0")
            print('oscilloscope_rf parameters set')
            
        except visa.VisaIOError:         # check that for the right value
            
            print('oscilloscope_rf OFFLINE!')


    
        # make sure the scope probe is set to the right value
        #self.inst.write(":KEY:AUTO")
        #self.inst.write(":AUToscale:ENABLE")
        #print(inst.query("*IDN?"))
        #inst.write(":CHANnel1:DISPlay OFF")
        #inst.write(":CHANnel2:DISPlay ON")
        #inst.write('*RST')
        #units = inst.query(":CHANnel2:UNITs?")
        #print(units)         
        
        
    def get_frequency(self):
        
        freq = self.inst.query(":MEASure:FREQuency? CHANnel2")
        
        return freq
    
    def get_amplitude(self):
        
        ampl = self.inst.query(":MEASure:VAMPlitude? CHANnel2")
        
        return ampl
        
    def get_peak_to_peak(self):
        
        ptp = self.inst.query(":MEASure:VPP? CHANnel2")
        
        return ptp
        
    def get_rms(self):
        
        rms = self.inst.query(":MEASure:VRMS? CHANnel2")
        
        return rms    
        
    def get_scale(self):
        
        scale = self.inst.query(":CHANnel2:SCALe?")
        
        return scale
        
    def quit_connection(self):
        
        self.inst.close()