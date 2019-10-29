from time import sleep
import threading
from Functions.core import walk, keyboardListener, timePrinter, exitOnError, setImageFolder
from Functions.battle import hunt, setIfHealAtPokecenter, setIfFindASpecificPokemon, setPokemonToHunt, \
    setQuantityAttacksToHeal, setCommand
from Functions.heal import setPlaceForHeal
import os


def main():
    setImageFolder(os.getcwd() + r"\\imagens\\")
    setCommand('fight_1')
    setIfHealAtPokecenter(True)
    setPlaceForHeal('cinnabar_pokecenter')
    setQuantityAttacksToHeal(200)
    setIfFindASpecificPokemon(True)
    setPokemonToHunt('krabby')


    t = []
    t.append(threading.Thread(target=keyboardListener, args=()))
    t.append(threading.Thread(target=hunt, args=()))
    t.append(threading.Thread(target=exitOnError, args=()))
    t.append(threading.Thread(target=timePrinter, args=()))

    sleep(1)
    for oneT in t:
        oneT.start()

main()