"""
My fun little python script to autoclick in cookie clicker
#Only functions on Windows right now
"""

from ctypes import windll, Structure, c_long, byref, wintypes
import keyboard
import time
import sys
from msvcrt import kbhit, getch

click = False
pressed = False
running = True
setx = 0
sety = 0

def getCursorPos():
    pt = wintypes.POINT()
    windll.user32.GetCursorPos(byref(pt))
    return pt

def keyboardInput(callback):
    global pressed
    global click
    global setx
    global sety
    if callback.event_type == 'down':
        if callback.name == 'home' and pressed == False:
            pressed = True

    if callback.event_type == 'up' and pressed == True:
        if(callback.name == 'home'):
            pressed = False
            setx = getCursorPos().x
            sety = getCursorPos().y
            click = not click



def handleMouse():

    windll.user32.SetCursorPos(setx, sety)
    windll.user32.mouse_event(0x0002, 0, 0, 0, 0)
    windll.user32.mouse_event(0x0004, 0, 0, 0, 0)


def milliTime():
    return int(round(time.time() * 1000))

def mainfun():
    global click
    global running

    print("\nInitializing AutoClicker...")

    clickIndex = 0
    timer = milliTime()
    keyboard.hook(keyboardInput)
    doClick = 0
    clickedSec = 0
    clickedLast = 0
    toggle = "OFF"
    print("AutoClicker Initialized!")
    print("\nPress HOME anywhere to toggle autoclicking, and press ESC in console window to exit autoclicker.\n")
    while running:
        if kbhit():
            key = ord(getch())
            if key == 27:
                running = False
        if click:
            if(doClick >= 30):
                doClick = 0
            if doClick == 0:
                handleMouse()
                clickedSec += 1
            doClick += 1
            toggle = "ON"
        else:
            toggle = "OFF"

        if(milliTime() - timer >= 1000):
            timer = milliTime()
            #print("\rClicks Last Second: " + str(clickedSec))
            clickedLast = clickedSec
            clickedSec = 0
        print("AutoClicker toggled: " + toggle + "  |  Clicks Last Second: " + str(clickedLast) + " ", end='              \r')
    if running == False:
        print("\n\nAutoClicker ending...")

if __name__ == "__main__":
    mainfun()
