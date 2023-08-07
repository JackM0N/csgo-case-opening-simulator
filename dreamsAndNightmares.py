import case as c
import random

blue = ("MAG-7 | Foresight", "SCAR-20 | Poultrygeist", "Sawed-Off | Spirit Board", "P2000 | Lifted Spirits", "MP5-SD | Necro Jr.", "MAC-10 | Ensnared", "Five-SeveN | Scrawl")
purple = ("XM1014 | Zombie Offensive", "G3SG1 | Dream Glade", "PP-Bizon | Space Cat", "USP-S | Ticket to Hell", "M4A1-S | Night Terror")
pink = ("MP7 | Abyssal Apparition", "Dual Berettas | Melondrama", "FAMAS | Rapid Eye Movement")
red = ("MP9 | Starlight Protector", "AK-47 | Nightwish")
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