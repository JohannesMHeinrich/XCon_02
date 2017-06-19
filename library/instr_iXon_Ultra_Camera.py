# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 13:59:14 2017

@author: JohannesMHeinrich
"""
import time
from time import localtime, strftime

# to make usage of the ATMCD32D.DLL
from ctypes import *

# import library ATMCD32D.DLL
dll_Andor = windll.LoadLibrary("C:\Program Files\Andor SOLIS\Drivers\ATMCD32D.DLL")
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
    
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
        
        # parameters for my initialize
        self.acquisition_mode = 1
        self.read_mode = 4
        self.flag_my_init = True
        self.flag_modus = 0
        self.flag_trig_pic = 0
        self.exposure_time = 0.001
        self.current_temperature = 23
        self.temp_list = []
        self.wanted_temperature = 20   
      
        # get the number of available cameras         
        self.get_available_cameras()




        
        
        
    ###########################################################################
    # my own function initialize. starts the camera and puts it into a loop ### 
    ###########################################################################        

    def my_initialize(self):
        
        self.initialize()
        
        self.set_read_mode(self.read_mode)
        self.set_image()
        self.set_acquisition_mode(self.acquisition_mode)
        
        self.set_temperature(self.wanted_temperature)
        self.set_shutter_ex()
        
        self.cooler_on()
        
        
        
        while self.flag_my_init == True:
            
            tmp_wanted_temperature = int(self.wanted_temperature)
            self.set_temperature(tmp_wanted_temperature)
            
            ###########################################################################
            if self.flag_modus == 0: # no mode selected - allow access to temperature and deliver temp data  
                
                while self.flag_modus == 0:   
                    
                    self.current_temperature = self.get_temperature()
    
                    time.sleep(0.5)
                    
                    if self.flag_my_init == False:
                        break
                    
                    if tmp_wanted_temperature != self.wanted_temperature:
                        break
            ###########################################################################                    
            elif self.flag_modus == 1: # mode single pic selected - allow in addition to set stuff 
                
                while self.flag_modus == 1:
                    
                    if self.flag_trig_pic == 0: # give temp and status
                    
                        while self.flag_trig_pic == 0:  
                            
                            self.current_temperature = self.get_temperature()
                            
                            time.sleep(0.5)
                            
                            if self.flag_my_init == False:
                                break
                            if self.flag_modus != 1:
                                break
                            if tmp_wanted_temperature != self.wanted_temperature:
                                break
                            
                        if self.flag_my_init == False:
                            break               
                        if tmp_wanted_temperature != self.wanted_temperature:
                            break
                            
                    else:   # set flat_trig_pic back and start acquisition
                        self.set_exposure_time(self.exposure_time)
                        self.start_acquisition()
                        self.wait_for_acquisition()
                        self.get_most_recent_image()
                        self.save_as_png()
                        self.flag_trig_pic = 0
                        print('single picture made') # timestamp and stuff
            ###########################################################################                    
            elif self.flag_modus == 2: # mode continous single pic selected - my own mode
                
                while self.flag_modus == 2:
                    
                    self.current_temperature = self.get_temperature()
                    
                    self.set_exposure_time(self.exposure_time)
                    self.start_acquisition()
                    self.wait_for_acquisition()
                    self.get_most_recent_image()
                    
                    if self.flag_my_init == False:
                        break
                    
                    if tmp_wanted_temperature != self.wanted_temperature:
                        break
                    
            ###########################################################################                            
            else:
                print('some error with the mode of the camera')
                

         
        self.set_temperature(20)
                
        while True:
            
            self.current_temperature = self.get_temperature()
            
            if self.current_temperature <= 0:
                print('please wait while camera temperature is rising, currently at ' + str(self.current_temperature))
                time.sleep(5)
            else:
                print('shutting down the camera')
                time.sleep(1)
                self.cooler_off()
                time.sleep(3)
                self.shut_down()
                break
            
            
        self.flag_my_init = True # für den nächsten start. zum abbrechen ssetze vona außen auf False  







    ###########################################################################
    # the intrinsic functions, translated to python ########################### 
    ###########################################################################
 
    # page 114: unsigned int WINAPI GetAvailableCameras(long* totalCameras)
    def get_available_cameras(self):
        print('check for available cameras:')        
       
        status = c_long()
        pStatus = pointer(status)
        
        tmp = dll_Andor.GetAvailableCameras(pStatus)

        # check if get_status worked
        if tmp == 20002:
            print('-> number of available cameras: ' + str(status.value))
        else:
            print('-> some error getting the status; ' + str(tmp))          
            
    # page 199: unsigned int WINAPI Initialize(char* dir)
    def initialize(self): 
        tmp = c_long()
        
        tmp = dll_Andor.Initialize("C:\Program Files\Andor SOLIS\Drivers")
        
        # check if initialization worked
        if tmp == 20002:
            print('-> camera initialized')
        elif tmp == 20003:
            print('DRV_VXDNOTINSTALLED; maybe camera off?..')
        else:
            print('some error initializing the camera; ' + str(tmp))
            
    # page 295: unsigned int WINAPI SetTemperature(int temperature)         
    def set_temperature(self,T):
        tmp = T
        dll_Andor.SetTemperature(c_long(tmp))
    
    # page 189: unsigned int WINAPI GetTemperature(int* temperature)          
    def get_temperature(self):
        # declare ctype c_int for later use?
        temperature = c_long()     
        pTmp = pointer(temperature)
        status = dll_Andor.GetTemperature(pTmp)

        return temperature.value
        
    # page 104: unsigned int WINAPI CoolerON(void)
    def cooler_on(self):
        dll_Andor.CoolerON()        
     
    # page 103: unsigned int WINAPI CoolerOFF(void)
    def cooler_off(self):
        dll_Andor.CoolerOFF()          
        
    # page 285: unsigned int WINAPI SetReadMode(int mode)
    def set_read_mode(self,n):
        #  0 = Full Vertical Binning, 1 = Multi-Track, 2 = Random-Track, 3 = Single-Track, 4 = Image
        tmp = dll_Andor.SetReadMode(n)

        # check if set read mode worked
        if tmp == 20002:
            print('-> read mode set to: ' + str(n))
        else:
            print('some error setting the camera image; ' + str(tmp))

    # page 268: unsigned int WINAPI SetImage(int hbin, int vbin, int hstart, int hend, int vstart, int vend)
    def set_image(self):
        # int hbin, int vbin, int hstart, int hstop, int vstart, int vstop
        tmp = dll_Andor.SetImage(1,1,1,512,1,512)
        
        # check if image setting worked
        if tmp == 20002:
            print('-> all parameters for camera image accepted')
        else:
            print('some error setting the camera image; ' + str(tmp))               

    # page 226: unsigned int WINAPI SetAcquisitionMode(int mode)                              
    def set_acquisition_mode(self,n):
        # acquisition_mode accepts n: 1 = Single Scan, 2 = Accumulate, 3 = Kinetics, 4 = Fast Kinetics , 5 = Run till abort
        n_to_c = c_int(n)        
        tmp = dll_Andor.SetAcquisitionMode(n_to_c)

        # check if set_acquisition_mode worked
        if tmp == 20002:
            print('-> camera set_acquisition_mode to: ' + str(n))
        else:
            print('some error setting the camera mode; ' + str(tmp)) 

    # page 256: unsigned int WINAPI SetExposureTime(float time)
    def set_exposure_time(self,t):

        tmp = dll_Andor.SetExposureTime(c_float(t))

        # check if set_exposure_time worked
        if tmp == 20002:
            pass
#            print('DRV_SUCCESS; camera set_exposure_time to: ' + str(t))
        else:
            print('some error setting the camera exposure time; ' + str(tmp))
            
            
    # page 289: unsigned int WINAPI SetShutterEx(int typ, int mode, int closingtime, int openingtime, int extmode)
    def set_shutter_ex(self):

        tmp = dll_Andor.SetShutterEx(1, 1, 0, 0, 1)

        # check if set_shutter_ex worked
        if tmp == 20002:
            pass
#            print('DRV_SUCCESS; camera set_exposure_time to: ' + str(t))
        else:
            print('some error setting the shutter time; ' + str(tmp))

    # page 278: unsigned int WINAPI SetNumberAccumulations(int number) 
    def set_number_accumulations(self,n):
        # int number n: number of scans to accumulate    
        tmp = dll_Andor.SetNumberAccumulations(c_long(n))
        
        # check if set_number_accumulations worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_number_accumulations to: ' + str(n))
        else:
            print('some error setting the camera set_number_accumulations; ' + str(tmp))

    # page 225: unsigned int WINAPI SetAccumulationCycleTime(float time)
    def set_accumulation_cycle_time(self,t):
        # float time: the accumulation cycle time in seconds
        tmp = dll_Andor.SetAccumulationCycleTime(c_float(t))
        
        # check if set_accumulation_cycle_time worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_accumulation_cycle_time to: ' + str(t))
        else:
            print('some error setting the camera set_accumulation_cycle_time; ' + str(tmp))

    # page 278: unsigned int WINAPI SetNumberKinetics(int number)
    def set_number_kinetics(self,n):
        # int number: number of scans to store
        tmp = dll_Andor.SetNumberKinetics(c_long(n))
        
        # check if set_number_kinetics worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_number_kinetics to: ' + str(n))
        else:
            print('some error setting the camera set_number_kinetics; ' + str(tmp))

    # page 274: unsigned int WINAPI SetKineticCycleTime(float time)
    def set_kinetic_cycle_time(self,t):
        # float time: the kinetic cycle time in seconds
        tmp = dll_Andor.SetKineticCycleTime(c_float(t))
        
        # check if set_kinetic_cycle_time worked
        if tmp == 20002:
            print('DRV_SUCCESS; camera set_kinetic_cycle_time to: ' + str(t))
        else:
            print('some error setting the camera set_kinetic_cycle_time; ' + str(tmp))

    # page 303: unsigned int WINAPI StartAcquisition(void)
    def start_acquisition(self):
       
        tmp = dll_Andor.StartAcquisition()

        # check if set_acquisition_mode worked
        if tmp == 20002:
            pass
#            print('DRV_SUCCESS; camera started acquisition:')
        else:
            print('some error starting the acquisition; ' + str(tmp))
            
    # page 110: unsigned int WINAPI GetAcquiredData(at_32* arr, unsigned long size)
    def get_acquired_data(self,m_data,m_pixels):
       
        tmp = dll_Andor.GetAcquiredData(m_data,m_pixels)

        # check if set_acquisition_mode worked
        if tmp == 20002:
            pass
#            print('DRV_SUCCESS; got the data:')
        else:
            print('some error getting the data; ' + str(tmp))
            
    # page 169: unsigned int WINAPI GetMostRecentImage(at_32* arr, unsigned long size)        
    def get_most_recent_image(self):
       
        tmp = dll_Andor.GetMostRecentImage(self.data,self.n_pixel)

        # check if get_most_recent_image worked
        if tmp == 20002:
            pass
#            print('DRV_SUCCESS; got the most recent image:')
        else:
            print('some error getting the most recent image; ' + str(tmp))
            
#        py_data = np.array(self.data).reshape(self.image_width, self.image_height)
#        
#        return py_data
             
    # page 187: unsigned int WINAPI GetStatus(int* status)     
    def get_status(self):
        # This function will return the current status of the Andor SDK system.
        # This function should be called before an acquisition is started to
        # ensure that it is IDLE and during an acquisition to monitor the process
        status = c_int()
        pStatus = pointer(status)
        
        tmp = dll_Andor.GetStatus(pStatus)

        # check if get_status worked
        if tmp == 20002:
            print('DRV_SUCCESS; got the status: ' + str(status))
        else:
            print('some error getting the status; ' + str(tmp))            

    # page 305: unsigned int WINAPI WaitForAcquisition(void)
    def wait_for_acquisition(self):
        #print('wait_for_acquisition')
        dll_Andor.WaitForAcquisition() 

    # page 102: unsigned int WINAPI AbortAcquisition(void)
    def abort_acquisition(self):
        print('abort_acquisition')
        dll_Andor.AbortAcquisition()            
    
    # page 302: unsigned int WINAPI ShutDown(void)
    def shut_down(self):
        print('iXon_Ultra_camera closed')
        print('------------------------')
        dll_Andor.ShutDown()                  

    ###########################################################################
    # END intrinsic functions ################################################# 
    ###########################################################################





    ###########################################################################
    ##### BUILD ON TOP FUNCTIONS ##############################################
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
        png_data = np.array(self.data).reshape(self.image_width, self.image_height)        
        plotted_png_data = plt.imshow(png_data, cmap=cm.gray, vmin=500, vmax=1000, extent=(1, self.image_width, 1, self.image_height), origin='lower')

        now = str(strftime("%Y_%m_%d_%H%M%S", localtime()))
        
        name = now + '_cam.png'
        
        plt.savefig(name)
