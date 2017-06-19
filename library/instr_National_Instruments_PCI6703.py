# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""


import numpy as np
from PyDAQmx import *

class VoltUpdate():
    """ Class to output a single Voltage Update to an Analog Output Channel
    
    Usage:  dcvolt = VoltUpdate(volt(default = 0.0), aochannel(default = "Dev3/ao0"))
            dcvolt.start()
            dcvolt.clear()
    """
    
    def __init__(self, volt=0.0 , aochannel="Dev3/ao0"):
        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))
        DAQmxCreateAOVoltageChan(taskHandle,aochannel,"",-10.0,10.0,DAQmx_Val_Volts,"")
        self.taskHandle = taskHandle
        self.voltage = np.array([volt])
        
        self.start()
        self.clear()
    def start(self):
        DAQmxStartTask(self.taskHandle)
        DAQmxWriteAnalogF64(self.taskHandle,1,1,10.0,DAQmx_Val_GroupByChannel,self.voltage,None,None)
    def clear(self):
        DAQmxClearTask(self.taskHandle)