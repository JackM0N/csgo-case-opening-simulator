import case as c
import random

blue = ("G3SG1 | Keeping Tabs", "MP7 | Guerrilla", "Dual Berettas | Tread", "AUG | Plague", "PP-Bizon | Lumen", "XM1014 | Watchdog", "USP-S | Black Lotus")
purple = ("MAG-7 | BI83 Spectrum", "Five-SeveN | Boost Protocol", "MP9 | Mount Fuji", "FAMAS | ZX Spectron", "M4A4 | Spider Lily")
pink = ("MAC-10 | Toybox", "SSG 08 | Turbo Peek", "Glock-18 | Snack Attack")
red = ("AK-47 | Leet Museo", "Desert Eagle | Ocean Drive")
goldknife = ("Bowie Knife | ", "Butterfly Knife | ", "Falchion Knife | ", "Huntsman Knife | ", "Shadow Daggers | ")
goldpattern = ("Gamma Doppler", "Lore", "Bright Water", "Autotronic", "Freehand", "Black Laminate")

def run():
    case = c.Case(blue, purple, pink, red, goldknife, goldpattern)

    while True:
        simType = input("Would you like to roll single skin each time (S) or simulate opening multiple skins (M)? (Type S or M) ")

        if simType.upper() == 'S':
            print('')
            print("Single it is!")
            print('')
            print(case.rollSkin()+ " " + case.rollWear())
            nrOfRolls = 1
            while True:
                print('')
                repeat = input("Again? (Y/N) ")
                print('')
                if repeat.upper() == 'Y':
                    nrOfRolls += 1
                    print("(Roll number: " + str(nrOfRolls) + ")")
                    print(case.rollSkin()+ " " + case.rollWear())
                elif repeat.upper() == 'N':
                    print("Okay, bye!")
                    break
                else:
                    print("Write Y (Yes) or N (No) ")
            break


        elif simType.upper() == 'M':
            print('')
            print("Multiple it is!")
            print('')
            
            case.rollMultiple()

            while True:
                print('')
                repeat = input("Again? (Y/N) ")
                print('')
                if repeat.upper() == 'Y':
                    case.rollMultiple()
                elif repeat.upper() == 'N':
                    print("Okay, bye!")
                    break
                else:
                    print("Write Y (Yes) or N (No) ")
            break
        else:
            print("Please choose a valid option")