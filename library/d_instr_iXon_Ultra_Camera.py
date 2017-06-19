# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:59:14 2017

@author: JohannesMHeinrich
"""
import time
from time import localtime, strftime

from ctypes import *
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

import random
    
class iXon_Ultra_camera():
    """ Class to interface the camera
    
        usage:
        to fill later
    """
    def __init__(self):
        # the parameters to start the camera
        # to set the image right inside the camera
        self.image_width = 512
        self.image_height = 512
        
        # create "array" in python to collect data - this array here is for one picture
        self.n_pixel = self.image_width * self.image_height
        self.data = (c_long * self.n_pixel)()
        
        self.data[131072] = 500

        self.current_temperature = 23
        self.temp_list = []
    
        # just to test if cam is online               
        self.get_available_cameras()


    ###########################################################################
    # CREATE COMPLETE OWN PROGRAM - ONLY MINIMAL OUTPUT TO THE OUTSIDE ######## 
    ###########################################################################

        # MY OWN FUNCTION INIT??????????? with while and stuff? start with init, then while, then if cases for different modi operandi. this function will be threated when intialized!
        # THATS NOT A FUNCTION INIT; THATS AN FUNCTION OPERATION MODI for all different sets of flags through interface. take care of abortion with the temperature.
        # output is the data when called, the thread opareats depending on the flags from the outside


        self.acquisition_mode = 1
        self.read_mode = 4
        self.flag_my_init = True
        self.flag_modus = 0
        self.flag_trig_pic = 0
        self.exposure_time = 0.001
        
        
        self.wanted_temperature = -10
        
        

    def my_initialize(self):
        
        self.initialize()
        
        self.set_read_mode(self.read_mode)
        self.set_image()
        
        while self.flag_my_init == True:
            
            ###########################################################################
            if self.flag_modus == 0: # no mode selected - allow access to temperature and deliver temp data  
                
                while self.flag_modus == 0:   
                    
                    temp = self.get_temperature()
    
                    time.sleep(0.5)
                    print(temp)
                    
                    if self.flag_my_init == False:
                        break
            ###########################################################################                    
            elif self.flag_modus == 1: # mode single pic selected - allow in addition to set stuff 
            
                self.set_acquisition_mode(self.acquisition_mode)
                
                while self.flag_modus == 1:
                    
                    if self.flag_trig_pic == 0: # give temp and status
                    
                        while self.flag_trig_pic == 0:  
                            
                            temp = self.get_temperature()
                            
                            time.sleep(0.5)
                            print('blub')
                            
                            if self.flag_my_init == False:
                                break
                            if self.flag_modus != 1:
                                break
                            
                        if self.flag_my_init == False:
                            break
                            
                    else:   # set flat_trig_pic back and start acquisition
                        self.set_exposure_time(self.exposure_time)
                        self.start_acquisition()
                        self.wait_for_acquisition()
                        self.get_most_recent_image()
                        self.flag_trig_pic = 0
                        print('single picture made') # timestamp and stuff
            ###########################################################################                    
            elif self.flag_modus == 2: # mode continous single pic selected - my own mode
            
                self.set_acquisition_mode(self.acquisition_mode)
                
                while self.flag_modus == 2:
                    
                    self.set_exposure_time(self.exposure_time)
                    self.start_acquisition()
                    self.wait_for_acquisition()
                    self.get_most_recent_image()
                    print('cont pics picture made') # timestamp and stuff
                    
                    if self.flag_my_init == False:
                        break
                    
            ###########################################################################                            
            elif self.flag_modus == 5: # mode continuus pic selected
                print('continuus mode pictures')
            ###########################################################################   
            elif self.flag_modus == 6: # mode continuus pic selected ownmade
            
                self.set_acquisition_mode(self.acquisition_mode)
                self.set_exposure_time(self.exposure_time)
                
                while self.flag_modus == 6:
                    
                    self.start_acquisition()
                    self.wait_for_acquisition()
                    self.get_most_recent_image()
                    
                    if self.flag_my_init == False:
                        break
            ###########################################################################
                
                
                
        self.shut_down() # benötigt noch den temperatur quatsch!
        self.flag_my_init = True # für den nächsten start. zum abbrechen ssetze vona außen auf False  
        




 
  
  
    ###########################################################################
    # the intrinsic functions, translated to python ########################### 
    ###########################################################################
 
    # page 114: unsigned int WINAPI GetAvailableCameras(long* totalCameras)
    def get_available_cameras(self):
        print('check for available cameras:')        
       
        status = c_long(0)
        
        tmp = 20002

        # check if get_status worked
        if tmp == 20002:
            print('-> number of available cameras: ' + str(status.value))
        else:
            print('-> some error getting the status; ' + str(tmp))          
            
    # page 199: unsigned int WINAPI Initialize(char* dir)
    def initialize(self): 
                
        tmp = 20002
        
        # check if initialization worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera initialized')
        elif tmp == 20003:
            print('DRV_VXDNOTINSTALLED; maybe camera off?..')
        else:
            print('some error initializing the camera; ' + str(tmp))
            
    # page 295: unsigned int WINAPI SetTemperature(int temperature)         
    def set_temperature(self,T):
        tmp = T
        
    
    # page 189: unsigned int WINAPI GetTemperature(int* temperature)          
    def get_temperature(self):
        # declare ctype c_int for later use?
        status = float(random.random()*-20-10)
        
        return status
        
    # page 104: unsigned int WINAPI CoolerON(void)
    def cooler_on(self):
        print('cooler on')         
     
    # page 103: unsigned int WINAPI CoolerOFF(void)
    def cooler_off(self):
        print('cooler off')                  
        
    # page 285: unsigned int WINAPI SetReadMode(int mode)
    def set_read_mode(self,n):
        #  0 = Full Vertical Binning, 1 = Multi-Track, 2 = Random-Track, 3 = Single-Track, 4 = Image
        tmp = 20002

        # check if set read mode worked
        if tmp == 20002:
            print('DRV_SUCCESS; read mode set to: ' + str(n))
        else:
            print('some error setting the camera image; ' + str(tmp))

    # page 268: unsigned int WINAPI SetImage(int hbin, int vbin, int hstart, int hend, int vstart, int vend)
    def set_image(self):
        # int hbin, int vbin, int hstart, int hstop, int vstart, int vstop
        tmp = 20002
        
        # check if image setting worked
        if tmp == 20002:
            print('DRV_SUCCESS; all parameters for camera image accepted')
        else:
            print('some error setting the camera image; ' + str(tmp))               

    # page 226: unsigned int WINAPI SetAcquisitionMode(int mode)                              
    def set_acquisition_mode(self,n):
        # acquisition_mode accepts n: 1 = Single Scan, 2 = Accumulate, 3 = Kinetics, 4 = Fast Kinetics , 5 = Run till abort     
        tmp = 20002

        # check if set_acquisition_mode worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_acquisition_mode to: ' + str(n))
        else:
            print('some error setting the camera mode; ' + str(tmp)) 

    # page 256: unsigned int WINAPI SetExposureTime(float time)
    def set_exposure_time(self,t):

        tmp = 20002

        # check if set_exposure_time worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_exposure_time to: ' + str(t))
        else:
            print('some error setting the camera exposure time; ' + str(tmp))

    # page 278: unsigned int WINAPI SetNumberAccumulations(int number) 
    def set_number_accumulations(self,n):
        # int number n: number of scans to accumulate    
        tmp = 20002
        
        # check if set_number_accumulations worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_number_accumulations to: ' + str(n))
        else:
            print('some error setting the camera set_number_accumulations; ' + str(tmp))

    # page 225: unsigned int WINAPI SetAccumulationCycleTime(float time)
    def set_accumulation_cycle_time(self,t):
        # float time: the accumulation cycle time in seconds
        tmp = 20002
        
        # check if set_accumulation_cycle_time worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_accumulation_cycle_time to: ' + str(t))
        else:
            print('some error setting the camera set_accumulation_cycle_time; ' + str(tmp))

    # page 278: unsigned int WINAPI SetNumberKinetics(int number)
    def set_number_kinetics(self,n):
        # int number: number of scans to store
        tmp = 20002
        
        # check if set_number_kinetics worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_number_kinetics to: ' + str(n))
        else:
            print('some error setting the camera set_number_kinetics; ' + str(tmp))

    # page 274: unsigned int WINAPI SetKineticCycleTime(float time)
    def set_kinetic_cycle_time(self,t):
        # float time: the kinetic cycle time in seconds
        tmp = 20002
        
        # check if set_kinetic_cycle_time worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_kinetic_cycle_time to: ' + str(t))
        else:
            print('some error setting the camera set_kinetic_cycle_time; ' + str(tmp))

    # page 303: unsigned int WINAPI StartAcquisition(void)
    def start_acquisition(self):
       
        tmp = 20002

        # check if set_acquisition_mode worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera started acquisition:')
        else:
            print('some error starting the acquisition; ' + str(tmp))
            
    # page 110: unsigned int WINAPI GetAcquiredData(at_32* arr, unsigned long size)
    def get_acquired_data(self,m_data,m_pixels):
       
        tmp = 20002

        # check if set_acquisition_mode worked
        if tmp == 20002:
            print('DRV_SUCCESS; got the data:')
        else:
            print('some error getting the data; ' + str(tmp))
            
    # page 169: unsigned int WINAPI GetMostRecentImage(at_32* arr, unsigned long size)        
    def get_most_recent_image(self):
     
        tmp = 20002
        
        py_data = []
        for j in range(512):
            vec = []
            for i in range(512):
                vec.append(int(random.random()*500+500))
            py_data.append(vec)
        
        # check if get_most_recent_image worked
        if tmp == 20002:
            print('DRV_SUCCESS; got the most recent image:')
        else:
            print('some error getting the most recent image; ' + str(tmp))
            
        self.data = py_data
        
        return py_data
             
    # page 187: unsigned int WINAPI GetStatus(int* status)     
    def get_status(self):
        # This function will return the current status of the Andor SDK system.
        # This function should be called before an acquisition is started to
        # ensure that it is IDLE and during an acquisition to monitor the process
        status = c_int()
        
        tmp = 20002

        # check if get_status worked
        if tmp == 20002:
            print('DRV_SUCCESS; got the status: ' + str(status))
        else:
            print('some error getting the status; ' + str(tmp))            

    # page 305: unsigned int WINAPI WaitForAcquisition(void)
    def wait_for_acquisition(self):
        print('wait_for_acquisition')

    # page 102: unsigned int WINAPI AbortAcquisition(void)
    def abort_acquisition(self):
        print('abort_acquisition')      
    
    # page 302: unsigned int WINAPI ShutDown(void)
    def shut_down(self):
        print('iXon_Ultra_camera closed')           

    ###########################################################################
    # END intrinsic functions ################################################# 
    ###########################################################################










#    def save_as_bmp(self):
#       
#        tmp = dll_Andor.SaveAsBmp('C:/Users/Manip/Documents/Python/XCon/2017_02_14_XCon_01_new/pic2.bmp','GREY.PAL',c_long(self.bmp_contrast_min),c_long(self.bmp_contrast_max))      
#
#        # check if saving worked
#        if tmp == 20002:
#            print('DRV_SUCCESS; saved the bmp')
#        else:
#            print('some error saving the bmp; ' + str(tmp))
            

      


    def save_as_png(self):
        py_data = np.array(self.data).reshape(self.image_width, self.image_height)        
        test = plt.imshow(py_data, cmap=cm.gray, vmin=500, vmax=1000, extent=(1, self.image_width, 1, self.image_height), origin='lower')
#        print(py_data)
#        print(py_data[0])
        now = str(strftime("%Y_%m_%d_%H%M%S", localtime()))
        
        name = now + '_cam.png'
        
        plt.savefig(name)






# def GetAcquisitionTimings
# set_number_accumulations # default is one, one image per point in the series
# def get_images (p166)  