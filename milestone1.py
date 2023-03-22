# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:25:49 2022

@author: Carol
"""

import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np

t = np. linspace(0 , 6, 12*1024)

f = [392.00, 440.00,  392.00,349.23,329.63,349.23,392.00,293.66,329.63,349.23,329.63,349.23,392.00]
ti =[0,   0.4, 0.8, 1.2, 1.6, 2,   2.4, 3.1, 3.5, 3.9, 4.6, 5,   5.4]
Ti =[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6, 0.3, 0.3, 0.6]
x=0
i=0
for i in range(len(f)) :
    x+= np.sin( 2*np.pi*f[i]*t )*( t>ti[i] )*( t<(Ti[i]+ti[i]) )
    i+=1
    
plt.plot(t, x)
sd.play(x, 2*1024)   
        
        