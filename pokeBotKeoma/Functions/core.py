from time import sleep
import pyautogui
import os
from pynput import keyboard as keyboardL
from datetime import datetime



class Core:
    imageFolder = os.getcwd() + r"\\imagens\\"
    mouseX = 0
    mouseY = 0
    thingsOK = True
    exiting = False


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
    Core.mouseX, Core.mouseY = pyautogui.position()
    print("mouseX :"+str(Core.mouseX))
    print("mouseY :"+str(Core.mouseY))


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
        Core.thingsOK = False
        sleep(300)
        if not Core.thingsOK:
            print("EXITING BY INACTIVITY")
            exit('exitOnError')
        elif Core.exiting:
            exit('exitOnError')


def exit(called):
    Core.exiting = True
    print(called+' exiting!!!!!!!!!')
    Core.exit()


def skill(key):
    pyautogui.press(str(key))

