# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 12:41:48 2016

@author: JohannesMHeinrich
"""

import time # ------------------------------------------------------------------------- import time
from time import localtime, strftime # ------------------------------------------------ import for the right format of time values
from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- similar to above
import random # ----------------------------------------------------------------------- not needed???
import math # -------------------------------------------------------------------------
import datetime # --------------------------------------------------------------------- for the timestamp of the monitoring
import glob, os # --------------------------------------------------------------------- to search the directorys
import csv

### UNCOMMENT BELOW for EXPERIMENT computer ###########################################
#from library.instr_AgilentTech_Oscilloscope_DSO1024A import oscilloscope_rf #------------------ class for the AgilentTech Oscilloscope DSO1024A
##from library.instr_HighFinesseWM_WS07 import
#from library.instr_iXon_Ultra_Camera import iXon_Ultra_camera #-------------------------------- class for the ANDOR camera 
#from library.instr_Keithley_Power_Supply_2231A_30_3 import oven_power_supply # ---------------- class for the Keithley power supply for the oven current
#from library.instr_National_Instruments_PCI6010 import AnalogInput #------------------------------------------ class for the DAC 6010 - not used at the moment
#from library.instr_National_Instruments_PCI6703 import VoltUpdate #------------------------------------------ class for the DAC 6703 from NI
#from library.instr_Red_Pitaya import scpi #----------------------------------------------------- class for the red pitaya
#from library.instr_SPC_ion_pump import ion_pump_SPC #------------------------------------------ class for the ion pump
#from library.instr_Thorlabs_piezo_controller import piezo_fiber_laser # ------------------------------- class for the thorlabs piezo of the fiber laser

### UNCOMMENT BELOW for HOME computer with DUMMY CLASSES ###############################

from library.d_instr_AgilentTech_Oscilloscope_DSO1024A import oscilloscope_rf #------------ DUMMY class for the AgilentTech Oscilloscope DSO1024A
from library.d_instr_iXon_Ultra_Camera import iXon_Ultra_camera #-------------------------- DUMMY class for the ANDOR camera
from library.d_instr_Keithley_Power_Supply_2231A_30_3 import oven_power_supply # ---------------- class for the Keithley power supply for the oven current
from library.d_instr_National_Instruments_PCI6010 import AnalogInput #------------------------------------ DUMMY class for the DAC 6010 - not used at the moment
from library.d_instr_National_Instruments_PCI6703 import VoltUpdate #------------------------------------ DUMMY class for the DAC 6703 from NI
from library.d_instr_Red_Pitaya import scpi #----------------------------------------------- DUMMY class for the red pitaya
from library.d_instr_SPC_ion_pump import ion_pump_SPC #------------------------------------ DUMMY class for the ion pump
from library.d_instr_Thorlabs_piezo_controller import piezo_fiber_laser # ------------------------------- class for the thorlabs piezo of the fiber laser


#from time import localtime, strftime
#from function_answer_emails import start_email_bot


path_to_data = 'data\\'

program_scheduler = QtScheduler()
program_scheduler.start()



########################################################################################################
########################################################################################################
########################################################################################################
################                                                            ############################
################               THE MAIN PROGRAMM                            ############################
################                                                            ############################
########################################################################################################
########################################################################################################
########################################################################################################



class c_program:
    def __init__(self):

########################################################################################################
########################################################################################################
########################################################################################################
################# here a better explanation of what is happening must be written   #####################
#################                                                                  #####################
#################                                                                  #####################
########################################################################################################
########################################################################################################        
########################################################################################################       

        ################################################################################################        
        ### PARAMETERS & CONSTANTS ##### PARAMETERS & CONSTANTS ##### PARAMETERS & CONSTANTS ###########
        ################################################################################################

        #---------------- SEQUENCE 01 PARAMETERS ----------------------------------------------------------#

        self.load_be_creation_seq_01 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.load_be_creation_custom_name_seq_01 = "config_be_creation.txt"
        self.load_be_creation_time_seq_01 = 0.0
        
        self.load_trap_voltages_seq_01 = [[0,0,0,0,0,0,0,0,0,0]]
        self.load_trap_voltages_n_seq_01 = 0
        self.load_trap_voltages_times_seq_01 = [0]     
        
        self.load_trap_voltages_seq_01_for_plot = [[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]],[[0],[0]]]
 
        self.piezo_controller_list_seq_01 = [0]
        self.piezo_controller_list_times_seq_01 = [0]
        
        self.aom_list_seq_01 = [0]
        self.aom_list_times_seq_01 = [0]
        
        self.pic_list_times_seq_01 = []
        #--------------------------------------------------------------------------------------------------#
        
        
        #---------------- CAMERA PARAMETERS ---------------------------------------------------------------#                  
            # they are all in the camera class
        #--------------------------------------------------------------------------------------------------#
        
       
        #---------------- TRAP PARAMETERS -----------------------------------------------------------------#
        self.dc_1 = 0.0 # ------------------------------------------ dc voltage el. 1, set by DAC 6703
        self.dc_2 = 0.0 # ------------------------------------------ dc voltage el. 2, set by DAC 6703
        self.dc_3 = 0.0 # ------------------------------------------ dc voltage el. 3, set by DAC 6703
        self.dc_4 = 0.0 # ------------------------------------------ dc voltage el. 4, set by DAC 6703
        self.dc_5 = 0.0 # ------------------------------------------ dc voltage el. 5, set by DAC 6703
        self.dc_6 = 0.0 # ------------------------------------------ dc voltage el. 6, set by DAC 6703
        self.dc_7 = 0.0 # ------------------------------------------ dc voltage el. 7, set by DAC 6703
        self.dc_8 = 0.0 # ------------------------------------------ dc voltage el. 8, set by DAC 6703

        self.dc_endcaps = 0.0 # ------------------------------------ dc voltage for the endcaps, set by DAC 6703 
        self.dc_center = 0.0 # ------------------------------------- dc voltage for the center electrodes, set by DAC 6703         
              
        self.rf_amplitude = 400 # ---------------------------------- rf amplitude, set by red pitaya
        self.rf_amplitude_ampl = 5 # ------------------------------- rf amplification by amplifier
        self.rf_frequency = 19225000 # ----------------------------- rf frequency, set by red pitaya

        self.rf_osc_ampl = 0.0 # ----------------------------------- rf amplitude, set by AgilentTech Oscilloscope DSO1024A        
        self.rf_osc_freq = 0.0 # ----------------------------------- rf frequency, set by AgilentTech Oscilloscope DSO1024A
        self.rf_osc_rms = 0.0 # ------------------------------------ rf rms, set by AgilentTech Oscilloscope DSO1024A
        
        self.rf_cali_f_start = 15 # -------------------------------- rf calibration start frequency, set by red pitaya 
        self.rf_cali_f_stop = 25 # --------------------------------- rf calibration stop frequency, set by red pitaya 
        self.rf_cali_step_size = 0.01 # ---------------------------- rf calibration step size

        self.rf_cali_x_values = [] # ------------------------------- list for the plot of rf calibration x-values
        self.rf_cali_y_values = [] # ------------------------------- list for the plot of rf calibration y-values
        self.breaker_calibration = 0

        self.trap_r0 = 0.0035 # ------------------------------------ distance from trap axis to nearest point on an electrode
        self.trap_z0 = 0.006 # ------------------------------------- half the length of the center trap electrodes 3 and 6
        
        self.trap_ax_Be = 0.0001 # --------------------------------- stability factor for Be+ in our trap with U_endcaps = self.dc_2
        self.trap_qx_Be = 0.01 # ----------------------------------- stability factor for Be+ in our trap with V_rf = self.rf_osc_rms * sqrt(2)
        self.trap_ay_Be = 0.01 # ----------------------------------- stability factor for Be+ in our trap with U_endcaps = self.dc_2
        self.trap_qy_Be = 0.0001 # --------------------------------- stability factor for Be+ in our trap with V_rf = self.rf_osc_rms * sqrt(2)
        self.trap_omegax_Be_squared = 0.0 # ------------------------ harmonic oscillation frequency for Be+ in pseudopotential (no micromotion)
        self.trap_omegay_Be_squared = 0.0 # ------------------------ harmonic oscillation frequency for Be+ in pseudopotential (no micromotion)
        self.trap_depthx_Be = 0.0 # -------------------------------- depth of the trap for Be+ in eV
        self.trap_depthy_Be = 0.0 # -------------------------------- depth of the trap for Be+ in eV

        self.trap_potential_r_values = [] # ------------------------ r values for potential plot in x and y direction
        self.trap_potential_x_Be = [] # ---------------------------- values for x
        self.trap_potential_y_Be = [] # ---------------------------- values for y
        
        self.trap_stability_x_values = [] # ------------------------ values for the plot of the stability diagram
        self.trap_stability_y_values = [] # ------------------------ values for the plot of the stability diagram
        self.trap_stability_y2_values = [] # ----------------------- minus values for the plot of the stability diagram
        
        self.breaker_change_rf_amplitude = 0
        self.v_start_rf_sweep = 0.0
        self.v_stop_rf_sweep = 0.0
        self.t_duration_rf_sweep = 0.0
        self.counter_rf_sweep = 0.0 # ------------------------------
        
        self.load_all_voltages = []
#        self.load_trap_custom_name = "config_2017_06_11_150017_trap_voltages.txt"
        #--------------------------------------------------------------------------------------------------#
        
        
        #---------------- OVEN AND EGUN PARAMETERS --------------------------------------------------------#
        self.oven_current = 0.0 # ---------------------------------- current of the oven, set by DAC 6703  
        self.oven_calibration_factor = 1/0.9577698 # --------------- the calibration factor before applying
               
        self.egun_current_filament = 0.0 # ------------------------- current of the egun, set by DAC 6703  
        self.egun_calibration_factor = 1/0.837989 # ---------------- the calibration factor before applying     
        
        self.egun_voltage_filament = 0.0 # ------------------------- voltage of the egun filament, set by DAC 6703  
        self.egun_voltage_wehnelt = 0.0 # -------------------------- voltage of the egun wehnelt, set by DAC 6703         
        self.egun_calibration_voltage = -1/100 # ------------------- the calibration factor before applying

        self.t_oven_emission = 0.0 # ------------------------------- Be+ creation time parameter, duration of oven emission, used by python code
        self.t_oven_stand_by = 0.0 # ------------------------------- Be+ creation time parameter, duration of oven stand by, used by python code

        self.i_oven_emission = 0.0 # ------------------------------- Be+ creation current parameter for oven emission, set by DAC 6703  
        self.i_oven_stand_by = 0.0 # ------------------------------- Be+ creation current parameter for oven stand by, set by DAC 6703
        
        self.t_egun_delay = 0.0 # ---------------------------------- Be+ creation time parameter, delay for start of egun, used by python code
        self.t_egun_emission = 0.0 # ------------------------------- Be+ creation time parameter, duration of egun emission, used by python code
        
        self.i_fil_emission = 0.0 # -------------------------------- Be+ creation current parameter for egun emission, set by DAC 6703  
        self.i_fil_stand_by = 0.0 # -------------------------------- Be+ creation current parameter for egun stand by, set by DAC 6703  
        
        self.v_fil_emission = 0.0 # -------------------------------- Be+ creation voltage parameter for egun filament emission, set by DAC 6703 
        self.v_fil_stand_by = 0.0 # -------------------------------- Be+ creation voltage parameter for egun filament stand by, set by DAC 6703 
        
        self.v_weh_emission = 0.0 # -------------------------------- Be+ creation voltage parameter for egun wehnelt emission, set by DAC 6703 
        self.v_weh_stand_by = 0.0 # -------------------------------- Be+ creation voltage parameter for egun wehnelt stand by, set by DAC 6703 
        
        self.n_rep = 1 # ------------------------------------------- Be+ creation repetition parameter, defines amount of cycles for egun
        
        self.be_creation_flag = 0.0 # ------------------------------ Be+ creation flag - needed to show the remaining duration of the sequence
        self.breaker_Be_creation = 0 
        
        self.load_be_creation = []
        #--------------------------------------------------------------------------------------------------#    
        
        
        #---------------- ION PUMP PARAMETERS -------------------------------------------------------------#
        self.pressure_ion_pump = 0.0000000001 # -------------------- pressure monitoring: reads analog input, done by DAC 6010 - not used. delete?
        self.pressure_ion_pump_digital = 0.0000000001 # ------------ pressure monitoring: reads digital value from ion pump controller (spc) via serial connection
        self.pressure_ion_pump_digital_monitoring = [] # ----------- to monitor the pressure development
        #--------------------------------------------------------------------------------------------------#


        #---------------- 313 LASER PARAMETERS -------------------------------------------------------------#
        self.laser_313_aom_voltage = 0.0 # ------------------------- to change the aom voltage
        
        self.laser_313_aom_ttl = 0.0 # ----------------------------- to change the aom voltage
        
        self.laser_313_piezo_voltage = 0.0 # ----------------------- to change the piezo voltage
        
        self.laser_313_piezo_voltage_measured = 0.0 # -------------- measured value
        
        
        
        self.laser_313_piezo_u_start = 0.0
        self.laser_313_piezo_u_step = 0.0
        self.laser_313_piezo_t_break = 0.0
        self.laser_313_piezo_n_rep = 1
        self.laser_313_piezo_n_incr = 50
        self.change_fiber_laser_piezo_delay = 0.1
        self.laser_313_flag = 0.0 # -------------------------------- 313nm change flag - needed to show the remaining duration of the sequence
        
        self.breaker_change_fiber_piezo = 0
        
        self.laser_313_aom_u_start = 0.0
        self.laser_313_aom_u_step = 0.0
        self.laser_313_aom_t_break = 0.0
        self.laser_313_aom_n_rep = 1
        self.laser_313_aom_n_incr = 50
        self.change_fiber_laser_aom_delay = 0.1
        self.laser_313_aom_flag = 0.0 # ---------------------------- 313nm change flag - needed to show the remaining duration of the sequence
        
        self.breaker_change_fiber_aom = 0        
        
        #--------------------------------------------------------------------------------------------------#




        #---------------- LISTS FOR THE TIME DEPENDENT MONITORING -----------------------------------------#
        self.time_now = [1970,1,1,0,0,1]
        self.x_values_time = [] # ---------------------------------- for the monitoring
        self.x_values_difference_to_now = [] # --------------------- for the plot of the monitoring
        self.m_time_duration = 400   # ---------------------------- how much data the time dependent plots contain
        #--------------------------------------------------------------------------------------------------#


        #---------------- CONSTANTS --- CONSTANTS --- CONSTANTS --- CONSTANTS --- CONSTANTS --- CONSTANTS -#
        self.elementary_charge = 1.60217662*math.pow(10,-19) # ----- 
        self.atomic_mass_unit = 1.6605390*math.pow(10,-27) # -------
        
        self.mass_Be = 9 # ----------------------------------------- 
        self.charge_Be = 1 # ---------------------------------------
        #--------------------------------------------------------------------------------------------------#






        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        
        #++ initialize devices + initialize devices + initialize devices + initialize devices ++++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ start the camera ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#         
        self.camera = iXon_Ultra_camera()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ start the red pitaya ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
        self.red_pitaya_01 = scpi('134.157.7.124')
        self.start_red_pitaya_01()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ start the rf oscilloscope +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
        self.rf_osci = oscilloscope_rf()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ start the ion pump ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++# 
        self.ion_pump = ion_pump_SPC()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

#        self.simion = simion_analysis()
        # create instance of email bot
#        self.emailbot = e_mail()
        
        self.oven_supply = oven_power_supply()
        
        self.fiber_piezo = piezo_fiber_laser()





        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        
        #++ scheduled jobs + scheduled jobs + scheduled jobs + scheduled jobs + scheduled jobs +++++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
        #++ scheduled job for the update my time ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#          
        program_scheduler.add_job(self.set_time_now, 'interval', seconds=1, id='set_time_now_id')
        
        #++ scheduled job for the update of all plots +++++++++++++++++++++++++++++++++++++++++++++++++++++#          
        program_scheduler.add_job(self.update_rf_oscilloscope, 'interval', seconds=2, id='update_rf_oscilloscope_id')
              
        #++ scheduled job for the update of the ion pump pressure plots +++++++++++++++++++++++++++++++++++#  
        program_scheduler.add_job(self.update_pressure_ion_pump_digital, 'interval', seconds=2, id='update_pressure_ion_pump_digital_id')    

        #++ scheduled job for the update of the piezo voltage +++++++++++++++++++++++++++++++++++++++++++++#          
        program_scheduler.add_job(self.apply_313_piezo_get_voltage, 'interval', seconds=0.5, id='update_piezo_voltage_id')

        #++ scheduled job for the complete monitoring +++++++++++++++++++++++++++++++++++++++++++++++++++++# 
        program_scheduler.add_job(self.time_monitoring_up, 'interval', seconds=2, id='time_monitoring_up_id')
        
#        #++ scheduled job for the complete monitoring +++++++++++++++++++++++++++++++++++++++++++++++++++++# 
#        program_scheduler.add_job(self.time_monitoring_baking, 'interval', seconds=15, id='time_monitoring_baking_id') 
#        
#        #++ scheduled job for analog reading of pressure ++++++++++++++++++++++++++++++++++++++++++++++++++# 
#        program_scheduler.add_job(self.update_pressure_ion_pump, 'interval', seconds=5, id='update_pressure_ion_pump_id')       

#        program_scheduler.add_job(start_email_bot, 'interval', seconds=30, id='email_id', args = [self.pressure_ion_pump_digital])
        




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ the second part of the class contains all the FUNCTIONS which are  ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ used from the GUI                                                  ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~                                                                    ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    #~~ function to load a Be+ creation sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def sequ_01_be_creation_load(self,keyword_for_filename):
        
        self.load_be_creation_config(keyword_for_filename)    
        self.load_be_creation_seq_01 = self.load_be_creation[:]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
    #~~ function to load mulitple settings for the trap voltages, depending on the tagged word ~~~~~~~~#
    def sequ_01_trap_voltages_load(self, keyword_for_filename):
   
        # load trap parameters parameters as specified and save
        all_files = []
        for file in glob.glob(str(path_to_data) + '*_trap_voltages_*' + str(keyword_for_filename) + '*.txt'):      
            file_name = str(file)
            file_name = file_name[5:]
            all_files.append(file_name)
            print(file_name)
        
        complete_data = []
        
        self.load_trap_voltages_n_seq_01 = len(all_files)
        
        if self.load_trap_voltages_n_seq_01 == 0:
            
            print('nothing found with that keyword')
            
            self.load_trap_voltages_seq_01 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            
        else:
        
            for i in range(len(all_files)):
                data = []
                with open(str(path_to_data) + str(all_files[i]), newline='') as inputfile:
                    for row in csv.reader(inputfile):
                        data.append(row)        
        
                data = data[0][:]
        
                v_dc_1 = float(data[6])
                v_dc_2 = float(data[7])
                v_dc_3 = float(data[8])
                v_dc_4 = float(data[9])
                v_dc_5 = float(data[10])
                v_dc_6 = float(data[11])
                v_dc_7 = float(data[12])
                v_dc_8 = float(data[13])
                        
                v_rf_ampl = float(data[14])
                v_rf_frequ = float(data[15])/1000000
                
                tmp_load_all_voltages = [v_dc_1,v_dc_2,v_dc_3,v_dc_4,v_dc_5,v_dc_6,v_dc_7,v_dc_8,v_rf_ampl,v_rf_frequ]                
                complete_data.append(tmp_load_all_voltages)
                
            self.load_trap_voltages_seq_01 = complete_data[:]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~ function to connect the trap voltages with the time values for the change ~~~~~~~~~~~~~~~~~~~~~#
    def sequ_01_trap_voltages_init(self):
        
        self.load_trap_voltages_n_seq_01 = len(self.load_trap_voltages_times_seq_01)
        
        if self.load_trap_voltages_n_seq_01 != 0 and self.load_trap_voltages_n_seq_01 == len(self.load_trap_voltages_times_seq_01):
            entry = []
            temp_list= []
            for j in range(len(self.load_trap_voltages_seq_01[0])):
                
                times = []
                values = []
                
                for i in range(self.load_trap_voltages_n_seq_01):
                    times.append(self.load_trap_voltages_times_seq_01[i])
                    values.append(self.load_trap_voltages_seq_01[i][j])           
                
                entry = [times,values]
                
                temp_list.append(entry)
                
            
            self.load_trap_voltages_seq_01_for_plot = temp_list[:]
        else:
            print("not right parameters - number of times not equal number of voltages")
            
            self.load_trap_voltages_seq_01 = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
            self.load_trap_voltages_times_seq_01 = [0,0]        
            self.load_trap_voltages_seq_01_for_plot = [[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]],[[0,0],[0,0]]]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function to save the crystal creation parameters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def save_seq_01_config(self, keyword_for_filename):        

        file_name = str(strftime("%Y_%m_%d_%H%M%S", localtime())) + '_crystal_creation_' + str(keyword_for_filename) + '.txt'  
        
        data_be_creation = [[self.load_be_creation_time_seq_01], self.load_be_creation_seq_01]
        data_trap_voltages = [self.load_trap_voltages_times_seq_01, self.load_trap_voltages_seq_01]
        data_piezo = [self.piezo_controller_list_times_seq_01,self.piezo_controller_list_seq_01]
        data_aom = [self.aom_list_times_seq_01,self.aom_list_seq_01]
        data_pics = self.pic_list_times_seq_01
        
        dataset = [str(strftime("%Y,%m,%d,%H,%M,%S", localtime())),data_be_creation,data_trap_voltages,data_piezo,data_aom,data_pics]    
                       
        with open(str(path_to_data) + str(file_name), "a") as myfile:
            writer=csv.writer(myfile)
            
            writer.writerow(dataset[0])             # date
            
            writer.writerow(dataset[1][0])          # starting time oven sequence
            writer.writerow(dataset[1][1])          # oven sequence parameters
            
            writer.writerow(dataset[2][0])          # time values for trap voltages
            for i in range(len(dataset[2][0])):     # trap voltages
                writer.writerow(dataset[2][1][i])
                
            writer.writerow(dataset[3][0])          # time values for piezo
            writer.writerow(dataset[3][1])          # values for piezo
            
            writer.writerow(dataset[4][0])          # time values for aom
            writer.writerow(dataset[4][1])          # values for aom
            
            writer.writerow(dataset[5])          # time values for pics
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~ function to save the crystal creation parameters ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def load_seq_01_config(self, keyword_for_filename):        
        
        kind_of_dataset = 'crystal_creation'        
        k_f_f = str(keyword_for_filename)

        
        all_files = []
        
        for file in glob.glob(str(path_to_data) + '*_' + str(kind_of_dataset) + '_' + str(k_f_f) + '.txt'):
            file_name = str(file)
            file_name = file_name[5:]
            all_files.append(file_name)
        
        data = []
        
        if not all_files:
            print('nothing found to that keyword')
        else:
     
            with open(str(path_to_data) + str(all_files[-1])) as inputfile:

                for row in csv.reader(inputfile):
                    data.append(row)      
        
        data = [x for x in data if x != []] # clean from empty sublists
        
#        date = data[0][:]
        be_creation_time = float(data[1][0])
        be_creation_values = [float(i) for i in data[2]]
        trap_volt_time = [float(i) for i in data[3]]
        
        n_volt = len(trap_volt_time)
        
        trap_volt_list = []
        for h in range(n_volt):
            trap_volt_list.append([float(i) for i in data[4+h]])
            
        piezo_time = [float(i) for i in data[4 + n_volt]]
        piezo_values = [float(i) for i in data[5 + n_volt]]    
        
        aom_time = [float(i) for i in data[6 + n_volt]]
        aom_values = [float(i) for i in data[7 + n_volt]]
        
        pics = [float(i) for i in data[8 + n_volt]]
        
                
#        print(date)
#        print(be_creation_time)
#        print(be_creation_values)
#        print(trap_volt_time)
#        print(trap_volt_list)
#        print(piezo_time)
#        print(piezo_values)
#        print(aom_time)
#        print(aom_values)
#        print(pics)


        self.load_be_creation_time_seq_01 = be_creation_time
        self.load_be_creation_seq_01 = be_creation_values[:]
        self.load_trap_voltages_times_seq_01 = trap_volt_time[:]
        self.load_trap_voltages_seq_01 = trap_volt_list[:][:]
        
        self.sequ_01_trap_voltages_init()
        print(self.load_trap_voltages_seq_01)
        
        self.piezo_controller_list_times_seq_01 = piezo_time[:]
        self.piezo_controller_list_seq_01 = piezo_values[:]
        self.aom_list_times_seq_01 = aom_time[:]
        self.aom_list_seq_01 = aom_values[:]
        self.pic_list_times_seq_01 = pics[:]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
               
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    #~~ first three FUNCTIONS are only to activate and deactivate the buttons ~~~~~~~~~~~~~~~~~~~~~~~~~#      
    def cam_init(self):
        self.camera.my_initialize()
        
    def cam_off(self):
        self.camera.flag_my_init = False
        
    def do_single_pic(self):
        self.camera.flag_trig_pic = 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
  
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#         


    #~~ function to apply the DC voltage on the individuel electrodes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def apply_dc_voltage_to_el(self,value,channel):           
        VoltUpdate(float(value),channel)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function to apply an ADDITIONAL voltag to the DC electrodes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def add_dc_voltages_to_els(self,the_value,list_of_electrodes):

        voltages_now = [self.dc_1,self.dc_2,self.dc_3,self.dc_4,self.dc_5,self.dc_6,self.dc_7,self.dc_8]
          
        for i in range(len(list_of_electrodes)):
            
            num = list_of_electrodes[i]
            
            voltage_new = voltages_now[i-1]+the_value
            
            chan = "Dev3/ao" + str(num)
            
            if voltage_new <= 10 and voltage_new >= -10:
                VoltUpdate(float(voltage_new),chan)
            else:
                print("problem with setting the dc voltages")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ functions for the rf frequency done by the red pitaya ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    # function to start red pitaya
    def start_red_pitaya_01(self):    
        wave_form = 'sine'
        self.red_pitaya_01.tx_txt('SOUR1:FUNC ' + str(wave_form).upper())
        self.red_pitaya_01.tx_txt('OUTPUT1:STATE ON')
        print('red pitaya parameters set')
     
    # function to set amplitude  
    def set_rf_amplitude(self):
        
        if self.rf_amplitude_ampl == 0:
            tmp_amp = (self.rf_amplitude - 54)/1629
        elif self.rf_amplitude_ampl == 1:
            tmp_amp = (self.rf_amplitude - 46)/1494
        elif self.rf_amplitude_ampl == 2:
            tmp_amp = (self.rf_amplitude - 34)/1415
        elif self.rf_amplitude_ampl == 3:
            tmp_amp = (self.rf_amplitude - 27)/1314
        elif self.rf_amplitude_ampl == 4:
            tmp_amp = (self.rf_amplitude - 21)/1207
        elif self.rf_amplitude_ampl == 5:
            tmp_amp = (self.rf_amplitude - 15)/1095
        elif self.rf_amplitude_ampl == 6:
            tmp_amp = (self.rf_amplitude - 10)/956
        elif self.rf_amplitude_ampl == 7:
            tmp_amp = (self.rf_amplitude - 5)/784
        elif self.rf_amplitude_ampl == 8:
            tmp_amp = (self.rf_amplitude - 3.8)/512
        elif self.rf_amplitude_ampl == 9:
            tmp_amp = (self.rf_amplitude - (-3.7))/64
        else:
            print('problem with setting rf')
            
        if tmp_amp < 0.35:      
        
            self.red_pitaya_01.tx_txt('SOUR1:VOLT ' + str(tmp_amp))
            print('rf amplitude set')
            
        else:
            print("problem")

    # function to set frequency
    def set_rf_frequency(self):
        self.red_pitaya_01.tx_txt('SOUR1:FREQ:FIX ' + str(self.rf_frequency))
        print('rf frequency set')
                
    # function to turn red pitaya off
    def set_rf_off(self):     
        self.red_pitaya_01.tx_txt('OUTPUT1:STATE OFF')
        print('rf off')  
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
       
    #~~ function to get new values from the rf oscilloscope ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def update_rf_oscilloscope(self):
             
        value_freq = float(self.rf_osci.get_frequency())
        value_ampl = 20.0*float(self.rf_osci.get_peak_to_peak())
        value_rms = 20.0*float(self.rf_osci.get_rms())

        self.rf_osc_freq = value_freq
        self.rf_osc_ampl = value_ampl
        self.rf_osc_rms = value_rms
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
        


    #~~ function save the trap values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def save_trap_config(self, keyword_for_filename):
        file_name = str(strftime("%Y_%m_%d_%H%M%S", localtime())) + '_trap_voltages_' + str(keyword_for_filename) + '.txt'

        dataset = [str(strftime("%Y,%m,%d,%H,%M,%S", localtime())),float(self.dc_1),float(self.dc_2),float(self.dc_3),float(self.dc_4),float(self.dc_5),float(self.dc_6),float(self.dc_7),float(self.dc_8),float(self.rf_amplitude),float(self.rf_frequency)]    

        self.save_data(path_to_data, file_name, dataset)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function to load a Be+ creation sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def load_trap_config(self, keyword_for_filename):
        
        data = self.load_data('trap_voltages', str(keyword_for_filename))
        
#        year = int(data[0])#        month = int(data[1])#        day = int(data[2])#        hour = int(data[3])#        mins = int(data[4])#        secs = int(data[5])#        time = [year,month,day,hour,mins,secs]
        
        if len(data) > 1:
            v_dc_1 = float(data[6])
            v_dc_2 = float(data[7])
            v_dc_3 = float(data[8])
            v_dc_4 = float(data[9])
            v_dc_5 = float(data[10])
            v_dc_6 = float(data[11])
            v_dc_7 = float(data[12])
            v_dc_8 = float(data[13])
            
            v_rf_ampl  = float(data[14])
            v_rf_frequ = float(data[15])/1000000
            
            self.load_all_voltages = [v_dc_1,v_dc_2,v_dc_3,v_dc_4,v_dc_5,v_dc_6,v_dc_7,v_dc_8,v_rf_ampl,v_rf_frequ]
        else:
            pass
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            
            
#    #~~ function load the trap values ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
#    def load_trap_custom(self):
#
#
#        data = []
#        with open(str(path_to_data) + str(self.load_trap_custom_name), newline='') as inputfile:
#            for row in csv.reader(inputfile):
#                data.append(row)        
#
#        data = data[0][:]
##        year = int(data[0])
##        month = int(data[1])
##        day = int(data[2])
##
##        hour = int(data[3])
##        mins = int(data[4])
##        secs = int(data[5])
##        
##        time = [year,month,day,hour,mins,secs]
#
#        v_dc_1 = float(data[6])
#        v_dc_2 = float(data[7])
#        v_dc_3 = float(data[8])
#        v_dc_4 = float(data[9])
#        v_dc_5 = float(data[10])
#        v_dc_6 = float(data[11])
#        v_dc_7 = float(data[12])
#        v_dc_8 = float(data[13])
#        
#
#        v_rf_ampl = float(data[14])
#        v_rf_frequ = float(data[15])/1000000
#        
#        self.load_all_voltages = [v_dc_1,v_dc_2,v_dc_3,v_dc_4,v_dc_5,v_dc_6,v_dc_7,v_dc_8,v_rf_ampl,v_rf_frequ]
#    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
        
#
#    #~~ function load the trap values 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
#    def load_trap_config(self):
#
#        
#        name_list = str(path_to_data) + "config_trap_voltages.txt"
#        data = []
#        with open(name_list, newline='') as inputfile:
#            for row in csv.reader(inputfile):
#                data.append(row)        
#
#        data = data[0][:]
##        year = int(data[0])
##        month = int(data[1])
##        day = int(data[2])
##
##        hour = int(data[3])
##        mins = int(data[4])
##        secs = int(data[5])
##        
##        time = [year,month,day,hour,mins,secs]
#
#        v_dc_1 = float(data[6])
#        v_dc_2 = float(data[7])
#        v_dc_3 = float(data[8])
#        v_dc_4 = float(data[9])
#        v_dc_5 = float(data[10])
#        v_dc_6 = float(data[11])
#        v_dc_7 = float(data[12])
#        v_dc_8 = float(data[13])
#        
#
#        v_rf_ampl = float(data[14])
#        v_rf_frequ = float(data[15])/1000000
#        
#        self.load_all_voltages = [v_dc_1,v_dc_2,v_dc_3,v_dc_4,v_dc_5,v_dc_6,v_dc_7,v_dc_8,v_rf_ampl,v_rf_frequ]
#    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


















    #~~ function to do the calibration of the rf frequency ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def do_calibration_frequency(self):
        
        self.rf_cali_x_values = []
        self.rf_cali_y_values = []
        
        f_start = int(self.rf_cali_f_start*1000000)
        f_stop = int(self.rf_cali_f_stop*1000000)
        step_size = int(self.rf_cali_step_size*1000000)
        
        for i in range(f_start, f_stop, step_size):
            
            self.rf_frequency = i
            
            self.set_rf_frequency()
            print('applied rf ' + str(i))
            print('sleep now for 10')
            time.sleep(10)
            if self.breaker_calibration == 1:
                print('abort rf calibration')
                break
            
            print('measure values from oscilloscope')
            self.update_rf_oscilloscope
            
            self.rf_cali_x_values.append(self.rf_frequency)
            self.rf_cali_y_values.append(self.rf_osc_rms*1.414)
            
            print('sleep now for 10')
            print('--------------------------------')
            time.sleep(10)
            
            if self.breaker_calibration == 1:
                print('abort rf calibration')
                break
            
        self.breaker_calibration = 0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
            
            
    #~~ function q qnd a factor analysis and potential depth ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def analyze_trap_for_Be(self):
        
        tmp_dc_min = min([self.dc_1,self.dc_3,self.dc_6,self.dc_8])
        tmp_dc_max = min([self.dc_2,self.dc_4,self.dc_5,self.dc_7])
        tmp_dc = tmp_dc_max - tmp_dc_min
        
        angular_frequency = self.rf_frequency*2*math.pi
        self.trap_ax_Be = 4*self.charge_Be*self.elementary_charge*tmp_dc/(self.mass_Be*self.atomic_mass_unit*(angular_frequency*self.trap_r0)**2)
        self.trap_qx_Be = 2*self.charge_Be*self.elementary_charge*self.rf_osc_rms*math.sqrt(2)/(self.mass_Be*self.atomic_mass_unit*(angular_frequency*self.trap_r0)**2)
        self.trap_ay_Be = -1*self.trap_ax_Be
        self.trap_qy_Be = -1*self.trap_qx_Be
        
        self.trap_omegax_Be_squared = (math.pow(self.trap_qx_Be,2)/2+self.trap_ax_Be)*math.pow(angular_frequency/2,2)
        self.trap_omegay_Be_squared = (math.pow(self.trap_qy_Be,2)/2+self.trap_ay_Be)*math.pow(angular_frequency/2,2)
        
        self.trap_depthx_Be = self.mass_Be*self.atomic_mass_unit/2*self.trap_omegax_Be_squared*math.pow(self.trap_r0,2)/self.elementary_charge
        self.trap_depthy_Be = self.mass_Be*self.atomic_mass_unit/2*self.trap_omegay_Be_squared*math.pow(self.trap_r0,2)/self.elementary_charge
          
        self.prepare_plot_data_trap_for_Be()
        self.prepare_plot_data_trap_stability()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function to prepare the plot data for the trap potential ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def prepare_plot_data_trap_for_Be(self):
        
        self.trap_potential_r_values = []
        self.trap_potential_x_Be = []
        self.trap_potential_y_Be = []
            
        tmp = 100        
        for i in range(tmp):
            r_value = -0.0035+i*0.007/(tmp)
            
            self.trap_potential_r_values.append(r_value)
            
            y1 = self.mass_Be*self.atomic_mass_unit/2*(self.trap_omegax_Be_squared*math.pow(r_value,2))/self.elementary_charge
            y2 = self.mass_Be*self.atomic_mass_unit/2*(self.trap_omegay_Be_squared*math.pow(r_value,2))/self.elementary_charge
            
            self.trap_potential_x_Be.append(y1)
            self.trap_potential_y_Be.append(y2)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function to prepare the plot data for stability diagram -~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def prepare_plot_data_trap_stability(self):
        self.trap_stability_x_values = []
        self.trap_stability_y_values = []
        self.trap_stability_y2_values = []      
        
        tmp = 100        
        for i in range(tmp):
            tmp_x = 0.0+1.0*i/tmp
            tmp_y = math.pow(tmp_x,2)/2
            
            self.trap_stability_x_values.append(tmp_x)
            self.trap_stability_y_values.append(tmp_y)
            self.trap_stability_y2_values.append(-1.0*tmp_y)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ OVEN AND E-GUN TAB ~ OVEN AND E-GUN TAB ~ OVEN AND E-GUN TAB ~ OVEN AND E-GUN TAB ~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~ function to set oven current ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_oven_current(self,current):       
        self.oven_current = current             
        VoltUpdate(float(self.oven_calibration_factor*current),"Dev3/ao8")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
    #~~ function to set oven current with the new power supply ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_oven_current2(self,current):       
        self.oven_current = current
        self.oven_supply.select_channel(3)
        self.oven_supply.set_voltage(6)
        self.oven_supply.set_current(current)
        self.oven_supply.set_output('ON')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~ function to set oven current to zero qnd turn output off ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_oven_current2_off(self):       
        self.oven_current = 0.0
        self.oven_supply.select_channel(3)
        self.oven_supply.set_voltage(6)
        self.oven_supply.set_current(0.0)
        self.oven_supply.set_output('OFF')
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
    
    #~~ functions control the egun ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    
    # egun current filament
    def apply_egun_current_filament(self,current):     
        self.egun_current_filament = current
        VoltUpdate(float(self.egun_calibration_factor*current),"Dev3/ao9")
        
    # egun current filament
    def apply_egun_current_filament2(self,current):     
        self.egun_current_filament = current
        self.oven_supply.select_channel(1)
        self.oven_supply.set_voltage(6)
        self.oven_supply.set_current(current)
        self.oven_supply.set_output('ON')
        

    # egun voltage filament
    def apply_egun_voltage_filament(self,voltage):     
        self.egun_voltage_filament = voltage
        VoltUpdate(float(self.egun_calibration_voltage*voltage),"Dev3/ao10")
        
    # egun wehnelt voltage
    def apply_egun_voltage_wehnelt(self,voltage):
        self.egun_voltage_wehnelt = voltage   
        VoltUpdate(float(self.egun_calibration_voltage*voltage),"Dev3/ao11")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function for Be+ creation sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def apply_Be_creation(self):
        
        for i in range(self.n_rep):
            
            self.apply_oven_current2(self.i_oven_emission)
            
            self.apply_egun_current_filament2(self.i_fil_stand_by)
            self.apply_egun_voltage_filament(self.v_fil_stand_by)
            self.apply_egun_voltage_wehnelt(self.v_weh_stand_by)
            
            
            n_sleep_cycles = 50                
            for k in range(n_sleep_cycles):                    
                if self.breaker_Be_creation == 1:
                    break                      
                time.sleep(self.t_egun_delay/n_sleep_cycles)
            
            
            self.apply_egun_current_filament2(self.i_fil_emission)
            self.apply_egun_voltage_filament(self.v_fil_emission)
            self.apply_egun_voltage_wehnelt(self.v_weh_emission)
            
            n_sleep_cycles = 50                
            for k in range(n_sleep_cycles):                    
                if self.breaker_Be_creation == 1:
                    break                      
                time.sleep(self.t_egun_emission/n_sleep_cycles)
                
            self.apply_egun_current_filament2(self.i_fil_stand_by)
            self.apply_egun_voltage_filament(self.v_fil_stand_by)
            self.apply_egun_voltage_wehnelt(self.v_weh_stand_by)
          
            n_sleep_cycles = 50                
            for k in range(n_sleep_cycles):                    
                if self.breaker_Be_creation == 1:
                    break                      
                time.sleep((self.t_oven_emission-self.t_egun_delay-self.t_egun_emission)/n_sleep_cycles)
                
            self.apply_oven_current2(self.i_oven_stand_by)
                        
            n_sleep_cycles = 50                
            for k in range(n_sleep_cycles):                    
                if self.breaker_Be_creation == 1:
                    break                      
                time.sleep(self.t_oven_stand_by/n_sleep_cycles)
                
        self.breaker_Be_creation = 0
                
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function for the Be+ counter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def Be_creation_counter(self):
        total_dur = int(10*self.n_rep*(self.t_oven_emission+self.t_oven_stand_by))
        for i in range(total_dur):
            self.be_creation_flag = float(i*0.1)
            
            if self.breaker_Be_creation == 1:
                print('abort Be ion creation')
                break
            
            time.sleep(0.1)
        
        self.be_creation_flag = 0.0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    
    #~~ function to save the Be+ creation sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#                          
    def save_be_creation_config(self, keyword_for_filename):
        file_name = str(strftime("%Y_%m_%d_%H%M%S", localtime())) + '_be_creation_' + str(keyword_for_filename) + '.txt'

        dataset = [str(strftime("%Y,%m,%d,%H,%M,%S", localtime())),float(self.t_oven_emission),float(self.t_oven_stand_by),float(self.i_oven_emission),float(self.i_oven_stand_by),float(self.t_egun_delay),float(self.t_egun_emission),float(self.i_fil_emission),float(self.i_fil_stand_by),float(self.v_fil_emission),float(self.v_fil_stand_by),float(self.v_weh_emission),float(self.v_weh_stand_by),float(self.n_rep)]    
        
        self.save_data(path_to_data, file_name, dataset)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    
    #~~ function to load a Be+ creation sequence ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def load_be_creation_config(self, keyword_for_filename):
        
        data = self.load_data('be_creation', str(keyword_for_filename))
        
#        year = int(data[0])#        month = int(data[1])#        day = int(data[2])#        hour = int(data[3])#        mins = int(data[4])#        secs = int(data[5])#        time = [year,month,day,hour,mins,secs]
        
        if len(data) > 1:
            be_t_oven_emission = float(data[6])
            be_t_oven_stand_by = float(data[7])
            be_i_oven_emission = float(data[8])
            be_i_oven_stand_by = float(data[9])
            be_t_egun_delay    = float(data[10])
            be_t_egun_emission = float(data[11])
            be_i_fil_emission  = float(data[12])
            be_i_fil_stand_by  = float(data[13])
            be_v_fil_emission  = float(data[14])
            be_v_fil_stand_by  = float(data[15])
            be_v_weh_emission  = float(data[16])        
            be_v_weh_stand_by  = float(data[17])
            be_n_rep           = float(data[18])  
        
            self.load_be_creation = [be_t_oven_emission,be_t_oven_stand_by,be_i_oven_emission,be_i_oven_stand_by,be_t_egun_delay,be_t_egun_emission,be_i_fil_emission,be_i_fil_stand_by,be_v_fil_emission,be_v_fil_stand_by,be_v_weh_emission,be_v_weh_stand_by,be_n_rep]
        else:
            pass
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ ION PUMP TAB ~ ION PUMP TAB ~ ION PUMP TAB ~ ION PUMP TAB ~ ION PUMP TAB ~ ION PUMP TAB ~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function for the digital measured pressure update ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#              
    def update_pressure_ion_pump_digital(self):
        p = self.ion_pump.read_pressure()           
        self.pressure_ion_pump_digital = p
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function for the analog measured pressure update ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def update_pressure_ion_pump(self):        
        analog_input = AnalogInput([1],0.2)
        p = analog_input.read()[0]
        analog_input.clear()
        self.pressure_ion_pump = p
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~ function to aom voltage ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_313_aom_set_voltage(self,voltage):       
        self.laser_313_aom_voltage = voltage             
        VoltUpdate(float(voltage),"Dev3/ao8")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
 
    #~~ function to aom ttl signal ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_313_aom_ttl(self,voltage):       
        self.laser_313_aom_ttl = voltage             
        VoltUpdate(float(voltage),"Dev3/ao9")
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ function for the voltage of the piezo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_313_piezo_set_voltage(self,voltage):       
        self.laser_313_piezo_voltage = voltage             
        self.fiber_piezo.set_voltage(voltage)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~ function for the voltage of the piezo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def apply_313_piezo_get_voltage(self):
        self.laser_313_piezo_voltage_measured = self.fiber_piezo.read_voltage()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#





    #~~ function for the 313nm fiber laser aom change counter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def change_fiber_laser_aom_counter(self):
        
        total_dur = int(10*(self.laser_313_aom_n_rep*(self.laser_313_aom_n_incr+1)*self.change_fiber_laser_aom_delay+(self.laser_313_aom_n_rep-1)*self.laser_313_aom_t_break))
        
        for i in range(total_dur):
            
            self.laser_313_aom_flag = float(i*0.1)
            
            if self.breaker_change_fiber_aom == 1:
                break
            
            time.sleep(0.1)
        
        self.laser_313_aom_flag = 0.0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
    #~~ function for the 313nm fiber laser change counter ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def change_fiber_laser_piezo_counter(self):
        
        total_dur = int(10*(self.laser_313_piezo_n_rep*(self.laser_313_piezo_n_incr+1)*self.change_fiber_laser_piezo_delay+(self.laser_313_piezo_n_rep-1)*self.laser_313_piezo_t_break))
        
        for i in range(total_dur):
            
            self.laser_313_flag = float(i*0.1)
            
            if self.breaker_change_fiber_piezo == 1:
                break
            
            time.sleep(0.1)
        
        self.laser_313_flag = 0.0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
        
        
        
        




















    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ MONITORING FUNCTION ~ MONITORING FUNCTION ~ MONITORING FUNCTION ~ MONITORING FUNCTION ~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    def time_monitoring_up(self):
              
        
        tmp_time = [int(strftime("%Y", localtime())),int(strftime("%m", localtime())),int(strftime("%d", localtime())),int(strftime("%H", localtime())),int(strftime("%M", localtime())),int(strftime("%S", localtime()))]
        tmp_pressure = self.pressure_ion_pump_digital
        tmp_camera_temp = self.camera.current_temperature
               
        self.x_values_time.append(tmp_time)
        self.pressure_ion_pump_digital_monitoring.append(tmp_pressure)
        self.camera.temp_list.append(tmp_camera_temp)
        
        
        if len(self.x_values_time) < self.m_time_duration:
            pass
        else:
            self.x_values_time = self.x_values_time[-self.m_time_duration:]
            self.pressure_ion_pump_digital_monitoring = self.pressure_ion_pump_digital_monitoring[-self.m_time_duration:]
            self.camera.temp_list = self.camera.temp_list[-self.m_time_duration:]
            
            
        
        self.x_values_difference_to_now = []
        for i in range(len(self.x_values_time)):
            dt = datetime.datetime(int(self.x_values_time[i][0]), int(self.x_values_time[i][1]),int(self.x_values_time[i][2]), int(self.x_values_time[i][3]), int(self.x_values_time[i][4]),int(self.x_values_time[i][5]))
            
            timestamp = (dt - datetime.datetime.now()).total_seconds()
            self.x_values_difference_to_now.append(timestamp)
        

        self.analyze_trap_for_Be()
        
        

    def set_time_now(self):
        
        self.time_now = [int(strftime("%Y", localtime())),int(strftime("%m", localtime())),int(strftime("%d", localtime())),int(strftime("%H", localtime())),int(strftime("%M", localtime())),int(strftime("%S", localtime()))]











    #~~ smoth change of a device value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def smooth_change(self, device, v_start, v_step, n_incr, delay_incr, n_rep, t_break):
        

        if device == 0:
            msg = 'abort fiber laser AOM voltage change'
        elif device == 1:
            msg = 'abort fiber laser piezo voltage change'
                
                
        for i in range(n_rep):
            
            u_start = v_start + i*v_step
            
            incr = float(v_step/n_incr)
            
            
            for j in range(n_incr + 1):
                
                voltage_to_set = "{0:.2f}".format(round(u_start + j*incr,2))
                
                if device == 0:
                    self.apply_313_aom_set_voltage(float(voltage_to_set))
                    print(voltage_to_set + ' set at AOM')
                elif device == 1:
                    self.apply_313_piezo_set_voltage(float(voltage_to_set))
                    print(voltage_to_set + ' set at piezo')
                else:
                    pass
                
                
                
                if device == 0 and self.breaker_change_fiber_aom == 1:
                    break
                elif device == 1 and self.breaker_change_fiber_piezo == 1:
                    break
                else:
                    pass
                
                time.sleep(delay_incr)
                
            
            
            if n_rep > 1:
            
                n_sleep_cycles = 50
                
                for i in range(n_sleep_cycles):
                    
                    if device == 0 and self.breaker_change_fiber_aom == 1:
                        print(msg)
                        break
                    elif device == 1 and self.breaker_change_fiber_piezo == 1:
                        print(msg)
                        break
                    else:
                        pass    
                    
                    time.sleep(t_break/n_sleep_cycles)
            
            
            if device == 0 and self.breaker_change_fiber_aom == 1:
                print(msg)
                break
            elif device == 1 and self.breaker_change_fiber_piezo == 1:
                print(msg)
                break
            else:
                pass
            
        if device == 0:
            self.breaker_change_fiber_aom = 0
        elif device == 1:
             self.breaker_change_fiber_piezo = 0
        else:
            pass
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




    #~~ smoth change of a device value ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def smooth_change_rf_amplitude(self):

        while self.breaker_change_rf_amplitude == 0:
            
            v_start = self.v_start_rf_sweep
            v_stop = self.v_stop_rf_sweep
            t_duration = self.t_duration_rf_sweep                   
            
            incr = float((v_stop-v_start)/100.0)
            
            
            for j in range(100):
                
                voltage_to_set = "{0:.3f}".format(round(v_start + j*incr,3))
                
                self.rf_amplitude = float(voltage_to_set)
                self.set_rf_amplitude()
                
                self.counter_rf_sweep = j
                
                print(voltage_to_set + ' set for rf amplitude')
              
                
                if self.breaker_change_rf_amplitude == 1:
                    break
                else:
                    pass
                
                time.sleep(t_duration/100)
                
                
                
                
            v_start = self.v_stop_rf_sweep
            v_stop = self.v_start_rf_sweep
            t_duration = self.t_duration_rf_sweep                   
            
            incr = float((v_stop-v_start)/100.0)

            if self.breaker_change_rf_amplitude == 1:
                break
            else:
                pass            
            
            for j in range(100):
                
                voltage_to_set = "{0:.3f}".format(round(v_start + j*incr,3))
                
                self.rf_amplitude = float(voltage_to_set)
                self.set_rf_amplitude()
                
                self.counter_rf_sweep = 100-j                
                
                print(voltage_to_set + ' set for rf amplitude')
              
                
                if self.breaker_change_rf_amplitude == 1:
                    break
                else:
                    pass
                
                time.sleep(t_duration/100)
                
        self.breaker_change_rf_amplitude = 0
        self.counter_rf_sweep = 0
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def save_data(self, f_path, f_name, d_set):
               
        with open(str(f_path) + str(f_name), "a") as myfile:
            for i in range(len(d_set)):
                myfile.write(str(d_set[i]) + ',')             

            
            

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def load_data(self, kind_of_dataset, keyword_for_filename):
        
        all_files = []
        
        for file in glob.glob(str(path_to_data) + '*_' + str(kind_of_dataset) + '_' + str(keyword_for_filename) + '.txt'):
            file_name = str(file)
            file_name = file_name[5:]
            all_files.append(file_name)
        
        data = []
        
        if not all_files:
            print('nothing found to that keyword')
        else:

      
            with open(str(path_to_data) + str(all_files[-1]), newline='') as inputfile:

                for row in csv.reader(inputfile):
                    data.append(row)
    
            data = data[0][:]
        
        return data
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#




















#    def time_monitoring_baking(self):
#        
#        self.baking_p_time.append(self.time_now)        
#        self.baking_p.append(self.pressure_ion_pump_digital)
#        
#        self.baking_p_time_difference_to_now = []
#        
#        for i in range(len(self.baking_p_time)):
#            dt = datetime.datetime(int(self.baking_p_time[i][0]), int(self.baking_p_time[i][1]),int(self.baking_p_time[i][2]), int(self.baking_p_time[i][3]), int(self.baking_p_time[i][4]),int(self.baking_p_time[i][5]))
#            
#            timestamp = (dt - datetime.datetime.now()).total_seconds()
#            self.baking_p_time_difference_to_now.append(timestamp)
#
#        self.baking_m_time_difference_to_now = []
#        
#        for i in range(len(self.baking_m_time)):
#            dt = datetime.datetime(int(self.baking_m_time[i][0]), int(self.baking_m_time[i][1]),int(self.baking_m_time[i][2]), int(self.baking_m_time[i][3]), int(self.baking_m_time[i][4]),int(self.baking_m_time[i][5]))
#            
#            timestamp = (dt - datetime.datetime.now()).total_seconds()
#            self.baking_m_time_difference_to_now.append(timestamp)









#    def sequ_01_be_creation_load(self):
#        
#        # load be creation parameters as specified and save with time as specified
#        data = []
#        with open(self.load_be_creation_custom_name_seq_01, newline='') as inputfile:
#            for row in csv.reader(inputfile):
#                data.append(row)
#
#        be_t_oven_emission = float(data[6])
#        be_t_oven_stand_by = float(data[7])
#        be_i_oven_emission = float(data[8])
#        be_i_oven_stand_by = float(data[9])
#        be_t_egun_delay = float(data[10])
#        be_t_egun_emission = float(data[11])
#        be_i_fil_emission = float(data[12])
#        be_i_fil_stand_by = float(data[13])
#        be_v_fil_emission = float(data[14])
#        be_v_fil_stand_by = float(data[15])
#        be_v_weh_emission = float(data[16])        
#        be_v_weh_stand_by = float(data[17])
#        be_n_rep = float(data[18])  
#        
#        self.load_be_creation_seq_01 = [be_t_oven_emission,be_t_oven_stand_by,be_i_oven_emission,be_i_oven_stand_by,be_t_egun_delay,be_t_egun_emission,be_i_fil_emission,be_i_fil_stand_by,be_v_fil_emission,be_v_fil_stand_by,be_v_weh_emission,be_v_weh_stand_by,be_n_rep]




#    def do_sequ_01(self):
#        
#        # load be creation parameters as specified and save with time as specified
#        data = []
#        with open("config_be_creation.txt", newline='') as inputfile:
#            for row in csv.reader(inputfile):
#                data.append(row)
#
#        be_t_oven_emission = float(data[6])
#        be_t_oven_stand_by = float(data[7])
#        be_i_oven_emission = float(data[8])
#        be_i_oven_stand_by = float(data[9])
#        be_t_egun_delay = float(data[10])
#        be_t_egun_emission = float(data[11])
#        be_i_fil_emission = float(data[12])
#        be_i_fil_stand_by = float(data[13])
#        be_v_fil_emission = float(data[14])
#        be_v_fil_stand_by = float(data[15])
#        be_v_weh_emission = float(data[16])        
#        be_v_weh_stand_by = float(data[17])
#        be_n_rep = float(data[18])  
#        
#        self.load_be_creation_seq_01 = [be_t_oven_emission,be_t_oven_stand_by,be_i_oven_emission,be_i_oven_stand_by,be_t_egun_delay,be_t_egun_emission,be_i_fil_emission,be_i_fil_stand_by,be_v_fil_emission,be_v_fil_stand_by,be_v_weh_emission,be_v_weh_stand_by,be_n_rep]
#


        
#        with open(all_files[-1], "r") as myfile:
#            
#            data = list(myfile.read())
            

            
#            print(year)
#            print(month)
#            print(day)
            
#            print(hour)
#            print(mins)
#            print(data)
                
#        dataset = [str(strftime("%Y,%m,%d,%H,%M,%S", localtime())),float(self.dc_1),float(self.dc_2),float(self.dc_3),float(self.dc_4),float(self.dc_5),float(self.dc_6),float(self.dc_7),float(self.dc_8),float(self.rf_amplitude),float(self.rf_frequency)]    
#        print(str(strftime('config_' + "%Y_%m_%d_%H%M%S", localtime())) + '_trap_voltages.txt')
#        file_name = 'config_' + str(strftime("%Y_%m_%d_%H%M%S", localtime())) + '_trap_voltages.txt'
#        with open(file_name, "a") as myfile:
#            for i in range(len(dataset)):
#                myfile.write(str(dataset[i]) + ',')
#            myfile.write(str('\n'))  

             



# NOT USED AT THE MOMENT

#    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
#    #~~ COMPLETE MONITORING OF ALL VALUES ~ COMPLETE MONITORING OF ALL VALUES ~~~~~~~~~~~~~~~~~~~~~#
#    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#    #~~ dataset[0] - dataset[5]: yyyy,mm,dd,hh,MM,ss
#    #~~ dataset[6] - dataset[13]: the dc values
#    #~~ dataset[14], dataset[15]: rf amplitude and frequency
#    #~~ dataset[16]: pressure ion pump
#    #~~ dataset[17], dataset[18]: meassured rf source amplitude and frequency
#    #~~ dataset[19]: meassured temp in camera        
#        
#    def complete_monitoring(self):
#
#        dataset = [str(strftime("%Y,%m,%d,%H,%M,%S", localtime())),float(self.dc_1),float(self.dc_2),float(self.dc_3),float(self.dc_4),float(self.dc_5),float(self.dc_6),float(self.dc_7),float(self.dc_8),float(self.rf_amplitude),float(self.rf_frequency),float(self.pressure_ion_pump_digital),float(self.rf_osc_ampl),float(self.rf_osc_freq),float(self.camera.current_temperature)]    
#    
#        with open("complete_monitoring.txt", "a") as myfile:
#            for i in range(len(dataset)):
#                myfile.write(str(dataset[i]) + ',')
#            myfile.write(str('\n'))
