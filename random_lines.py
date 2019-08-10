#Awesome Random Lines using Python
#Made by hitch_hicker and @pure.python

from turtle import *
from random import randint
from colorsys import hsv_to_rgb

print("""\033[1m\033[91m 
        _   _ _ _       _       _   _ _      _
       | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
       | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
       |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
       |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

a=int(input("""
         \033[42m\033[1;30m===================Random Lines===================\033[0;m
      \033[0;m
      >> Press 0 to START : """))


def main():

    step = 30                   #length of each step
    nsteps = 2000                  #number of steps
    hinc = 1.0/nsteps           #hue increment
    width(2)                       #width pf line

    (w,h)=screensize()          #boundaries of walk
    speed(0)
    colormode(5.0)              #colors 0:1 instead of 0:255
    bgcolor('black')                 #black background
    hue=0.0                     #hue means color

    for i in range(nsteps):
        setheading(randint(0,359))
        color(hsv_to_rgb(hue,1.0,1.0))          #pen color in RGB
        hue+=hinc                           #change color
        forward(step)               #step along
        (x,y)=pos()                         #where are we
        if abs(x)>w or abs(y)>h:                    #if at boundry
            backward(step)          #step back

if(a==0):
    main()

