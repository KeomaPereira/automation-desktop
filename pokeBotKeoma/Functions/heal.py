from time import sleep
import pyautogui
import os
from pynput import keyboard as keyboardL
from datetime import datetime
from imagesearch import *
from Functions.core import walk, getImageFolder


class Heal:
    pokeCenter = ''


def setPlaceForHeal(poke):
    Heal.pokeCenter = poke


def getPlaceForHeal():
    return Heal.pokeCenter


def healPokeCenter():
    if getPlaceForHeal() == 'cinnabar_pokecenter':
        sleep(4)
        walk('a', 8)
        walk('d', 1)
        sleep(1)
        walk('d', 1)
        sleep(1)
        walk('s', 1)
        sleep(3)
        walk('a', 2)
        walk('s', 18)
        walk('d', 8)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('w', 6)
        sleep(1)
        walk('w', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('w', 10)
        sleep(1)
        nurseTalk()
        walk('s', 12)
        walk('d', 5)
        sleep(3)
        walk("s", 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        sleep(1)
        walk('a', 1)
        walk("w", 25)
        sleep(1)
        walk('d', 1)
        sleep(1)
        walk('d', 1)
        sleep(1)
        walk('d', 1)
        sleep(1)
        walk('w', 1)
    if getPlaceForHeal() == 'lavander_tower':
        print('Healing')
        sleep(2)
        walk('w', 10)
        walk('d', 4)
        nurseTalk()
        walk('a', 1)


def nurseTalk():
    i = 0
    while not imgClick(getImageFolder() + 'yesPlease.png', 1, 1):
        i = i + 1
        pyautogui.typewrite(' ')
        sleep(0.5)
        if i > 5:
            return
    sleep(2)
    for i in range(0, 3):
        pyautogui.typewrite(' ')
        sleep(2)
        messageWindow = imagesearch(getImageFolder() + 'messageWindow.png', precision=0.8)
        if messageWindow is None:
            return


def healWithPotion(text):
    sleep(1)
    imgClick(getImageFolder() + 'mochila.png', 1, 1)
    sleep(1)
    imgClick(getImageFolder() + 'superPocao.png', 1, 1)
    sleep(1)
    if (text == 'GOLBAT'):
        imgClick(getImageFolder() + 'golbat.png', 1, 1)
    if (text == 'NIDOKING'):
        imgClick(getImageFolder() + 'nido.png', 1, 1)
    sleep(2)


