# -*- coding: utf-8 -*-
"""
Created on Sat Feb 04 15:41:48 2016

@author: JohannesMHeinrich
"""



class scpi (object):
    """SCPI class used to access Red Pitaya over an IP network."""
    delimiter = '\r\n'

    def __init__(self, host, timeout=None, port=5000):
        print('started red pitaya connection')
            
            
        

    def rx_txt(self, chunksize = 4096):
        print('return data from red pitaya 0')
        
        a = 'Test 0'
        
        return a

    def rx_arb(self):
        print('return data from red pitaya')
        
        a = 'Test'
        
        return a

    def tx_txt(self, msg):
        print('send text to red pitaya')

    def close(self):
        print('closed red pitaya')

    def __del__(self):
        print('closed red pitaya')