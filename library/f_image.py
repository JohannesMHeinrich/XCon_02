# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 22:59:35 2016

@author: JohannesMHeinrich
"""

import matplotlib.pyplot as plt

from PIL import Image


def get_image(file_name):
  
    fig_01 = plt.figure()
    
    fig_01.patch.set_facecolor('white')
    fig_01.patch.set_alpha(0)
    
    ax = fig_01.add_subplot(111)
    
    ax.plot(range(10))
 
    ax.patch.set_alpha(0)
    
    ax.axis('off')
    
    plt.tight_layout(pad=0.01, w_pad=0.01, h_pad=0.01)
    
    
    img = Image.open(file_name)
    ax.imshow(img,zorder=0)

        
    return fig_01