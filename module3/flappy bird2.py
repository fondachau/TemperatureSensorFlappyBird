# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 09:31:09 2016

@author: Fonda Chau
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys, time, math


def pause():
    programPause = raw_input("if you would like to continue, press enter")


xsize=100
   
def data_gen():
    t = data_gen.t
    while True:
       t+=1
       val=40*math.sin(t*2.0*3.1415/100.0)+40
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
        if t>xsize: # Scroll to the left.
            ax.set_xlim(t-xsize, t)
        if t>20:    
            if y>=80 and ((t-20)%120>=0 and (t-20)%120<=20):
                endgame(t/40)
            elif y<=20 and ((t-20)%120>=0 and (t-20)%120<=20):       
                endgame(t/40)
            elif y>=60 and  ((t-60)%120>=0 and (t-60)%120<=20):      
                endgame(t/40)
            elif y<=00 and ((t-60)%120>=0 and (t-60)%120<=20):      
                endgame(t/40)
            elif y>=70 and ((t-100)%120>=0 and (t-100)%120<=20):       
                endgame(t/40) 
            elif y<=30 and ((t-100)%120>=0 and(t-100)%120<=20):        
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
            plt.plot([t+80, t+80], [0, -20])
            plt.plot([t+80, t+80], [60, 100])
            plt.plot([t+60, t+60], [0, -20])
            plt.plot([t+60, t+80], [0, 0])
            plt.plot([t+100,t+120], [70, 70])
            plt.plot([t+100, t+100], [70, 100])
            plt.plot([t+120, t+120], [30, -20])
            plt.plot([t+120, t+120], [70, 100])
            plt.plot([t+100, t+100], [30, -20])
            plt.plot([t+100,t+120], [30, 30])
    return line,


def on_close_figure(event):
    sys.exit(0)

data_gen.t = -1
fig = plt.figure()
fig.canvas.mpl_connect('close_event', on_close_figure)
ax = fig.add_subplot(111)
line, = ax.plot([], [], lw=2)
ax.set_ylim(-100, 100)
ax.set_xlim(0, xsize)
ax.grid()
xdata, ydata = [], []

# Important: Although blit=True makes graphing faster, we need blit=False to prevent
# spurious lines to appear when resizing the stripchart.
ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=100, repeat=False)
plt.show()
