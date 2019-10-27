from time import sleep
import pyautogui
import os
from pynput import keyboard as keyboardL
from datetime import datetime
from imagesearch import *
from Functions.core import walk, skill
from Functions.heal import healPokeCenter


class Battle:
    imageFolder = os.getcwd() + r"\\imagens\\"
    attacksCharged = 0
    thingsOK = True
    healAtPokeCenter = False
    specificPokemon = False
    command = 'fight_1'
    pokemonToHunt = ''
    quantityAttacksToHeal = 0


def setIfHealAtPokecenter(heal):
    Battle.healAtPokeCenter = heal


def setIfFindASpecificPokemon(findSpecific):
    Battle.specificPokemon = findSpecific


def setPokemonToHunt(pokemon):
    Battle.pokemonToHunt = pokemon


def setQuantityAttacksToHeal(quantity):
    Battle.quantityAttacksToHeal = quantity


def hunt():
    while(True):
        cancelLearning()
        print(Battle.attacksCharged)
        if (Battle.attacksCharged >= Battle.quantityAttacksToHeal):
                    if (Battle.healAtPokeCenter):
                        healPokeCenter()
                        Battle.attacksCharged = 0
        for x in range(0, 4):
            walk("a", 3)
            walk("d", 2)
        verifyBattle()
        print("hunting!")



def verifyBattle():
    img = imagesearch(Battle.imageFolder+'battleFound.png', precision=0.8)
    if img is not None:
        print("battleFound!")
        sleep(1)
        img = imagesearch_numLoop(Battle.imageFolder + 'fight.png', 1, 5, precision=0.8)
        if img is not None:
            if 'fight' in Battle.command:
                battle(Battle.command)


def battle(verifySituationCommand):
    while True:
        if imgClick(Battle.imageFolder + 'fight.png', 1, 1):
            sleep(0.4)
            if (Battle.specificPokemon == False):
                if '1' in verifySituationCommand:
                    skill(random.randint(1,4))
            else:
                if imgClick(Battle.imageFolder + Battle.pokemonToHunt +'.png', 1, 1):
                    skill(random.randint(1,4))
                else:
                    run()
            sleep(3)
        Battle.attacksCharged = Battle.attacksCharged + 1

        img = imagesearch(Battle.imageFolder+'battleFound.png', precision=0.8)
        if img is None:
            Battle.thingsOK = True
            return


def verifyFaint():
    if imgClick(Battle.imageFolder + 'faited.png', 1, 1):
        imgClick(Battle.imageFolder + 'pokemonChange.png', 1, 5)
        sleep(1)
        skill('2')


def run():
    imgClick(Battle.imageFolder + 'run.png', 1, 5)
    sleep(2)


def cancelEvolving():
    if imgClick(Battle.imageFolder + 'evolving.png', 1, 1):
        imgClick(Battle.imageFolder + 'noEvolve.png', 1, 5)


def cancelLearning():
    if imgClick(Battle.imageFolder + 'learn.png', 1, 1):
        imgClick(Battle.imageFolder + 'doNotLearn.png', 1, 5)
        imgClick(Battle.imageFolder + 'confirmNotLearning.png', 1, 5)


