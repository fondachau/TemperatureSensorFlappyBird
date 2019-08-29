# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:41:14 2016

@author: Fonda Chau
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math

import serial

xsize=100
game="play on"  
print game 

# configure the serial port
ser = serial.Serial(
     port='COM9',
     baudrate=115200,
     parity=serial.PARITY_NONE,
     stopbits=serial.STOPBITS_TWO,
     bytesize=serial.EIGHTBITS
)
ser.isOpen()
def pause():
    programPause = raw_input("its over. you lose.")



xsize=100
   
def data_gen():
    t = data_gen.t
    while True:
       t+=1
       strin1 = ser.readline()
       strin2= ser.readline()
      #if strin>10 and strin2<10 and strin3>125 and strin3<125 and strin4>50 and strin4<120 and strin5>180 and strin5<210 and strin6>30 and string6<40:   
       val=strin1
       state=strin2
       print "val is"+val
       print "state is"+state
       yield t, val

def endgame(x):
    print "game over"
    print "your score was:", x
    print("if you would like to play again, reload the program")
    pause()    
def run(data):
    # update the data
    t,y = data
    if t>-1:
        
        xdata.append(t)
        ydata.append(y)
        s=int(y)        
        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
        if t>20:    
            if s>80 and ((t-20)%120>=0 and (t-20)%120<=20):
                endgame(t/40)
            elif s<20 and ((t-20)%120>=0 and (t-20)%120<=20):                         
                endgame(t/40)
            elif s>60 and  ((t-60)%120>=0 and (t-60)%120<=20):      
                endgame(t/40)
            elif s<30 and ((t-60)%120>=0 and (t-60)%120<=20):      
                endgame(t/40)
            elif s>70 and ((t-100)%120>=0 and (t-100)%120<=20):       
                endgame(t/40) 
            elif s<40 and ((t-100)%120>=0 and(t-100)%120<=20):        
                endgame(t/40)    
            elif t%40==0:
                score=t/40
                print score

        if t>50: # Scroll to the left.
            ax.set_xlim(t-50, t+50)
        line.set_data(xdata, ydata)
        if t%120==0:
            plt.plot([t+20, t+40], [80, 80])
            plt.plot([t+20, t+20], [80, 100])
            plt.plot([t+40, t+40], [20, -20])
            plt.plot([t+40, t+40], [80, 100])
            plt.plot([t+20, t+20], [20, -20])
            plt.plot([t+20, t+40], [20, 20])
            plt.plot([t+60, t+80], [60, 60])
            plt.plot([t+60, t+60], [60, 100])
            plt.plot([t+80, t+80], [30, -20])
            plt.plot([t+80, t+80], [60, 100])
            plt.plot([t+60, t+60], [30, -20])
            plt.plot([t+60, t+80], [30, 30])
            plt.plot([t+100,t+120], [70, 70])
            plt.plot([t+100, t+100], [70, 100])
            plt.plot([t+120, t+120], [40, -20])
            plt.plot([t+120, t+120], [70, 100])
            plt.plot([t+100, t+100], [40, -20])
            plt.plot([t+100,t+120], [40, 40])
    return line,

def on_close_figure(event):
    sys.exit(0)

data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(0, 100)
ax.set_xlim(0, xsize)
ax.set_xlabel('time(s)')
ax.set_ylabel('temperature(oC')
ax.set_title('temperature sensor')
ax.grid()
xdata, ydata = [], []

# Important: Although blit=True makes graphing faster, we need blit=False to prevent
# spurious lines to appear when resizing the stripchart.
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)
plt.show()
