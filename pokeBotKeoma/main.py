from time import sleep
import threading
from Functions.core import walk, keyboardListener, timePrinter, exitOnError
from Functions.battle import hunt, setIfHealAtPokecenter, setIfFindASpecificPokemon, setPokemonToHunt, setQuantityAttacksToHeal
from Functions.heal import setPlaceForHeal


def main():
    setIfHealAtPokecenter(True)
    setPlaceForHeal('cinnabar_pokecenter')
    setQuantityAttacksToHeal(20)
    setIfFindASpecificPokemon(False)
    setPokemonToHunt('')


    t = []
    t.append(threading.Thread(target=keyboardListener, args=()))
    t.append(threading.Thread(target=hunt, args=()))
    t.append(threading.Thread(target=exitOnError, args=()))
    t.append(threading.Thread(target=timePrinter, args=()))

    sleep(1)
    for oneT in t:
        oneT.start()

main()