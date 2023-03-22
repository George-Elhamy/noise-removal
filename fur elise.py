# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:16:48 2022

@author: Carol
"""

import matplotlib.pyplot as plt
import sounddevice as sd
import numpy as np


t = np. linspace(0 , 3, 12*1024)

# r --> RIGHT HAND ,  l --> LEFT HAND

#BAR1
r1=np.sin(2*np.pi*659.25*t)*(t<0.13)*(t>0)
r2=np.sin(2*np.pi*622.25*t)*(t<0.26)*(t>0.13)




#BAR2
r3=np.sin(2*np.pi*659.25*t)*(t<0.39)*(t>0.26)
r4=np.sin(2*np.pi*622.25*t)*(t<0.52)*(t>0.39)
r5=np.sin(2*np.pi*659.25*t)*(t<0.65)*(t>0.52)
r6=np.sin(2*np.pi*493.88*t)*(t<0.78)*(t>0.65)
r7=np.sin(2*np.pi*587.33*t)*(t<0.91)*(t>0.78)
r8=np.sin(2*np.pi*523.25*t)*(t<1.04)*(t>0.91)




#BAR3
#RIGHT HAND
r9=np.sin(2*np.pi*440.00*t)*(t<1.3)*(t>1.04)
r10=np.sin(2*np.pi*261.63*t)*(t<1.56)*(t>1.43)
r11=np.sin(2*np.pi*329.63*t)*(t<1.69)*(t>1.56)
r12=np.sin(2*np.pi*440.00*t)*(t<1.82)*(t>1.69)
#LEFT HAND
l1=np.sin(2*np.pi*110.00*t)*(t<1.17)*(t>1.04)
l2=np.sin(2*np.pi*164.81*t)*(t<1.3)*(t>1.17)
l3=np.sin(2*np.pi*220.00*t)*(t<1.43)*(t>1.3)

#BAR4
#RIGHT HAND
r13=np.sin(2*np.pi*493.88*t)*(t<2.08)*(t>1.82)
r14=np.sin(2*np.pi*329.63*t)*(t<2.34)*(t>2.21)
r15=np.sin(2*np.pi*415.30*t)*(t<2.47)*(t>2.34)
r16=np.sin(2*np.pi*493.88*t)*(t<2.6)*(t>2.47)
#LEFT HAND
l4=np.sin(2*np.pi*82.41*t)*(t<1.95)*(t>1.82)
l5=np.sin(2*np.pi*164.81*t)*(t<2.08)*(t>1.95)
l6=np.sin(2*np.pi*207.65*t)*(t<2.21)*(t>2.08)


#BAR5
#RIGHT HAND
r17=np.sin(2*np.pi*523.25*t)*(t<2.86)*(t>2.6)

#LEFT HAND
l7=np.sin(2*np.pi*110.00*t)*(t<2.73)*(t>2.6)
l8=np.sin(2*np.pi*164.81*t)*(t<2.86)*(t>2.73)
l9=np.sin(2*np.pi*220.00*t)*(t<2.99)*(t>2.86)

r=r1+r2+r3+r4+r5+r6+r7+r8+r9+r10+r11+r12+r13+r14+r15+r16+r17
l=l1+l2+l3+l4+l5+l6+l7+l8+l9
x=l+r

plt.plot(t, x)

sd.play(x, 4*1024)