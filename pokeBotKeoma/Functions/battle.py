from time import sleep
import pyautogui
import os
from pynput import keyboard as keyboardL
from datetime import datetime
from imagesearch import *
from Functions.core import walk, skill, setThingsOK, getImageFolder
from Functions.heal import healPokeCenter


class Battle:
    attacksCharged = 0
    healAtPokeCenter = False
    specificPokemon = False
    command = ''
    pokemonToHunt = ''
    quantityAttacksToHeal = 0


def setIfHealAtPokecenter(heal):
    Battle.healAtPokeCenter = heal


def getIfHealAtPokecenter():
    return Battle.healAtPokeCenter


def setIfFindASpecificPokemon(findSpecific):
    Battle.specificPokemon = findSpecific


def getIfFindASpecificPokemon():
    return Battle.specificPokemon


def setPokemonToHunt(pokemon):
    Battle.pokemonToHunt = pokemon


def getPokemonToHunt():
    return Battle.pokemonToHunt


def setQuantityAttacksToHeal(quantity):
    Battle.quantityAttacksToHeal = quantity


def getQuantityAttacksToHeal():
    return Battle.quantityAttacksToHeal


def setAttacksCharged(attack):
    Battle.attacksCharged = attack


def getAttacksCharged():
    return Battle.attacksCharged


def setCommand(comm):
    Battle.command = comm


def getCommand():
    return Battle.command


def hunt():
    while(True):
        cancelLearning()
        print(getAttacksCharged())
        if (getAttacksCharged() >= getQuantityAttacksToHeal()):
                    if (getIfHealAtPokecenter):
                        healPokeCenter()
                        setAttacksCharged(0)
        for x in range(0, 4):
            walk("a", 3)
            walk("d", 2)
        verifyBattle()
        print("hunting!")



def verifyBattle():
    img = imagesearch(getImageFolder() + 'battleFound.png', precision=0.8)
    if img is not None:
        print("battleFound!")
        sleep(1)
        img = imagesearch_numLoop(getImageFolder() + 'fight.png', 1, 5, precision=0.8)
        if img is not None:
            if 'fight' in Battle.command:
                battle(Battle.command)


def battle(verifySituationCommand):
    while True:
        if imgClick(getImageFolder() + 'fight.png', 1, 1):
            sleep(0.4)
            if (getIfFindASpecificPokemon() == False):
                if '1' in verifySituationCommand:
                    skill(random.randint(1,4))
            else:
                if imgClick(getImageFolder() + getPokemonToHunt() +'.png', 1, 1):
                    skill(random.randint(1,4))
                else:
                    run()
            sleep(3)
        setAttacksCharged(getAttacksCharged() + 1)

        img = imagesearch(getImageFolder() + 'battleFound.png', precision=0.8)
        if img is None:
            setThingsOK(True)
            return


def verifyFaint():
    if imgClick(getImageFolder() + 'faited.png', 1, 1):
        imgClick(getImageFolder() + 'pokemonChange.png', 1, 5)
        sleep(1)
        skill('2')


def run():
    imgClick(getImageFolder() + 'run.png', 1, 5)
    sleep(2)


def cancelEvolving():
    if imgClick(getImageFolder() + 'evolving.png', 1, 1):
        imgClick(getImageFolder() + 'noEvolve.png', 1, 5)


def cancelLearning():
    if imgClick(getImageFolder() + 'learn.png', 1, 1):
        imgClick(getImageFolder() + 'doNotLearn.png', 1, 5)
        imgClick(getImageFolder() + 'confirmNotLearning.png', 1, 5)


