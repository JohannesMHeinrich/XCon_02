# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""


from PyDAQmx import *
import numpy

class AnalogInput():
    """
    Reads several analog channels of NI6010 card defined as a tuple like
    (0,) for channel 0 only
    (1,2,3) for channels 1,2 and 3
     
    voltage_range can only be +/- 5 V, +/- 1 V and +/- 0.2 V     

    coupling
    referenced single ended mode : DAQmx_Val_RSE in CreateAIVoltageChan
    differential  (default value): DAQmx_Val_Cfg_Default
                                   this couples inputs 0-8, 1-9, ... 7-15
    """

    def __init__(self, device_list, voltage_range = 5,coupling = DAQmx_Val_Cfg_Default):
        taskHandle = TaskHandle(0)
        DAQmxCreateTask("",byref(taskHandle))

        number_channel = len(device_list)

        self.data_size = number_channel
        
        
        
        device=""
        
        for i_list in range(len(device_list)):        
            device=device+"Dev1/ai"+str(device_list[i_list])+","
            
        device=device[0:len(device)-1]
        
        #print(number_channel,"channel(s):",device)
             
        DAQmxCreateAIVoltageChan(taskHandle,device,"",coupling,-voltage_range,voltage_range,DAQmx_Val_Volts,None)
        
        self.taskHandle = taskHandle
        self.device_list = device_list


    # DAQmx Read Code     
    def read(self):
        DAQmxStartTask(self.taskHandle)
        read = int32()
        number_channel=len(self.device_list)
        data_size=number_channel
        data = numpy.zeros((data_size,), dtype=numpy.float64)
        DAQmxReadAnalogF64(self.taskHandle,1,10.0,DAQmx_Val_GroupByChannel,data,data_size,byref(read),None)
        
        
        return data
        
        
    def clear(self):
        DAQmxClearTask(self.taskHandle)