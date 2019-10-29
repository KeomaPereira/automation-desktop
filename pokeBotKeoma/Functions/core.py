from time import sleep
import pyautogui
import os
from pynput import keyboard as keyboardL
from datetime import datetime


class Core:
    mouseX = 0
    mouseY = 0
    thingsOK = True
    exiting = False
    imageFolder = ''


def setImageFolder(image):
    Core.imageFolder = image


def getImageFolder():
    return Core.imageFolder



def setMouseX(mouse):
    Core.mouseX = mouse


def getmouseX():
    return Core.mouseX


def setMouseY(mouse):
    Core.mouseY = mouse


def getmouseY():
    return Core.mouseY


def setThingsOK(things):
    Core.thingsOK = things


def getThingsOK():
    return Core.thingsOK


def setExiting(exiting):
    Core.exiting = exiting


def getExiting():
    return Core.exiting


def walk(key, times=1):
    if times == 1:
        pyautogui.typewrite(key)
    else:
        hold(key, times * 0.225)


def hold(key, holdTime=0.25):
    pyautogui.keyDown(key)
    sleep(holdTime)
    pyautogui.keyUp(key)


def on_press(key):
    try:
        k = key.char
        print('alphanumeric key {0} pressed'.format(key.char))
    except:
        return

    if k == 'p':
        im = pyautogui.screenshot()
        im.save('exit.png')
        exit('on_press')
    if k =='m':
        getMousePosition()


def getMousePosition():
    setMouseX(pyautogui.position())
    setMouseY(pyautogui.position())
    print("mouseX :"+str(getmouseX()))
    print("mouseY :"+str(getmouseY()))


def keyboardListener():
    try:
        with keyboardL.Listener(on_press=on_press) as listener:
            listener.join()
            listener.start()
    except:
        exit('keyboardListener')


def timePrinter():
    while True:
        print(datetime.now())
        sleep(10)
        if Core.exiting:
            exit('timePrinter')


def exitOnError():
    while True:
        setThingsOK(False)
        sleep(300)
        if not getThingsOK():
            print("EXITING BY INACTIVITY")
            exit('exitOnError')
        elif getExiting:
            exit('exitOnError')


def exit(called):
    Core.exiting = True
    print(called+' exiting!!!!!!!!!')


def skill(key):
    pyautogui.press(str(key))

