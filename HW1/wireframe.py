#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 14:50:39 2019

@author: sedwards
"""
###########
#This module defines function makewire for wireframe plot
# call module in script with import wireframe
# call function in script with wireframe.makewire(im)
#

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
                    


def makewire(image):
    
    r,c = np.shape(image)    # number rows r and columns c in im
    x = np.linspace(0,r,r)    # make 1D array of length r with r elements
    y = np.linspace(0,c,c)    # make 1D array of length c with c elements
    XX,YY = np.meshgrid(x,y)   # make two 2-d arrays of r x c, c x r

    fig = plt.figure(figsize=(12,6))             #identify plot as fig, specify size
    ax = fig.add_subplot(1,1,1,projection='3d')  # enable 3D plot
    wirey = ax.plot_wireframe(XX,YY,image, rstride=1, cstride=1)
    
    ax.set_zlabel("Counts)", size=15)
    ax.set_xlabel(" Pixel",size=15)
    ax.set_ylabel(" Pixel",size=15)
    return(wirey)









