# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 19:49:47 2016

@author: JohannesMHeinrich
"""

# import python classes --------------------------------------------------------------------------------
import sys # -------------------------------------------------------------------------- import for stuff i guess? i don't really know... 
from PyQt5 import QtCore, QtGui, QtWidgets # ------------------------------------------ imports for the GUI  
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas # ---- for lotting with matplotlib on the GUI widget "canvas"
from apscheduler.schedulers.qt import QtScheduler # ----------------------------------- similar to above
import time # ------------------------------------------------------------------------- time
import datetime # --------------------------------------------------------------------- for the timestamp of the monitoring
import threading # -------------------------------------------------------------------- for threading, so that gui and program don't freeze during jobs
import pyqtgraph as pg # -------------------------------------------------------------- for the plots
import numpy as np # ------------------------------------------------------------------ mathmodule and extended array functions
import math # ------------------------------------------------------------------------- mathmodule
import random # ----------------------------------------------------------------------- mathmodule
# import custom classes --------------------------------------------------------------------------------
from XCon_02_gui import Ui_XCon # -------------------------------------------------- import the layout generated with QtDesigner
from XCon_02_main import c_program # ----------------------------------------------- the program which collects the controll over all the devices

import library.f_image as f_image # ----------------------------------------------------- picture import function
# global style options for the plots -------------------------------------------------------------------
brush_black = (0,0,0,255) #------------------------------------------------------------ black
brush_background = (255,255,255,255) #------------------------------------------------- background
brush_trap_off = (0,0,0,99) #---------------------------------------------------------- grey for trap of

brush_red = (209,111,111,255) #---------------------------------------------------------- red for measured values
brush_blue = (109,123,205,255) #------------------------------------------------------- blue
#brush_violett = (190,72,181,255) #----------------------------------------------------- violett
#brush_green = (89,139,58,255) #-------------------------------------------------------- green
brush_yellow = (185,184,54,255)  #----------------------------------------------------- browhnish/yellow

redPen = pg.mkPen(color=brush_red, width=2) #------------------------------------------ same like brush_red
bluePen = pg.mkPen(color=brush_blue, width=2) #---------------------------------------- same like brush_blue
#violettPen = pg.mkPen(color=brush_violett, width=2) #---------------------------------- same like brush_violett
#greenPen = pg.mkPen(color=brush_green, width=2) #-------------------------------------- same like brush_green
yellowPen = pg.mkPen(color=brush_yellow, width=2) #------------------------------------ same like brush_yellow

geotrapPen = pg.mkPen(color=brush_black, width=2) #------------------------------------ black line
dashPen = pg.mkPen(color=brush_black, width=2, style=QtCore.Qt.DashLine) #------------- dashed black line

labelStyle_l = {'color': '#000', 'font-size': '12pt'} #-------------------------------- big label
labelStyle_m = {'color': '#000', 'font-size': '10pt'} #-------------------------------- middle label
labelStyle_s = {'color': '#000', 'font-size': '10pt'} #-------------------------------- small label

#from time import localtime, strftime # ------------------------------------------------ import for the right format of time values
#import datetime # --------------------------------------------------------------------- similar to above
#import math # ------------------------------------------------------------------------- similar to above
#from PIL import Image # --------------------------------------------------------------- to import png directly
#import csv # -------------------------------------------------------------------------- to create and read output/input in txt files


path_to_pics = 'pics\\'



starttime=time.time()
scheduler = QtScheduler()
scheduler.start()



########################################################################################################
########################################################################################################
########################################################################################################
################                                                            ############################
################       THE WINDOW CLASS                                     ############################
################                                                            ############################
########################################################################################################
########################################################################################################
########################################################################################################


 
class window(Ui_XCon):
    def __init__(self, dialog_A, the_program):
        Ui_XCon.__init__(self)
        self.setupUi(dialog_A)
        
########################################################################################################
########################################################################################################
########################################################################################################
################# the first part of the class sets up the layout of the program.   #####################
################# the PLOTS are placed and the PUSH BUTTONS are connected with the #####################
################# functions which are defined further below in the class           #####################
########################################################################################################
########################################################################################################        
########################################################################################################        

        ################################################################################################        
        ### SEQENCE 01 TAB # SEQENCE 01 TAB # SEQENCE 01 TAB # SEQENCE 01 TAB # SEQENCE 01 TAB #########
        ################################################################################################

        #---------------- PLOT for the pressure monitoring ------------------------------------------------#
        self.plot_pressure_seq_01 = pg.PlotWidget(name='PlotPressure_seq_01')  ## giving the plots names allows us to link their axes together
        self.plot_pressure_seq_01.setBackground(background=brush_background)
        self.plot_pressure_seq_01.setLabel('left', 'p', units='mBar', **labelStyle_l)
        self.plot_pressure_seq_01.setLabel('bottom', 't', units='s', **labelStyle_l)        
        self.plot_pressure_seq_01.showGrid(x=True,y=True)
        self.plot_pressure_seq_01.setLogMode(x=None, y=True)
        self.plot_pressure_seq_01.setRange(xRange=(-100, 0),yRange=(-10, -8)) 
        self.verticalLayout_ion_pump_pressure_seq_01.addWidget(self.plot_pressure_seq_01)       
        #--------------------------------------------------------------------------------------------------#

        #---------------- PLOT for png file of trap --------- ---------------------------------------------#
        self.fig_trap_seq_01 = f_image.get_image(str(path_to_pics) + 'pic_trap.png')
        self.canvas_fig_trap_seq_01 = FigureCanvas(self.fig_trap_seq_01)    
        self.verticalLayout_trap_pic_seq_01.addWidget(self.canvas_fig_trap_seq_01)
        self.canvas_fig_trap_seq_01.draw() 
        #--------------------------------------------------------------------------------------------------#

        #---------------- PLOT for png file of the oven and egun ------------------------------------------#
        self.fig_oven_and_egun_seq_01 = f_image.get_image(str(path_to_pics) + 'pic_oven.png')
        self.canvas_fig_oven_and_egun_seq_01 = FigureCanvas(self.fig_oven_and_egun_seq_01)    
        self.verticalLayout_monitoring_ovenandegun_seq_01.addWidget(self.canvas_fig_oven_and_egun_seq_01)
        self.canvas_fig_oven_and_egun_seq_01.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        
        
        
        #================ PUSH BUTTONS for seq 01 tab =====================================================#  
        self.pushButton_be_creation_time_seq_01_load.clicked.connect(self.load_para_be_creation_seq_01)
        self.pushButton_be_creation_time_seq_01_delete.clicked.connect(self.delete_para_be_creation_seq_01)
        
        self.pushButton_trap_voltages_seq_01_load.clicked.connect(self.load_para_trap_voltages_seq_01)
        
        self.pushButton_trap_voltages_time_seq_01_add.clicked.connect(self.load_para_trap_voltages_seq_01_time_add) 
        self.pushButton_trap_voltages_time_seq_01_delete.clicked.connect(self.load_para_trap_voltages_seq_01_time_delete)
        self.pushButton_trap_voltages_init_seq_01.clicked.connect(self.load_para_trap_voltages_seq_01_init)
        
        self.pushButton_piezo_seq_01_add.clicked.connect(self.piezo_seq_01_add)
        self.pushButton_piezo_seq_01_delete.clicked.connect(self.piezo_seq_01_delete)        
        
        self.pushButton_aom_seq_01_add.clicked.connect(self.aom_seq_01_add)
        self.pushButton_aom_seq_01_delete.clicked.connect(self.aom_seq_01_delete)
        
        self.pushButton_pic_seq_01_add.clicked.connect(self.pic_seq_01_add)
        self.pushButton_pic_seq_01_delete.clicked.connect(self.pic_seq_01_delete)
        
        self.pushButton_seq_01_save.clicked.connect(self.seq_01_save)
        self.pushButton_seq_01_load.clicked.connect(self.seq_01_load)
        #==================================================================================================#       
        
        
        #---------------- PLOT for function: crystal creation ---------------------------------------------#
        
        # grid for the three plots of oven and egun currents and voltages
        self.plot_crystal_creation = pg.GraphicsLayoutWidget()
        self.plot_crystal_creation.setBackground(background=brush_background)
        
        
        self.plot_be_creation_seq_01 = self.plot_crystal_creation.addPlot(row=0, col=0, colspan=1, title = 'be creation')
        
        self.plot_voltages_seq_01_dc_endcaps = self.plot_crystal_creation.addPlot(row=1, col=0, colspan=1, title = 'dc_voltages_endcaps')
        
        self.plot_voltages_seq_01_dc_center = self.plot_crystal_creation.addPlot(row=2, col=0, colspan=1, title = 'dc_voltages_center')
        
        self.plot_voltages_seq_01_rf_frequency = self.plot_crystal_creation.addPlot(row=3, col=0, colspan=1, title = 'rf_voltage_frequency')
        
        self.plot_voltages_seq_01_fr_amplitude = self.plot_crystal_creation.addPlot(row=4, col=0, colspan=1, title = 'rf_voltage_amplitude')
        
        self.plot_piezo_seq_01 = self.plot_crystal_creation.addPlot(row=5, col=0, colspan=1, title = 'piezo')
        
        self.plot_aom_seq_01 = self.plot_crystal_creation.addPlot(row=6, col=0, colspan=1, title = 'aom')

        self.plot_pic_seq_01 = self.plot_crystal_creation.addPlot(row=7, col=0, colspan=1, title = 'pics')
        
        
        # add the widget to the layout 
        self.verticalLayout_seq_01.addWidget(self.plot_crystal_creation)
        #--------------------------------------------------------------------------------------------------#
         
        ################################################################################################        
        ### CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB # CAMERA TAB# ##
        ################################################################################################        
        
        
        #---------------- PLOT for camera picture ---------------------------------------------------------#              
        self.plot_cam = pg.ImageView()
        cam_array = []
        for i in range(512):
            vec = []
            for j in range(512):
                vec.append(int(random.random()*500+500))
            cam_array.append(vec)
        self.plot_cam.setImage(np.array(cam_array).reshape(512,512),autoRange=True, autoLevels=True, levels=None, axes=None, xvals=None, pos=None, scale=None, transform=None, autoHistogramRange=True)
        self.verticalLayout_monitoring_picture_cam.addWidget(self.plot_cam)
        #--------------------------------------------------------------------------------------------------#
        
        
        #---------------- PLOT for camera temperature -----------------------------------------------------#
        self.plot_cam_temp = pg.PlotWidget(name='PlotCamTemp')  
        self.plot_cam_temp.setBackground(background=brush_background)
        self.plot_cam_temp.setLabel('left', 'Temp', units='Celsius', **labelStyle_l)   
        self.plot_cam_temp.showGrid(x=True,y=True)
        self.plot_cam_temp.setRange(xRange=(-100, 0), yRange=(-70, 30)) 
        self.verticalLayout_cam_seq.addWidget(self.plot_cam_temp) 
        #--------------------------------------------------------------------------------------------------#

        
        #================ PUSH BUTTONS for camera tab =====================================================#  
        self.pushButton_cam_INITIALIZE.clicked.connect(self.apply_cam_init)
        self.pushButton_cam_INITIALIZE.clicked.connect(self.input_cam_initialize)
        
        self.pushButton_cam_temp_set.clicked.connect(self.apply_cooling_change)        
        
        self.comboBox.currentIndexChanged['QString'].connect(self.input_cam)
        
        self.pushButton_cam_exposure_time.clicked.connect(self.read_para_cam_exp_time_from_gui_into_instance)
                  
        self.pushButton_cam_trigger_single_pic.clicked.connect(self.apply_trig_pic)
        
        self.pushButton_cam_OFF.clicked.connect(self.input_cam_off)
        self.pushButton_cam_OFF.clicked.connect(self.apply_cam_stop)        
        #==================================================================================================#
        
        
                
        ################################################################################################        
        ### TRAP TAB # TRAP TAB # TRAP TAB # TRAP TAB # TRAP TAB # TRAP TAB # TRAP TAB # TRAP TAB ######
        ################################################################################################
                
        #---------------- PLOT for png file of trap --------- ---------------------------------------------#
        self.fig_trap = f_image.get_image(str(path_to_pics) + 'pic_trap.png')
        self.canvas_fig_trap = FigureCanvas(self.fig_trap)    
        self.verticalLayout_trap_pic.addWidget(self.canvas_fig_trap)
        self.canvas_fig_trap.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        #---------------- PLOT for png file of trap - shift x ---------------------------------------------#
        self.fig_trap_shift_x = f_image.get_image(str(path_to_pics) + 'pic_trap_shift_x.png')
        self.canvas_fig_trap_shift_x = FigureCanvas(self.fig_trap_shift_x)    
        self.verticalLayout_shift_x.addWidget(self.canvas_fig_trap_shift_x)
        self.canvas_fig_trap_shift_x.draw() 
        #--------------------------------------------------------------------------------------------------#

        #---------------- PLOT for png file of trap - shift y ---------------------------------------------#
        self.fig_trap_shift_y = f_image.get_image(str(path_to_pics) + 'pic_trap_shift_y.png')
        self.canvas_fig_trap_shift_y = FigureCanvas(self.fig_trap_shift_y)    
        self.verticalLayout_shift_y.addWidget(self.canvas_fig_trap_shift_y)
        self.canvas_fig_trap_shift_y.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        
        #---------------- PLOT for png file of trap - shift z ---------------------------------------------#
        self.fig_trap_shift_z = f_image.get_image(str(path_to_pics) + 'pic_trap_shift_z.png')
        self.canvas_fig_trap_shift_z = FigureCanvas(self.fig_trap_shift_z)    
        self.verticalLayout_shift_z.addWidget(self.canvas_fig_trap_shift_z)
        self.canvas_fig_trap_shift_z.draw() 
        #--------------------------------------------------------------------------------------------------#


        #---------------- PLOT for png file of trap - endcaps end center ----------------------------------#
        self.fig_trap_endc_and_center = f_image.get_image(str(path_to_pics) + 'pic_trap_endcaps_and_center.png')
        self.canvas_fig_trap_endc_and_center = FigureCanvas(self.fig_trap_endc_and_center)    
        self.verticalLayout_trap_endc_and_center.addWidget(self.canvas_fig_trap_endc_and_center)
        self.canvas_fig_trap_endc_and_center.draw() 
        #--------------------------------------------------------------------------------------------------#


        #---------------- PLOT for png file of trap - endcaps end center ----------------------------------#
        self.fig_trap_sweep_rf = f_image.get_image(str(path_to_pics) + 'pic_trap_rf_sweep.png')
        self.canvas_fig_trap_sweep_rf = FigureCanvas(self.fig_trap_sweep_rf)    
        self.verticalLayout_sweep_rf.addWidget(self.canvas_fig_trap_sweep_rf)
        self.canvas_fig_trap_sweep_rf.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        

        #---------------- stability_plot ------------------------------------------------------------------#        
        self.stability_plot = pg.PlotWidget(name='Plot_trap_monitoring')  
        self.stability_plot.setBackground(background=brush_background)
        self.stability_plot.setLabel('left', 'a', **labelStyle_s)
        self.stability_plot.setLabel('bottom', 'q', **labelStyle_s)        
        self.stability_plot.showGrid(x=True,y=True)
        self.stability_plot.setRange(xRange=(0, 0.2), yRange=(-0.02, 0.02))
        self.verticalLayout_test.addWidget(self.stability_plot)     
        #--------------------------------------------------------------------------------------------------#
              
              
        #---------------- PLOT for the rf calibration -----------------------------------------------------#
        self.plot_rf_calibration = pg.PlotWidget(name='PlotRFFrequency_calibration')  
        self.plot_rf_calibration.setBackground(background=brush_background)
        self.plot_rf_calibration.setLabel('left', 'amplitude', units='V', **labelStyle_s)
        self.plot_rf_calibration.setLabel('bottom', 'frequency', units='Hz', **labelStyle_s)        
        self.plot_rf_calibration.showGrid(x=True,y=True)
        self.plot_rf_calibration.setLogMode(x=None, y=None)
        self.plot_rf_calibration.setRange(xRange=(18500000,19750000), yRange=(0, 800))
        self.verticalLayout_calib.addWidget(self.plot_rf_calibration)                
        #--------------------------------------------------------------------------------------------------#
                

        #================ PUSH BUTTONS for settings: dc voltages ==========================================#                  
        self.pushButton_el_1.clicked.connect(self.read_para_trap_dc1_from_gui_into_instance)
        self.pushButton_el_1.clicked.connect(self.apply_para_trap_dc1_on_device)        
        
        self.pushButton_el_2.clicked.connect(self.read_para_trap_dc2_from_gui_into_instance)
        self.pushButton_el_2.clicked.connect(self.apply_para_trap_dc2_on_device) 

        self.pushButton_el_3.clicked.connect(self.read_para_trap_dc3_from_gui_into_instance)
        self.pushButton_el_3.clicked.connect(self.apply_para_trap_dc3_on_device) 

        self.pushButton_el_4.clicked.connect(self.read_para_trap_dc4_from_gui_into_instance)
        self.pushButton_el_4.clicked.connect(self.apply_para_trap_dc4_on_device) 

        self.pushButton_el_5.clicked.connect(self.read_para_trap_dc5_from_gui_into_instance)
        self.pushButton_el_5.clicked.connect(self.apply_para_trap_dc5_on_device) 

        self.pushButton_el_6.clicked.connect(self.read_para_trap_dc6_from_gui_into_instance)
        self.pushButton_el_6.clicked.connect(self.apply_para_trap_dc6_on_device) 

        self.pushButton_el_7.clicked.connect(self.read_para_trap_dc7_from_gui_into_instance)
        self.pushButton_el_7.clicked.connect(self.apply_para_trap_dc7_on_device) 

        self.pushButton_el_8.clicked.connect(self.read_para_trap_dc8_from_gui_into_instance)
        self.pushButton_el_8.clicked.connect(self.apply_para_trap_dc8_on_device)
        
        # set dc voltages to zero
        self.pushButton_dc_to_zero.clicked.connect(self.dc_to_zero)
        #==================================================================================================#

               
        #================ PUSH BUTTONS for settings: rf voltage ===========================================#
        self.pushButton_rf_ampl.clicked.connect(self.read_para_trap_rf_amplitude_from_gui_into_instance)
        self.pushButton_rf_ampl.clicked.connect(self.apply_para_trap_rf_amplitude_on_device)
        
        self.pushButton_rf_freq.clicked.connect(self.read_para_trap_rf_frequency_from_gui_into_instance)
        self.pushButton_rf_freq.clicked.connect(self.apply_para_trap_rf_frequency_on_device)        
 
        self.pushButton_rf_all.clicked.connect(self.read_para_trap_rf_amplitude_from_gui_into_instance)          
        self.pushButton_rf_all.clicked.connect(self.read_para_trap_rf_frequency_from_gui_into_instance)
        self.pushButton_rf_all.clicked.connect(self.apply_para_trap_rf_amplitude_on_device)
        self.pushButton_rf_all.clicked.connect(self.apply_para_trap_rf_frequency_on_device)
        
        self.pushButton_rf_off.clicked.connect(self.apply_para_trap_rf_on_device_off)          
        #==================================================================================================#
        
                
        #================ PUSH BUTTONS for functions: trap ================================================#
        # set dc voltages to trapping
        self.pushButton_endcap_voltages.clicked.connect(self.set_dc_endcaps)
        
        # the extraction pulse
        self.pushButton_center_voltages.clicked.connect(self.set_dc_center)
        
        # the extraction pulse
        self.pushButton_extraction.clicked.connect(self.extraction_pulse)
        
        # the extraction pulse
        self.pushButton_tighten_potential.clicked.connect(self.trap_tighten_potential)        

        # the extraction pulse
        self.pushButton_losen_potential.clicked.connect(self.trap_losen_potential)          

        # movement in x direction
        self.pushButton_apply_x_shift_1567.clicked.connect(self.trap_move_x_1567)
        self.pushButton_apply_x_shift_2348.clicked.connect(self.trap_move_x_2348) 

        # movement in y direction
        self.pushButton_apply_y_shift_5678.clicked.connect(self.trap_move_y_5678)
        self.pushButton_apply_y_shift_1234.clicked.connect(self.trap_move_y_1234)

        # movement in z direction
        self.pushButton_apply_z_shift_27.clicked.connect(self.trap_move_z_27)
        self.pushButton_apply_z_shift_45.clicked.connect(self.trap_move_z_45)

        # sweep rf
        self.pushButton_sweep_ampl_start.clicked.connect(self.trap_sweep_rf)
        self.pushButton_sweep_ampl_stop.clicked.connect(self.trap_sweep_rf_abort) 

        # the rf calibration
        self.pushButton_calibration.clicked.connect(self.read_calibration_from_gui_into_instance)
        self.pushButton_calibration.clicked.connect(self.do_calibration)
        self.pushButton.clicked.connect(self.abort_calibration)
        #==================================================================================================#



        #==================================================================================================#
        self.pushButton_el_save.clicked.connect(self.el_save)
        self.pushButton_el_load.clicked.connect(self.el_load)
        
        self.pushButton_el_all.clicked.connect(self.read_para_trap_dc_from_gui_into_instance)
        self.pushButton_el_all.clicked.connect(self.apply_para_trap_dc_on_device)
        #==================================================================================================# 
        
        ################################################################################################        
        ### OVEN AND EGUN TAB # OVEN AND EGUN TAB # OVEN AND EGUN TAB # OVEN AND EGUN TAB ##############
        ################################################################################################                
                
                
        #---------------- PLOT for png file of the oven and egun ------------------------------------------#
        self.fig_oven_and_egun = f_image.get_image(str(path_to_pics) + 'pic_oven.png')
        self.canvas_fig_oven_and_egun = FigureCanvas(self.fig_oven_and_egun)    
        self.verticalLayout_monitoring_ovenandegun.addWidget(self.canvas_fig_oven_and_egun)
        self.canvas_fig_oven_and_egun.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        

        #---------------- PLOT for function: Be+ creation -------------------------------------------------#
        
        # grid for the three plots of oven and egun currents and voltages
        self.plot_Be_creation = pg.GraphicsLayoutWidget()
        self.plot_Be_creation.setBackground(background=brush_background)
        
        # the oven current
        self.plot_oven_current = self.plot_Be_creation.addPlot(row=0, col=0, colspan=1, title = 'oven current')
        self.plot_oven_current.setLabel('left', 'current', units='A', **labelStyle_m)
        
        # the egun current
        self.plot_egun_current = self.plot_Be_creation.addPlot(row=1, col=0, colspan=1, title = 'e-gun current filament')
        self.plot_egun_current.setLabel('left', 'current', units='A', **labelStyle_m)
        
        # the egun voltages
        self.plot_egun_voltages = self.plot_Be_creation.addPlot(row=2, col=0, colspan=1, title = 'e-gun voltages')
        self.plot_egun_voltages.setLabel('left', 'voltages', units='V', **labelStyle_m)
        
        # add the widget to the layout 
        self.verticalLayout_Be_creation.addWidget(self.plot_Be_creation)
        #--------------------------------------------------------------------------------------------------#
        
                
        #================ PUSH BUTTONS for settings: oven =================================================#
        self.pushButton_current_oven_apply.clicked.connect(self.read_para_oven_current_from_gui_into_instance)
        self.pushButton_current_oven_apply.clicked.connect(self.apply_para_oven_current_on_device)
        
        self.pushButton_current_oven_off.clicked.connect(self.apply_para_oven_current_on_device_off)
        #==================================================================================================#
        
              
        #================ PUSH BUTTONS for settings: egun =================================================#
        
        # egun current filament
        self.pushButton_current_filament_apply.clicked.connect(self.read_para_egun_current_filament_from_gui_into_instance)
        self.pushButton_current_filament_apply.clicked.connect(self.apply_para_egun_current_filament_on_device)

        self.pushButton_current_filament_off.clicked.connect(self.apply_para_egun_current_filament_on_device_off)
        
        # egun voltage filament
        self.pushButton_voltage_filament_apply.clicked.connect(self.read_para_egun_voltage_filament_from_gui_into_instance)
        self.pushButton_voltage_filament_apply.clicked.connect(self.apply_para_egun_voltage_filament_on_device)          

        self.pushButton_voltage_filament_off.clicked.connect(self.apply_para_egun_voltage_filament_on_device_off)
                
         # egun voltage wehnelt
        self.pushButton_voltage_wehnelt_apply.clicked.connect(self.read_para_egun_voltage_wehnelt_from_gui_into_instance)
        self.pushButton_voltage_wehnelt_apply.clicked.connect(self.apply_para_egun_voltage_wehnelt_on_device)       

        self.pushButton_voltage_wehnelt_off.clicked.connect(self.apply_para_egun_voltage_wehnelt_on_device_off)
        #==================================================================================================#


        
        #================ PUSH BUTTONS for function: Be+ creation =========================================#
        self.pushButton_Be_creation.clicked.connect(self.read_para_Be_creation)
        self.pushButton_Be_creation.clicked.connect(self.apply_Be_creation)
        
        self.pushButton_Be_creation_abort.clicked.connect(self.abort_Be_creation)
        
        self.pushButton_be_creation_sequence_save.clicked.connect(self.be_creation_sequence_save)
        self.pushButton_be_creation_sequence_load.clicked.connect(self.load_para_be_creation)
        #==================================================================================================#
        
        
        
        ################################################################################################        
        ### ION PUMP TAB # ION PUMP TAB # ION PUMP TAB # ION PUMP TAB # ION PUMP TAB # ION PUMP TAB ####
        ################################################################################################   
      
      
        #---------------- PLOT for png file of ion pump ---------------------------------------------------#
        self.fig_ion_pump = f_image.get_image(str(path_to_pics) + 'pic_ion_pump.png')
        self.canvas_fig_ion_pump = FigureCanvas(self.fig_ion_pump)    
        self.verticalLayout_ion_pump_picture.addWidget(self.canvas_fig_ion_pump)
        self.canvas_fig_ion_pump.draw() 
        #--------------------------------------------------------------------------------------------------#
        
        
        #---------------- PLOT for the pressure monitoring ------------------------------------------------#
        self.plot_pressure = pg.PlotWidget(name='PlotPressure')  ## giving the plots names allows us to link their axes together
        self.plot_pressure.setBackground(background=brush_background)
        self.plot_pressure.setLabel('left', 'pressure', units='mBar', **labelStyle_l)
        self.plot_pressure.setLabel('bottom', 'time', units='seconds', **labelStyle_l)        
        self.plot_pressure.showGrid(x=True,y=True)
        self.plot_pressure.setLogMode(x=None, y=True)
        self.plot_pressure.setRange(xRange=(-100, 0),yRange=(-10, -7)) 
        self.verticalLayout_ion_pump_pressure.addWidget(self.plot_pressure)       
        #--------------------------------------------------------------------------------------------------#
    


        ################################################################################################        
        ### 313 LASER TAB #313 LASER TAB # 313 LASER TAB # 313 LASER TAB # 313 LASER TAB ###############
        ################################################################################################

        #---------------- PLOT for function: 313 laser change ---------------------------------------------#

        # grid for the plot of the 313nm cooling laser change AOM
        self.plot_313_aom_change = pg.PlotWidget(name='Plot313AOMChange')  ## giving the plots names allows us to link their axes together
        self.plot_313_aom_change.setBackground(background=brush_background)
        self.plot_313_aom_change.setLabel('left', 'AOM voltage', units='V', **labelStyle_l)
        self.plot_313_aom_change.setLabel('bottom', 'time', units='seconds', **labelStyle_l)        
        self.plot_313_aom_change.showGrid(x=True,y=True)
        self.verticalLayout_313_aom_change.addWidget(self.plot_313_aom_change)
        #--------------------------------------------------------------------------------------------------#  


      
        # grid for the plot of the 313nm cooling laser change
        self.plot_313_change = pg.PlotWidget(name='Plot313Change')  ## giving the plots names allows us to link their axes together
        self.plot_313_change.setBackground(background=brush_background)
        self.plot_313_change.setLabel('left', 'piezo voltage', units='V', **labelStyle_l)
        self.plot_313_change.setLabel('bottom', 'time', units='seconds', **labelStyle_l)        
        self.plot_313_change.showGrid(x=True,y=True)
        self.verticalLayout_313_piezo_change.addWidget(self.plot_313_change)
        #--------------------------------------------------------------------------------------------------#



        self.pushButton_313_aom_apply.clicked.connect(self.read_para_aom_volt_from_gui_into_instance)
        self.pushButton_313_aom_apply.clicked.connect(self.apply_para_aom_volt_on_device) 

        self.pushButton_313_aom_off.clicked.connect(self.read_para_aom_volt_from_gui_into_instance_off)
        self.pushButton_313_aom_off.clicked.connect(self.apply_para_aom_volt_on_device)



        self.pushButton_313_aom_ttl_apply.clicked.connect(self.read_para_aom_ttl_from_gui_into_instance)
        self.pushButton_313_aom_ttl_apply.clicked.connect(self.apply_para_aom_ttl_on_device) 

        self.pushButton_313_aom_ttl_off.clicked.connect(self.read_para_aom_ttl_from_gui_into_instance_off)
        self.pushButton_313_aom_ttl_off.clicked.connect(self.apply_para_aom_ttl_on_device)
        




        self.pushButton_313_piezo_apply.clicked.connect(self.read_para_313_piezo_from_gui_into_instance)
        self.pushButton_313_piezo_apply.clicked.connect(self.apply_para_313_piezo_on_device) 

        self.pushButton_313_piezo_off.clicked.connect(self.read_para_313_piezo_from_gui_into_instance_off)
        self.pushButton_313_piezo_off.clicked.connect(self.apply_para_313_piezo_on_device)
        


        self.pushButton_313_aom_sweep_start.clicked.connect(self.read_para_313_aom_change)
        self.pushButton_313_aom_sweep_start.clicked.connect(self.apply_313_aom_change)
        
        self.pushButton_313_aom_sweep_abort.clicked.connect(self.abort_313_aom_sweep)


        
        
        self.pushButton_313_piezo_sweep_start.clicked.connect(self.read_para_313_change)
        self.pushButton_313_piezo_sweep_start.clicked.connect(self.apply_313_change)
        
        self.pushButton_313_piezo_sweep_abort.clicked.connect(self.abort_313_piezo_sweep)
                   
            
            
            
            
            
            
        
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        
        #++ timer + timer + timer + timer + timer + timer + timer + timer + timer + timer + timer ++++++#
        #+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#        

        
        #++ timer for the update of all plots +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#   
        self.timer_t_dependent_plots = QtCore.QTimer()
        self.timer_t_dependent_plots.setInterval(500)
        self.timer_t_dependent_plots.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_t_dependent_plots.timeout.connect(self.t_dependent_plot_updates)
        self.timer_t_dependent_plots.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ timer for the update of all plots II  - sequence 01 monitoring ++++++++++++++++++++++++++++++++#   
        self.timer_t_dependent_plots_II = QtCore.QTimer()
        self.timer_t_dependent_plots_II.setInterval(500)
        self.timer_t_dependent_plots_II.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_t_dependent_plots_II.timeout.connect(self.t_dependent_plot_updates_II)
        self.timer_t_dependent_plots_II.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
        
        #++ timer for the update of the cam +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.timer_cam_pic = QtCore.QTimer()
        self.timer_cam_pic.setInterval(1000)
        self.timer_cam_pic.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_cam_pic.timeout.connect(self.timer_cam_pic_updates)
        self.timer_cam_pic.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        
        
        #++ timer for of the Be creation parameters +++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.timer_Be_creation = QtCore.QTimer()
        self.timer_Be_creation.setInterval(500)
        self.timer_Be_creation.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_Be_creation.timeout.connect(self.read_para_Be_creation)
        self.timer_Be_creation.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#


        #++ timer for of the 313 fiber piezo  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.timer_313_aom_piezo = QtCore.QTimer()
        self.timer_313_aom_piezo.setInterval(1000)
        self.timer_313_aom_piezo.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_313_aom_piezo.timeout.connect(self.read_para_313_aom_change)
        self.timer_313_aom_piezo.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#

        #++ timer for of the 313 fiber piezo  +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#
        self.timer_313_piezo = QtCore.QTimer()
        self.timer_313_piezo.setInterval(1000)
        self.timer_313_piezo.setTimerType(QtCore.Qt.PreciseTimer)
        self.timer_313_piezo.timeout.connect(self.read_para_313_change)
        self.timer_313_piezo.start()
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++#




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ the second part of the class contains all the FUNCTIONS which are  ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ triggerered when the different push buttons are pressed. there are ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~ more functions dedicated to permanet monitoring and backgroundjobs ~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~ SEQUENCE 01 TAB ~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 

    #~~ loads the parameters for the berylium creation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def load_para_be_creation_seq_01(self):
        the_program.load_be_creation_time_seq_01 = self.doubleSpinBox_be_creation_time_seq_01.value()
        
        the_program.sequ_01_be_creation_load(str(self.lineEdit_be_creation_seq_01.text()))
        
        self.doubleSpinBox_t_oven_emission.setValue(the_program.load_be_creation_seq_01[0])
        self.doubleSpinBox_t_oven_stand_by.setValue(the_program.load_be_creation_seq_01[1])

        self.doubleSpinBox_i_oven_emission.setValue(the_program.load_be_creation_seq_01[2])
        self.doubleSpinBox_i_oven_stand_by.setValue(the_program.load_be_creation_seq_01[3])
        
        self.doubleSpinBox_t_egun_delay.setValue(the_program.load_be_creation_seq_01[4])
        self.doubleSpinBox_t_egun_emission.setValue(the_program.load_be_creation_seq_01[5])
        
        self.doubleSpinBox_i_fil_emission.setValue(the_program.load_be_creation_seq_01[6])
        self.doubleSpinBox_i_fil_stand_by.setValue(the_program.load_be_creation_seq_01[7])
        
        self.doubleSpinBox_v_fil_emission.setValue(the_program.load_be_creation_seq_01[8])
        self.doubleSpinBox_v_fil_stand_by.setValue(the_program.load_be_creation_seq_01[9])
        
        self.doubleSpinBox_v_weh_emission.setValue(the_program.load_be_creation_seq_01[10])
        self.doubleSpinBox_v_weh_stand_by.setValue(the_program.load_be_creation_seq_01[11])
        
        self.spinBox_n_rep_Be_creation.setValue(1)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def delete_para_be_creation_seq_01(self):
        the_program.load_be_creation_seq_01 = [0,0,0,0,0,0,0,0,0,0,0,0,0]
        the_program.load_be_creation_time_seq_01 = 0.0
        self.doubleSpinBox_be_creation_time_seq_01.setValue(0.0)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def load_para_trap_voltages_seq_01(self):  
        the_program.sequ_01_trap_voltages_load(str(self.lineEdit_trap_voltages_seq_01.text()))       
        self.label_trap_voltages_n_seq_01.setText(str(the_program.load_trap_voltages_n_seq_01))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def load_para_trap_voltages_seq_01_time_add(self):
        the_program.load_trap_voltages_times_seq_01.append(float(self.doubleSpinBox_trap_voltages_time_seq_01.value()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    def load_para_trap_voltages_seq_01_time_delete(self):
        the_program.load_trap_voltages_times_seq_01 = the_program.load_trap_voltages_times_seq_01[:-1]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def load_para_trap_voltages_seq_01_init(self):
        the_program.sequ_01_trap_voltages_init()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def piezo_seq_01_add(self):
        the_program.piezo_controller_list_seq_01.append(float(self.doubleSpinBox_piezo_seq_01.value()))
        the_program.piezo_controller_list_times_seq_01.append(float(self.doubleSpinBox_piezo_seq_01_time.value()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def piezo_seq_01_delete(self):
        the_program.piezo_controller_list_seq_01 = the_program.piezo_controller_list_seq_01[:-1]
        the_program.piezo_controller_list_times_seq_01 = the_program.piezo_controller_list_times_seq_01[:-1]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    def aom_seq_01_add(self):
        the_program.aom_list_seq_01.append(float(self.doubleSpinBox_aom_seq_01.value()))
        the_program.aom_list_times_seq_01.append(float(self.doubleSpinBox_aom_seq_01_time.value()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def aom_seq_01_delete(self):
        the_program.aom_list_seq_01 = the_program.aom_list_seq_01[:-1]
        the_program.aom_list_times_seq_01 = the_program.aom_list_times_seq_01[:-1]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#  
    def pic_seq_01_add(self):
        the_program.pic_list_times_seq_01.append(float(self.doubleSpinBox_pic_seq_01_time.value()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def pic_seq_01_delete(self):
        the_program.pic_list_times_seq_01 = the_program.pic_list_times_seq_01[:-1]
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
               
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#           
    def seq_01_save(self):
        the_program.save_seq_01_config(str(self.lineEdit_crystal_creation_seq_01_save.text()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#           
    def seq_01_load(self):
        the_program.load_seq_01_config(str(self.lineEdit_crystal_creation_seq_01_load.text()))
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~ CAMERA TAB ~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~# 


    #~~ first three FUNCTIONS are only to activate and deactivate the buttons ~~~~~~~~~~~~~~~~~~~~~~~~~#

    # when initialize button pressed -> enable communication with input options
    def input_cam_initialize(self):
        self.pushButton_cam_INITIALIZE.setEnabled(False)
        
        
        self.doubleSpinBox_cam_temp_set.setEnabled(True)
        self.pushButton_cam_temp_set.setEnabled(True)
        
        self.comboBox.setEnabled(True)
        
        self.doubleSpinBox_cam_exposure_time.setEnabled(True)
        self.pushButton_cam_exposure_time.setEnabled(True)
        
        self.pushButton_cam_OFF.setEnabled(True)
        
    # when off button pressed -> disable communication with input options   
    def input_cam_off(self):
        self.pushButton_cam_INITIALIZE.setEnabled(True)
        
        self.doubleSpinBox_cam_temp_set.setEnabled(False)
        self.pushButton_cam_temp_set.setEnabled(False)
        
        self.comboBox.setCurrentIndex(0)
        self.comboBox.setEnabled(False)
        
        self.doubleSpinBox_cam_exposure_time.setEnabled(False)
        self.pushButton_cam_exposure_time.setEnabled(False)
        
        self.pushButton_cam_OFF.setEnabled(False)  

    # decide what happens in the two different modi of the camera
    def input_cam(self):
        if self.comboBox.currentIndex() == 0:
            self.doubleSpinBox_cam_exposure_time.setEnabled(False)
            self.pushButton_cam_trigger_single_pic.setEnabled(False)
            
            the_program.camera.flag_modus = 0
            
        elif self.comboBox.currentIndex() == 1:
            self.doubleSpinBox_cam_exposure_time.setEnabled(True)
            self.pushButton_cam_trigger_single_pic.setEnabled(True)
            
            the_program.camera.flag_modus = 1
            
        elif self.comboBox.currentIndex() == 2:
            self.doubleSpinBox_cam_exposure_time.setEnabled(True)
            self.pushButton_cam_trigger_single_pic.setEnabled(False)
            
            the_program.camera.flag_modus = 2
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ initialize camera ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def apply_cam_init(self):
        thread_cam_A = threading.Thread(target=the_program.cam_init)
        thread_cam_A.start()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ set trigger for shutting down  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#   
    def apply_cam_stop(self):
        the_program.cam_off()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    
    
    #~~ set trigger to do a picture ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def apply_trig_pic(self):
        the_program.do_single_pic()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        

    #~~ change the desired temperature of the camera ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def apply_cooling_change(self):
        the_program.camera.wanted_temperature = self.doubleSpinBox_cam_temp_set.value()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        

    #~~ read exposure time ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    def read_para_cam_exp_time_from_gui_into_instance(self):
        the_program.camera.exposure_time = self.doubleSpinBox_cam_exposure_time.value()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~ TRAP TAB ~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#         

        
    #~~ FUNCTIONS for settings: dc voltages ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    # read parameters for electrode 1
    def read_para_trap_dc1_from_gui_into_instance(self):
        the_program.dc_1 = self.doubleSpinBox_el_1.value()

    # read parameters for electrode 2
    def read_para_trap_dc2_from_gui_into_instance(self):
        the_program.dc_2 = self.doubleSpinBox_el_2.value()
   
    # read parameters for electrode 3    
    def read_para_trap_dc3_from_gui_into_instance(self):
        the_program.dc_3 = self.doubleSpinBox_el_3.value()

    # read parameters for electrode 4
    def read_para_trap_dc4_from_gui_into_instance(self):
        the_program.dc_4 = self.doubleSpinBox_el_4.value()

    # read parameters for electrode 5        
    def read_para_trap_dc5_from_gui_into_instance(self):
        the_program.dc_5 = self.doubleSpinBox_el_5.value()
    
    # read parameters for electrode 6
    def read_para_trap_dc6_from_gui_into_instance(self):
        the_program.dc_6 = self.doubleSpinBox_el_6.value()
    
    # read parameters for electrode 7
    def read_para_trap_dc7_from_gui_into_instance(self):
        the_program.dc_7 = self.doubleSpinBox_el_7.value()
    
    # read parameters for electrode 8
    def read_para_trap_dc8_from_gui_into_instance(self):
        the_program.dc_8 = self.doubleSpinBox_el_8.value()

    # read all together             
    def read_para_trap_dc_from_gui_into_instance(self):
        self.read_para_trap_dc1_from_gui_into_instance()
        self.read_para_trap_dc2_from_gui_into_instance()
        self.read_para_trap_dc3_from_gui_into_instance()
        self.read_para_trap_dc4_from_gui_into_instance()
        self.read_para_trap_dc5_from_gui_into_instance()
        self.read_para_trap_dc6_from_gui_into_instance()
        self.read_para_trap_dc7_from_gui_into_instance()
        self.read_para_trap_dc8_from_gui_into_instance()


    # apply parameters for electrode 1
    def apply_para_trap_dc1_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_1,"Dev3/ao0")

    # apply parameters for electrode 2        
    def apply_para_trap_dc2_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_2,"Dev3/ao1")

    # apply parameters for electrode 3        
    def apply_para_trap_dc3_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_3,"Dev3/ao2")

    # apply parameters for electrode 4        
    def apply_para_trap_dc4_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_4,"Dev3/ao3")

    # apply parameters for electrode 5        
    def apply_para_trap_dc5_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_5,"Dev3/ao4")
   
   # apply parameters for electrode 6     
    def apply_para_trap_dc6_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_6,"Dev3/ao5")

    # apply parameters for electrode 7        
    def apply_para_trap_dc7_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_7,"Dev3/ao6")

    # apply parameters for electrode 8        
    def apply_para_trap_dc8_on_device(self):     
        the_program.apply_dc_voltage_to_el(the_program.dc_8,"Dev3/ao7")

      
        
#    def load_para(self):
#        the_program.load_trap_config()
#        
#        self.doubleSpinBox_el_1.setValue(the_program.load_all_voltages[0])
#        self.doubleSpinBox_el_2.setValue(the_program.load_all_voltages[1])
#        self.doubleSpinBox_el_3.setValue(the_program.load_all_voltages[2])
#        self.doubleSpinBox_el_4.setValue(the_program.load_all_voltages[3])
#        self.doubleSpinBox_el_5.setValue(the_program.load_all_voltages[4])
#        self.doubleSpinBox_el_6.setValue(the_program.load_all_voltages[5])
#        self.doubleSpinBox_el_7.setValue(the_program.load_all_voltages[6])
#        self.doubleSpinBox_el_8.setValue(the_program.load_all_voltages[7])
#
#        self.doubleSpinBox_rf_ampl.setValue(the_program.load_all_voltages[8])
#        self.doubleSpinBox_rf_freq.setValue(the_program.load_all_voltages[9])
        


    # apply all together              
    def apply_para_trap_dc_on_device(self):     
        self.apply_para_trap_dc1_on_device()
        self.apply_para_trap_dc2_on_device()
        self.apply_para_trap_dc3_on_device()
        self.apply_para_trap_dc4_on_device()
        self.apply_para_trap_dc5_on_device()
        self.apply_para_trap_dc6_on_device()
        self.apply_para_trap_dc7_on_device()
        self.apply_para_trap_dc8_on_device()

    # turn dc to zero       
    def dc_to_zero(self):
        self.doubleSpinBox_el_1.setValue(0.0)
        self.doubleSpinBox_el_2.setValue(0.0)
        self.doubleSpinBox_el_3.setValue(0.0)
        self.doubleSpinBox_el_4.setValue(0.0)
        self.doubleSpinBox_el_5.setValue(0.0)
        self.doubleSpinBox_el_6.setValue(0.0)
        self.doubleSpinBox_el_7.setValue(0.0)
        self.doubleSpinBox_el_8.setValue(0.0)

        self.read_para_trap_dc_from_gui_into_instance()
        self.apply_para_trap_dc_on_device()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ FUNCTIONS for settings: rf voltage ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    # read rf frequency    
    def read_para_trap_rf_frequency_from_gui_into_instance(self):
        the_program.rf_frequency = 1000000*self.doubleSpinBox_rf_freq.value()
        
    # read rf amplitude
    def read_para_trap_rf_amplitude_from_gui_into_instance(self):
        the_program.rf_amplitude_ampl = int(self.doubleSpinBox_rf_amplitude_ampl.value())
        the_program.rf_amplitude = self.doubleSpinBox_rf_ampl.value()


    # apply rf frequency          
    def apply_para_trap_rf_frequency_on_device(self):     
        the_program.set_rf_frequency()
        
    # apply rf amplitude 
    def apply_para_trap_rf_amplitude_on_device(self):     
        the_program.set_rf_amplitude()
        

    # apply bothe together 
    def apply_para_trap_rf_on_device_off(self):
        self.doubleSpinBox_rf_ampl.setValue(0.0)
        self.doubleSpinBox_rf_freq.setValue(0.0)
        
        self.read_para_trap_rf_amplitude_from_gui_into_instance()
        self.read_para_trap_rf_frequency_from_gui_into_instance()
        self.apply_para_trap_rf_amplitude_on_device()
        self.apply_para_trap_rf_frequency_on_device()
        
        the_program.set_rf_off()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
       
    #~~ FUNCTIONS for functions: trap ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
    # set dc to trapping voltages
    def set_dc_endcaps(self):
        the_program.dc_endcaps = self.doubleSpinBox_endcap_voltages.value()
        
        the_program.dc_2 = the_program.dc_endcaps
        the_program.dc_4 = the_program.dc_endcaps
        the_program.dc_5 = the_program.dc_endcaps
        the_program.dc_7 = the_program.dc_endcaps
        
        self.doubleSpinBox_el_2.setValue(the_program.dc_endcaps)
        self.doubleSpinBox_el_4.setValue(the_program.dc_endcaps)
        self.doubleSpinBox_el_5.setValue(the_program.dc_endcaps)
        self.doubleSpinBox_el_7.setValue(the_program.dc_endcaps)
        
        self.apply_para_trap_dc2_on_device()
        self.apply_para_trap_dc4_on_device()
        self.apply_para_trap_dc5_on_device()
        self.apply_para_trap_dc7_on_device()       
        
    # set dc to trapping voltages
    def set_dc_center(self):
        the_program.dc_center = self.doubleSpinBox_center_voltages.value()

        the_program.dc_1 = the_program.dc_center
        the_program.dc_3 = the_program.dc_center
        the_program.dc_6 = the_program.dc_center
        the_program.dc_8 = the_program.dc_center

        self.doubleSpinBox_el_1.setValue(the_program.dc_center)
        self.doubleSpinBox_el_3.setValue(the_program.dc_center)
        self.doubleSpinBox_el_6.setValue(the_program.dc_center)
        self.doubleSpinBox_el_8.setValue(the_program.dc_center)

        self.apply_para_trap_dc1_on_device()
        self.apply_para_trap_dc3_on_device()
        self.apply_para_trap_dc6_on_device()
        self.apply_para_trap_dc8_on_device()


    
    # set dc to extract all particles
    def extraction_pulse(self):
        self.doubleSpinBox_el_1.setValue(-10.0)
        self.doubleSpinBox_el_2.setValue(-10.0)
        self.doubleSpinBox_el_3.setValue(-10.0)
        self.doubleSpinBox_el_4.setValue(-10.0)
        self.doubleSpinBox_el_5.setValue(10.0)
        self.doubleSpinBox_el_6.setValue(10.0)
        self.doubleSpinBox_el_7.setValue(10.0)
        self.doubleSpinBox_el_8.setValue(10.0)

        self.read_para_trap_dc_from_gui_into_instance()        
        self.apply_para_trap_dc_on_device()
 

       
    def trap_tighten_potential(self):   
        self.doubleSpinBox_el_1.setValue(-10.0)
        self.doubleSpinBox_el_2.setValue(10.0)
        self.doubleSpinBox_el_3.setValue(-10.0)
        self.doubleSpinBox_el_4.setValue(10.0)
        self.doubleSpinBox_el_5.setValue(10.0)
        self.doubleSpinBox_el_6.setValue(-10.0)
        self.doubleSpinBox_el_7.setValue(10.0)
        self.doubleSpinBox_el_8.setValue(-10.0)
        
        self.read_para_trap_dc_from_gui_into_instance()        
        self.apply_para_trap_dc_on_device()        
     

    def trap_losen_potential(self):   
        self.doubleSpinBox_el_1.setValue(0)
        self.doubleSpinBox_el_2.setValue(10.0)
        self.doubleSpinBox_el_3.setValue(0)
        self.doubleSpinBox_el_4.setValue(10.0)
        self.doubleSpinBox_el_5.setValue(10.0)
        self.doubleSpinBox_el_6.setValue(0)
        self.doubleSpinBox_el_7.setValue(10.0)
        self.doubleSpinBox_el_8.setValue(0)
        
        self.read_para_trap_dc_from_gui_into_instance()        
        self.apply_para_trap_dc_on_device()    
        
        
    def trap_move_x_1567(self):
        
        shift = self.doubleSpinBox_shift_x_1567.value()
        
        self.doubleSpinBox_el_1.setValue(the_program.dc_1+shift)
        self.doubleSpinBox_el_5.setValue(the_program.dc_5+shift)
        self.doubleSpinBox_el_6.setValue(the_program.dc_6+shift)
        self.doubleSpinBox_el_7.setValue(the_program.dc_7+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[1,5,6,7])
     
    def trap_move_x_2348(self):
        
        shift = self.doubleSpinBox_shift_x_2348.value()
        
        self.doubleSpinBox_el_2.setValue(the_program.dc_2+shift)
        self.doubleSpinBox_el_3.setValue(the_program.dc_3+shift)
        self.doubleSpinBox_el_4.setValue(the_program.dc_4+shift)
        self.doubleSpinBox_el_8.setValue(the_program.dc_8+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[2,3,4,8])
        
        
        
    def trap_move_y_5678(self):
        
        shift = self.doubleSpinBox_shift_y_5678.value()
        
        self.doubleSpinBox_el_5.setValue(the_program.dc_5+shift)
        self.doubleSpinBox_el_6.setValue(the_program.dc_6+shift)
        self.doubleSpinBox_el_7.setValue(the_program.dc_7+shift)
        self.doubleSpinBox_el_8.setValue(the_program.dc_8+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[5,6,7,8])
     
     
     
    def trap_move_y_1234(self):
        
        shift = self.doubleSpinBox_shift_y_1234.value()
        
        self.doubleSpinBox_el_1.setValue(the_program.dc_1+shift)
        self.doubleSpinBox_el_2.setValue(the_program.dc_2+shift)
        self.doubleSpinBox_el_3.setValue(the_program.dc_3+shift)
        self.doubleSpinBox_el_4.setValue(the_program.dc_4+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[1,2,3,4])
        
        
    def trap_move_z_27(self):
        
        shift = self.doubleSpinBox_shift_z_27.value()
        
        self.doubleSpinBox_el_2.setValue(the_program.dc_2+shift)
        self.doubleSpinBox_el_7.setValue(the_program.dc_7+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[2,7])
        
        
        
        
    def trap_move_z_45(self):
        
        shift = self.doubleSpinBox_shift_z_45.value()
        
        self.doubleSpinBox_el_4.setValue(the_program.dc_4+shift)
        self.doubleSpinBox_el_5.setValue(the_program.dc_5+shift)
        
        self.read_para_trap_dc_from_gui_into_instance()
        
        the_program.add_dc_voltages_to_els(shift,[4,5]) 
        
        
        
    def trap_sweep_rf(self):
        the_program.v_start_rf_sweep = self.doubleSpinBox_sweep_ampl_start.value()
        the_program.v_stop_rf_sweep = self.doubleSpinBox_sweep_ampl_stop.value()
        the_program.t_duration_rf_sweep = self.doubleSpinBox_sweep_ampl_duration.value()           
        thread_sweep_rf = threading.Thread(target=the_program.smooth_change_rf_amplitude)
        thread_sweep_rf.start()
        
    def trap_sweep_rf_abort(self):
        
        the_program.breaker_change_rf_amplitude = 1
               
               
    def el_save(self):
        the_program.save_trap_config(str(self.lineEdit_save_voltages.text()))        
        
        
    def el_load(self):
        
        the_program.load_trap_config(str(self.lineEdit_import_voltages.text()))
        
        self.doubleSpinBox_el_1.setValue(the_program.load_all_voltages[0])
        self.doubleSpinBox_el_2.setValue(the_program.load_all_voltages[1])
        self.doubleSpinBox_el_3.setValue(the_program.load_all_voltages[2])
        self.doubleSpinBox_el_4.setValue(the_program.load_all_voltages[3])
        self.doubleSpinBox_el_5.setValue(the_program.load_all_voltages[4])
        self.doubleSpinBox_el_6.setValue(the_program.load_all_voltages[5])
        self.doubleSpinBox_el_7.setValue(the_program.load_all_voltages[6])
        self.doubleSpinBox_el_8.setValue(the_program.load_all_voltages[7])

        self.doubleSpinBox_rf_ampl.setValue(the_program.load_all_voltages[8])
        self.doubleSpinBox_rf_freq.setValue(the_program.load_all_voltages[9])          
        
        
        
        
        
        
        
        
        
    # read the values for the calibration function
    def read_calibration_from_gui_into_instance(self):
        the_program.rf_cali_f_start = self.doubleSpinBox_calib_start.value()
        the_program.rf_cali_f_stop = self.doubleSpinBox_calib_stop.value()
        the_program.rf_cali_step_size = self.doubleSpinBox_calib_step.value()
    
    # do the calibration function
    def do_calibration(self):
        thread_apply_frequency = threading.Thread(target=the_program.do_calibration_frequency)
        thread_apply_frequency.start()
        
    def abort_calibration(self):        
        the_program.breaker_calibration = 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

     
        
        
    
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ OVEN AND EGUN TAB ~ OVEN AND EGUN TAB ~ OVEN AND EGUN TAB ~ OVEN AND EGUN TAB ~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    
    #~~ oven current ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def read_para_oven_current_from_gui_into_instance(self):
        the_program.oven_current = self.doubleSpinBox_current_oven.value()
        
    def apply_para_oven_current_on_device(self):     
        the_program.apply_oven_current2(the_program.oven_current)
     
    def apply_para_oven_current_on_device_off(self):
        the_program.apply_oven_current2_off()
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
   

    #~~ FUNCTIONS for settings: egun ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
    # egun current filament
    def read_para_egun_current_filament_from_gui_into_instance(self):
        the_program.egun_current_filament = self.doubleSpinBox_current_filament.value()
        
    def apply_para_egun_current_filament_on_device(self):     
        the_program.apply_egun_current_filament2(the_program.egun_current_filament)

    def apply_para_egun_current_filament_on_device_off(self):
        the_program.apply_egun_current_filament2(0)        
        
    # egun voltage filament
    def read_para_egun_voltage_filament_from_gui_into_instance(self):
        the_program.egun_voltage_filament = self.doubleSpinBox_voltage_filament.value()
        
    def apply_para_egun_voltage_filament_on_device(self):     
        the_program.apply_egun_voltage_filament(the_program.egun_voltage_filament)
        
    def apply_para_egun_voltage_filament_on_device_off(self):     
        the_program.apply_egun_voltage_filament(0)      
       
    # egun voltage wehnelt
    def read_para_egun_voltage_wehnelt_from_gui_into_instance(self):
        the_program.egun_voltage_wehnelt = self.doubleSpinBox_voltage_wehnelt.value()
        
    def apply_para_egun_voltage_wehnelt_on_device(self):     
        the_program.apply_egun_voltage_wehnelt(the_program.egun_voltage_wehnelt)
        
    def apply_para_egun_voltage_wehnelt_on_device_off(self):     
        the_program.apply_egun_voltage_wehnelt(0)
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        

    #~~ FUNCTIONS for function: Be+ creation ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    # read sequence parameters
    def read_para_Be_creation(self):
        the_program.t_oven_emission = self.doubleSpinBox_t_oven_emission.value()
        the_program.t_oven_stand_by = self.doubleSpinBox_t_oven_stand_by.value()

        the_program.i_oven_emission = self.doubleSpinBox_i_oven_emission.value()
        the_program.i_oven_stand_by = self.doubleSpinBox_i_oven_stand_by.value()
        
        the_program.t_egun_delay = self.doubleSpinBox_t_egun_delay.value()
        the_program.t_egun_emission = self.doubleSpinBox_t_egun_emission.value()
        
        the_program.i_fil_emission = self.doubleSpinBox_i_fil_emission.value()
        the_program.i_fil_stand_by = self.doubleSpinBox_i_fil_stand_by.value()
        
        the_program.v_fil_emission = self.doubleSpinBox_v_fil_emission.value()
        the_program.v_fil_stand_by = self.doubleSpinBox_v_fil_stand_by.value()
        
        the_program.v_weh_emission = self.doubleSpinBox_v_weh_emission.value()
        the_program.v_weh_stand_by = self.doubleSpinBox_v_weh_stand_by.value()
        
        the_program.n_rep = self.spinBox_n_rep_Be_creation.value()  


    def load_para_be_creation(self):
        the_program.load_be_creation_config(str(self.lineEdit_be_creation_load.text()))
        
        self.doubleSpinBox_t_oven_emission.setValue(the_program.load_be_creation[0])
        self.doubleSpinBox_t_oven_stand_by.setValue(the_program.load_be_creation[1])

        self.doubleSpinBox_i_oven_emission.setValue(the_program.load_be_creation[2])
        self.doubleSpinBox_i_oven_stand_by.setValue(the_program.load_be_creation[3])
        
        self.doubleSpinBox_t_egun_delay.setValue(the_program.load_be_creation[4])
        self.doubleSpinBox_t_egun_emission.setValue(the_program.load_be_creation[5])
        
        self.doubleSpinBox_i_fil_emission.setValue(the_program.load_be_creation[6])
        self.doubleSpinBox_i_fil_stand_by.setValue(the_program.load_be_creation[7])
        
        self.doubleSpinBox_v_fil_emission.setValue(the_program.load_be_creation[8])
        self.doubleSpinBox_v_fil_stand_by.setValue(the_program.load_be_creation[9])
        
        self.doubleSpinBox_v_weh_emission.setValue(the_program.load_be_creation[10])
        self.doubleSpinBox_v_weh_stand_by.setValue(the_program.load_be_creation[11])
        
        self.spinBox_n_rep_Be_creation.setValue(the_program.load_be_creation[12]) 
  





    # start Be+ creation
    def apply_Be_creation(self):
        thread_egun = threading.Thread(target=the_program.apply_Be_creation)
        thread_egun.start()
        
        thread_egun_counter = threading.Thread(target=the_program.Be_creation_counter)
        thread_egun_counter.start()
        
    def abort_Be_creation(self):        
        the_program.breaker_Be_creation = 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def be_creation_sequence_save(self):
        the_program.save_be_creation_config(str(self.lineEdit_be_creation_save.text()))     
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~ 313 LASER TAB ~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#    

    #~~ aom voltage ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def read_para_aom_volt_from_gui_into_instance(self):
        the_program.laser_313_aom_voltage = self.doubleSpinBox_313_aom.value()
        
    def apply_para_aom_volt_on_device(self):     
        the_program.apply_313_aom_set_voltage(the_program.laser_313_aom_voltage)

    def read_para_aom_volt_from_gui_into_instance_off(self):
        self.doubleSpinBox_313_aom.setValue(0.0)
        the_program.laser_313_aom_voltage = float(0.0)
        
    #~~ aom ttl ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def read_para_aom_ttl_from_gui_into_instance(self):
        the_program.laser_313_aom_ttl = self.doubleSpinBox_313_ttl.value()
        
    def apply_para_aom_ttl_on_device(self):     
        the_program.apply_313_aom_ttl(the_program.laser_313_aom_ttl)

    def read_para_aom_ttl_from_gui_into_instance_off(self):
        self.doubleSpinBox_313_ttl.setValue(0.0)
        the_program.laser_313_aom_ttl = float(0.0)
        
        
        
    #~~ aom piezo ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
    def read_para_313_piezo_from_gui_into_instance(self):
        the_program.laser_313_piezo_voltage = self.doubleSpinBox_313_piezo.value()
        
    def apply_para_313_piezo_on_device(self):     
        the_program.apply_313_piezo_set_voltage(the_program.laser_313_piezo_voltage)

    def read_para_313_piezo_from_gui_into_instance_off(self):
        self.doubleSpinBox_313_piezo.setValue(0.0)
        the_program.laser_313_piezo_voltage = float(0.0) 
 

    # read sequence parameters for 313 change AOM 
    def read_para_313_aom_change(self):
        the_program.laser_313_aom_u_start = self.doubleSpinBox_313_aom_u_start.value()
        the_program.laser_313_aom_u_step = self.doubleSpinBox_313_aom_u_step.value()
        the_program.change_fiber_laser_aom_delay = self.doubleSpinBox_313_aom_t_delay.value()
        the_program.laser_313_aom_n_incr = self.spinBox_313_aom_n_incr.value()
        
        the_program.laser_313_aom_t_break = self.doubleSpinBox_313_aom_t_break.value()
        the_program.laser_313_aom_n_rep = self.spinBox_313_aom_n_rep.value()
    
    # thread for for 313 change AOM
    def apply_313_aom_change(self):
        device = int(0)
        thread_313_aom_change = threading.Thread(target=the_program.smooth_change, kwargs={'device':device,'v_start':the_program.laser_313_aom_u_start, 'v_step':the_program.laser_313_aom_u_step, 'n_incr':the_program.laser_313_aom_n_incr, 'delay_incr':the_program.change_fiber_laser_aom_delay, 'n_rep':the_program.laser_313_aom_n_rep, 't_break':the_program.laser_313_aom_t_break})
        thread_313_aom_change.start()
       
        thread_313_aom_change_counter = threading.Thread(target=the_program.change_fiber_laser_aom_counter)
        thread_313_aom_change_counter.start()

    def abort_313_aom_sweep(self):        
        the_program.breaker_change_fiber_aom = 1



    # read sequence parameters for 313 change
    def read_para_313_change(self):
        the_program.laser_313_piezo_u_start = self.doubleSpinBox_313_piezo_u_start.value()
        the_program.laser_313_piezo_u_step = self.doubleSpinBox_313_piezo_u_step.value()
        the_program.change_fiber_laser_piezo_delay = self.doubleSpinBox_313_piezo_t_delay.value()
        the_program.laser_313_piezo_n_incr = self.spinBox_313_piezo_n_incr.value()
        
        the_program.laser_313_piezo_t_break = self.doubleSpinBox_313_piezo_t_break.value()
        the_program.laser_313_piezo_n_rep = self.spinBox_313_piezo_n_rep.value()
    
    # thread for for 313 change    
    def apply_313_change(self):
        device = int(1)
        thread_313_change = threading.Thread(target=the_program.smooth_change, kwargs={'device':device,'v_start':the_program.laser_313_piezo_u_start, 'v_step':the_program.laser_313_piezo_u_step, 'n_incr':the_program.laser_313_piezo_n_incr, 'delay_incr':the_program.change_fiber_laser_piezo_delay, 'n_rep':the_program.laser_313_piezo_n_rep, 't_break':the_program.laser_313_piezo_t_break})
        thread_313_change.start()
        
        thread_313_change_counter = threading.Thread(target=the_program.change_fiber_laser_piezo_counter)
        thread_313_change_counter.start()

    def abort_313_piezo_sweep(self):        
        the_program.breaker_change_fiber_piezo = 1
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

      


    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    #~~ ALL THE PLOTS ~ ALL THE PLOTS ~ ALL THE PLOTS ~ ALL THE PLOTS ~ ALL THE PLOTS ~~~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


    #~~ this (huge) FUNCTION does all the periodic plots for the monitoring etc ~~~~~~~~~~~~~~~~~~~~~~~#        
    def t_dependent_plot_updates(self):
            
        ### CAMERA TAB ######################################################################################
        #~~ the camera temperature ~~~~~~~~~~~~~#        
        self.plotted_cam_temp = self.plot_cam_temp.plot(the_program.x_values_difference_to_now,the_program.camera.temp_list, pen=redPen, symbol='o', symbolBrush=brush_red, name = 'temp cam', clear = True)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
        ###################################################################################################
        

        ### TRAP TAB ######################################################################################

        #~~ the dc electrode plots ~~~~~~~~~~~~~#        
        self.label_el_1.setText(str("{0:.3f}".format(the_program.dc_1)))
        self.label_el_2.setText(str("{0:.3f}".format(the_program.dc_2)))
        self.label_el_3.setText(str("{0:.3f}".format(the_program.dc_3)))
        self.label_el_4.setText(str("{0:.3f}".format(the_program.dc_4)))
        self.label_el_5.setText(str("{0:.3f}".format(the_program.dc_5)))
        self.label_el_6.setText(str("{0:.3f}".format(the_program.dc_6)))
        self.label_el_7.setText(str("{0:.3f}".format(the_program.dc_7)))
        self.label_el_8.setText(str("{0:.3f}".format(the_program.dc_8)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #~~ the rf electrode plots ~~~~~~~~~~~~~#        
        self.label_rf_frequ.setText(str("{0:.2f}".format(the_program.rf_frequency*(1/1000000))))
        self.label_rf_ampl.setText(str("{0:.2f}".format(the_program.rf_osc_rms*1.414)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        
        #~~ the rf sweep progress plots ~~~~~~~~#        
        self.progressBar_sweep_rf.setValue(the_program.counter_rf_sweep)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        


        #~~ the trap analysis plots ~~~~~~~~~~~~#        
        self.plotted_stability_plot = self.stability_plot.plot(the_program.trap_stability_x_values,the_program.trap_stability_y_values, fillLevel=0, brush=brush_blue, name = 'stability diagram', clear = True)
        self.plotted_stability_plot2 = self.stability_plot.plot(the_program.trap_stability_x_values,the_program.trap_stability_y2_values, fillLevel=0, brush=brush_blue, name = 'stability diagram 2')
        self.plotted_position = self.stability_plot.plot([the_program.trap_qx_Be],[the_program.trap_ax_Be], pen=redPen, symbol='o', symbolSize=(12), symbolBrush = brush_red, name = 'stability diagram position')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #~~ the rf calibration plot ~~~~~~~~~~~~#
        self.plotted_monitoring_rf_calibration = self.plot_rf_calibration.plot(the_program.rf_cali_x_values,the_program.rf_cali_y_values, pen=redPen, symbol='o', symbolBrush = brush_red, name = 'pressure', clear = True)        
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ###################################################################################################



              
        ### OVEN AND EGUN TAB #############################################################################
              
        #~~ the be creation monitoring ~~~~~~~~~#        
        self.label_oven_i.setText(str("{0:.2f}".format(the_program.oven_current)))
        self.label_e_gun_i_fil.setText(str("{0:.2f}".format(the_program.egun_current_filament)))
        self.label_e_gun_u_fil.setText(str("{0:.0f}".format(the_program.egun_voltage_filament)))
        self.label_e_gun_i_weh.setText(str("{0:.0f}".format(the_program.egun_voltage_wehnelt)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #~~ the egun sequence plots ~~~~~~~~~~~~#
        x_values_oven_current = [0]
        y_values_oven_current = []

        x_values_egun = [0]
        y_values_egun_current_filament = []
        y_values_egun_voltage_filament = []
        y_values_egun_voltage_wehnelt = []

        dur = the_program.t_oven_emission + the_program.t_oven_stand_by

        # creates the plot for the oven and egun sequence
        for i in range(the_program.n_rep):
            
            x_values_oven_current.append(the_program.t_oven_emission + i*dur)
            x_values_oven_current.append(the_program.t_oven_emission+the_program.t_oven_stand_by + i*dur)
            y_values_oven_current.append(the_program.i_oven_emission)
            y_values_oven_current.append(the_program.i_oven_stand_by)
            
            x_values_egun.append(the_program.t_egun_delay + i*dur)
            x_values_egun.append(the_program.t_egun_delay+the_program.t_egun_emission + i*dur)
            x_values_egun.append(the_program.t_oven_emission+the_program.t_oven_stand_by + i*dur)

            y_values_egun_current_filament.append(the_program.i_fil_stand_by)
            y_values_egun_current_filament.append(the_program.i_fil_emission)
            y_values_egun_current_filament.append(the_program.i_fil_stand_by)
            
            y_values_egun_voltage_filament.append(the_program.v_fil_stand_by)
            y_values_egun_voltage_filament.append(the_program.v_fil_emission)
            y_values_egun_voltage_filament.append(the_program.v_fil_stand_by)
            
            y_values_egun_voltage_wehnelt.append(the_program.v_weh_stand_by)
            y_values_egun_voltage_wehnelt.append(the_program.v_weh_emission)
            y_values_egun_voltage_wehnelt.append(the_program.v_weh_stand_by)


        self.plotted_oven_current = self.plot_oven_current.plot(x_values_oven_current,y_values_oven_current, stepMode=True, fillLevel=0, brush=brush_red, name = 'Be creation', clear = True)        
        self.plotted_oven_current_timer = self.plot_oven_current.plot([the_program.be_creation_flag,the_program.be_creation_flag],[-0.5,3.5], pen=dashPen, symbol='o', symbolBrush = brush_black, name = 'oven current timer')

        self.plotted_egun_current = self.plot_egun_current.plot(x_values_egun,y_values_egun_current_filament, stepMode=True, fillLevel=0, brush=brush_red, name = 'Be creation', clear = True)
        self.plotted_egun_current_timer = self.plot_egun_current.plot([the_program.be_creation_flag,the_program.be_creation_flag],[-0.3,2], pen=dashPen, symbol='o', symbolBrush = brush_black, name = 'filament current timer')
        self.plotted_egun_voltages = self.plot_egun_voltages.plot(x_values_egun,y_values_egun_voltage_filament, stepMode=True, fillLevel=0, brush=brush_yellow, name = 'Be creation', clear = True)
        self.plotted_egun_voltages = self.plot_egun_voltages.plot(x_values_egun,y_values_egun_voltage_wehnelt, stepMode=True, fillLevel=0, brush=brush_blue, name = 'Be creation')
        self.plotted_egun_voltages_timer = self.plot_egun_voltages.plot([the_program.be_creation_flag,the_program.be_creation_flag],[-160,10], pen=dashPen, symbol='o', symbolBrush = brush_black, name = 'voltages timer')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ###################################################################################################
        
        
        ### ION PUMP TAB ##################################################################################
        #~~ the ion pump pressure temperature ~~#        
        self.plotted_pressure = self.plot_pressure.plot(the_program.x_values_difference_to_now,the_program.pressure_ion_pump_digital_monitoring, pen=redPen, symbol='o', symbolBrush = brush_red, name = 'pressure', clear = True)
        self.plotted_pressure_seq_01 = self.plot_pressure_seq_01.plot(the_program.x_values_difference_to_now,the_program.pressure_ion_pump_digital_monitoring, pen=redPen, symbol='o', symbolBrush = brush_red, name = 'pressure', clear = True)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
        ###################################################################################################        




        ### 313 COOLING LASER CHANGE #######################################################################
        self.label_laser_313_aom_voltage.setText(str("{0:.2f}".format(the_program.laser_313_aom_voltage)))
        self.label_laser_313_piezo_voltage.setText(str("{0:.2f}".format(the_program.laser_313_piezo_voltage_measured)))
        #~~ COOLING LASER CHANGE AOM plots ~~~~~~~~~~~#
        x_values_fiber_aom_time = [0]
        y_values_fiber_aom_volts = []
        
        for i in range(the_program.laser_313_aom_n_rep):
            t_start = i*(the_program.laser_313_aom_t_break+(the_program.laser_313_aom_n_incr+1)*the_program.change_fiber_laser_aom_delay)
            u_start = the_program.laser_313_aom_u_start + i*(the_program.laser_313_aom_u_step)
            
            for j in range(the_program.laser_313_aom_n_incr + 1):
                x_values_fiber_aom_time.append(t_start+(j+1)*the_program.change_fiber_laser_aom_delay)
                y_values_fiber_aom_volts.append(u_start+j*the_program.laser_313_aom_u_step/the_program.laser_313_aom_n_incr)             


        self.plotted_313_aom_change = self.plot_313_aom_change.plot(x_values_fiber_aom_time,y_values_fiber_aom_volts, stepMode=True, fillLevel=0, brush=brush_red, name = '313 aom', clear = True)        
        self.plotted_313_aom_change_timer = self.plot_313_aom_change.plot([the_program.laser_313_aom_flag,the_program.laser_313_aom_flag],[-1,6], pen=dashPen, symbol='o', symbolBrush = brush_black, name = '313 aom timer')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
       
        #~~ COOLING LASER CHANGE PIEZO plots ~~~~~~~~~~~#
        x_values_fiber_piezo_time = [0]
        y_values_fiber_piezo_volts = []
        
        for i in range(the_program.laser_313_piezo_n_rep):
            t_start = i*(the_program.laser_313_piezo_t_break+(the_program.laser_313_piezo_n_incr+1)*the_program.change_fiber_laser_piezo_delay)
            u_start = the_program.laser_313_piezo_u_start + i*(the_program.laser_313_piezo_u_step)
            
            for j in range(the_program.laser_313_piezo_n_incr + 1):
                x_values_fiber_piezo_time.append(t_start+(j+1)*the_program.change_fiber_laser_piezo_delay)
                y_values_fiber_piezo_volts.append(u_start+j*the_program.laser_313_piezo_u_step/the_program.laser_313_piezo_n_incr)             


        self.plotted_313_change = self.plot_313_change.plot(x_values_fiber_piezo_time,y_values_fiber_piezo_volts, stepMode=True, fillLevel=0, brush=brush_blue, name = '313 piezo', clear = True)        
        self.plotted_313_change_timer = self.plot_313_change.plot([the_program.laser_313_flag,the_program.laser_313_flag],[-10,160], pen=dashPen, symbol='o', symbolBrush = brush_black, name = '313 piezo timer')
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        ###################################################################################################
        

    #~~ this FUNCTION does all monitoring for the seq 01 tab ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        
    def t_dependent_plot_updates_II(self):
        
        #~~ the dc electrode plots ~~~~~~~~~~~~~#        
        self.label_el_1_seq_01.setText(str("{0:.3f}".format(the_program.dc_1)))
        self.label_el_2_seq_01.setText(str("{0:.3f}".format(the_program.dc_2)))
        self.label_el_3_seq_01.setText(str("{0:.3f}".format(the_program.dc_3)))
        self.label_el_4_seq_01.setText(str("{0:.3f}".format(the_program.dc_4)))
        self.label_el_5_seq_01.setText(str("{0:.3f}".format(the_program.dc_5)))
        self.label_el_6_seq_01.setText(str("{0:.3f}".format(the_program.dc_6)))
        self.label_el_7_seq_01.setText(str("{0:.3f}".format(the_program.dc_7)))
        self.label_el_8_seq_01.setText(str("{0:.3f}".format(the_program.dc_8)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


        #~~ the rf electrode plots ~~~~~~~~~~~~~#        
        self.label_rf_frequ_seq_01.setText(str("{0:.2f}".format(the_program.rf_frequency*(1/1000000))))
        self.label_rf_ampl_seq_01.setText(str("{0:.2f}".format(the_program.rf_osc_rms*1.414)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        #~~ the be creation monitoring ~~~~~~~~~#        
        self.label_oven_i_seq_01.setText(str("{0:.2f}".format(the_program.oven_current)))
        self.label_e_gun_i_fil_seq_01.setText(str("{0:.2f}".format(the_program.egun_current_filament)))
        self.label_e_gun_u_fil_seq_01.setText(str("{0:.0f}".format(the_program.egun_voltage_filament)))
        self.label_e_gun_i_weh_seq_01.setText(str("{0:.0f}".format(the_program.egun_voltage_wehnelt)))
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        
        self.textBrowser_trap_voltages_seq_01.setText(str(the_program.load_trap_voltages_times_seq_01))      
        
        
        #~~ the sequence plots ~~~~~~~~~~~~#
        dur = the_program.load_be_creation_seq_01[0]+the_program.load_be_creation_seq_01[1]
        
        x_values_be_creation_seq_01 = [0,the_program.load_be_creation_time_seq_01,the_program.load_be_creation_time_seq_01+dur]
        y_values_be_creation_seq_01 = [0,1]

        if the_program.load_trap_voltages_times_seq_01[-1] != 0:
            self.plot_be_creation_seq_01.setRange(xRange=(0,the_program.load_trap_voltages_times_seq_01[-1]))
            self.plot_piezo_seq_01.setRange(xRange=(0,the_program.load_trap_voltages_times_seq_01[-1]))
            self.plot_aom_seq_01.setRange(xRange=(0,the_program.load_trap_voltages_times_seq_01[-1]))
            self.plot_pic_seq_01.setRange(xRange=(0,the_program.load_trap_voltages_times_seq_01[-1]))
            
        else:
            pass
        
        
        self.plotted_be_creation_seq_01 = self.plot_be_creation_seq_01.plot(x_values_be_creation_seq_01,y_values_be_creation_seq_01, stepMode=True, fillLevel=0, brush=brush_red, name = 'seq 01 Be creation', clear = True)

        self.plotted_voltages_seq_01_dc_endcaps2 = self.plot_voltages_seq_01_dc_endcaps.plot(the_program.load_trap_voltages_seq_01_for_plot[1][0],the_program.load_trap_voltages_seq_01_for_plot[1][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt endcaps 2', clear = True)
        self.plotted_voltages_seq_01_dc_endcaps4 = self.plot_voltages_seq_01_dc_endcaps.plot(the_program.load_trap_voltages_seq_01_for_plot[3][0],the_program.load_trap_voltages_seq_01_for_plot[3][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt endcaps 4')
        self.plotted_voltages_seq_01_dc_endcaps5 = self.plot_voltages_seq_01_dc_endcaps.plot(the_program.load_trap_voltages_seq_01_for_plot[4][0],the_program.load_trap_voltages_seq_01_for_plot[4][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt endcaps 5')
        self.plotted_voltages_seq_01_dc_endcaps7 = self.plot_voltages_seq_01_dc_endcaps.plot(the_program.load_trap_voltages_seq_01_for_plot[6][0],the_program.load_trap_voltages_seq_01_for_plot[6][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt endcaps 7')
            
        self.plotted_voltages_seq_01_dc_center1 = self.plot_voltages_seq_01_dc_center.plot(the_program.load_trap_voltages_seq_01_for_plot[0][0],the_program.load_trap_voltages_seq_01_for_plot[0][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt center 1', clear = True)
        self.plotted_voltages_seq_01_dc_center3 = self.plot_voltages_seq_01_dc_center.plot(the_program.load_trap_voltages_seq_01_for_plot[2][0],the_program.load_trap_voltages_seq_01_for_plot[2][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt center 3')
        self.plotted_voltages_seq_01_dc_center6 = self.plot_voltages_seq_01_dc_center.plot(the_program.load_trap_voltages_seq_01_for_plot[5][0],the_program.load_trap_voltages_seq_01_for_plot[5][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt center 6')
        self.plotted_voltages_seq_01_dc_center8 = self.plot_voltages_seq_01_dc_center.plot(the_program.load_trap_voltages_seq_01_for_plot[7][0],the_program.load_trap_voltages_seq_01_for_plot[7][1], pen=bluePen, symbol='o', symbolBrush = brush_blue, name = 'seq 01 volt center 8')
        
        self.plotted_voltages_seq_01_rf_frequency = self.plot_voltages_seq_01_rf_frequency.plot(the_program.load_trap_voltages_seq_01_for_plot[9][0],the_program.load_trap_voltages_seq_01_for_plot[9][1], pen=yellowPen, symbol='o', symbolBrush = brush_yellow, name = 'seq 01 rf frequency', clear = True)
        
        self.plotted_voltages_seq_01_fr_amplitude = self.plot_voltages_seq_01_fr_amplitude.plot(the_program.load_trap_voltages_seq_01_for_plot[8][0],the_program.load_trap_voltages_seq_01_for_plot[8][1], pen=yellowPen, symbol='o', symbolBrush = brush_yellow, name = 'seq 01 rf amplitude', clear = True)
        
        self.plotted_piezo_seq_01 = self.plot_piezo_seq_01.plot(the_program.piezo_controller_list_times_seq_01, the_program.piezo_controller_list_seq_01,pen=redPen, symbol='o', symbolBrush = brush_red, name = 'seq 01 piezo', clear = True)
        
        self.plotted_aom_seq_01 = self.plot_aom_seq_01.plot(the_program.aom_list_times_seq_01, the_program.aom_list_seq_01,pen=redPen, symbol='o', symbolBrush = brush_red, name = 'seq 01 aom', clear = True)
 
        helper = []
        for i in range(len(the_program.pic_list_times_seq_01)):
            helper.append(int(0))
        
        if len(helper) > 0:
            self.plotted_pic_seq_01 = self.plot_pic_seq_01.plot(the_program.pic_list_times_seq_01, helper, symbol='s', name = 'seq 01 pic', clear = True)


        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#       
        
        
        
        
        
        
        
        
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
        


    #~~ not in the function above to control the timer for the update better ~~~~~~~~~~~~~~~~~~~~~~~~~~# 
    def timer_cam_pic_updates(self):
        self.plotted_cam = self.plot_cam.setImage(np.array(the_program.camera.data).reshape(the_program.camera.image_width, the_program.camera.image_height),autoRange=True, autoLevels=True, levels=None, axes=None, xvals=None, pos=None, scale=None, transform=None, autoHistogramRange=True)       
    #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#        










########################################################################################################
########################################################################################################
########################################################################################################
################                                                             ###########################
################        STARTING THE MAIN LOOP                               ###########################
################                                                             ###########################
########################################################################################################
########################################################################################################
########################################################################################################



if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    # create instance of parameters 
    the_program = c_program()
        
    # set up window   
    dialog_sequ = QtWidgets.QMainWindow()
    prog_sequ = window(dialog_sequ,the_program)    
    dialog_sequ.show()

#    # start permanent background jobs move to program!
#    scheduler.add_job(start_email_bot, 'interval', minutes=1, id='email_id', args = [the_program])

    
    sys.exit(app.exec_())
    
    

########################################################################################################
########################################################################################################
########################################################################################################
################                                                             ###########################
################        END OF PROGRAM                                       ###########################
################                                                             ###########################
########################################################################################################
########################################################################################################
########################################################################################################