import noCase as nc
import random

blue = ("MAG-7 | Foresight", "SCAR-20 | Poultrygeist", "Sawed-Off | Spirit Board", "P2000 | Lifted Spirits", "MP5-SD | Necro Jr.", "MAC-10 | Ensnared", "Five-SeveN | Scrawl")
purple = ("XM1014 | Zombie Offensive", "G3SG1 | Dream Glade", "PP-Bizon | Space Cat", "USP-S | Ticket to Hell", "M4A1-S | Night Terror")
pink = ("MP7 | Abyssal Apparition", "Dual Berettas | Melondrama", "FAMAS | Rapid Eye Movement")
red = ("MP9 | Starlight Protector", "AK-47 | Nightwish")
goldknife = ("Bowie Knife | ", "Butterfly Knife | ", "Falchion Knife | ", "Huntsman Knife | ", "Shadow Daggers | ")
goldpattern = ("Gamma Doppler", "Lore", "Bright Water", "Autotronic", "Freehand", "Black Laminate")

def rollSkin():
    res = ""
    rarity = nc.rollRarity()

    if rarity == "Blue":
        roll = random.randint(0, len(blue)-1)
        res = blue[roll]
    elif rarity == "Purple":
        roll = random.randint(0, len(purple)-1)
        res = purple[roll]
    elif rarity == "Pink":
        roll = random.randint(0, len(pink)-1)
        res = pink[roll]
    elif rarity == "Red":
        roll = random.randint(0, len(red)-1)
        res = red[roll]    
    elif rarity == "Gold":
        roll = random.randint(0, len(goldknife)-1)
        res = goldknife[roll]
        pat = random.randint(0, len(goldpattern)-1)
        res += goldpattern[pat]

    return res

def raritySkin(rarity):
    res = ""

    if rarity == "Blue":
        roll = random.randint(0, len(blue)-1)
        res = blue[roll]
    elif rarity == "Purple":
        roll = random.randint(0, len(purple)-1)
        res = purple[roll]
    elif rarity == "Pink":
        roll = random.randint(0, len(pink)-1)
        res = pink[roll]
    elif rarity == "Red":
        roll = random.randint(0, len(red)-1)
        res = red[roll]
    elif rarity == "Gold":
        roll = random.randint(0, len(goldknife)-1)
        res = goldknife[roll]
        pat = random.randint(0,len(goldpattern)-1)
        res += goldpattern[pat]

    return res

def rollMultiple():
    while True:
            nrOfRolls = input("How many skins would you like to open? ")

            if nrOfRolls.isdigit() and int(nrOfRolls) > 0:
                nrOfRolls = int(nrOfRolls)
                break
            else:
                print("Please input a number thats bigger than 0!")

    stats = {"Blue":0,"Purple":0,"Pink":0,"Red":0,"Gold":0}

    for i in range(nrOfRolls):
        rarity = nc.rollRarity()
        wear = nc.rollWear()
        print(raritySkin(rarity)+ " " + wear)
        stats = nc.rarityStats(rarity, stats)

    print("Your statistics look like this:")
    print(stats)

def run():
    while True:
        simType = input("Would you like to roll single skin each time (S) or simulate opening multiple skins (M)? (Type S or M) ")

        if simType.upper() == 'S':
            print('')
            print("Single it is!")
            print('')
            print(rollSkin()+ " " + nc.rollWear())
            nrOfRolls = 1
            while True:
                print('')
                repeat = input("Again? (Y/N) ")
                print('')
                if repeat.upper() == 'Y':
                    nrOfRolls += 1
                    print("(Roll number: " + str(nrOfRolls) + ")")
                    print(rollSkin()+ " " + nc.rollWear())
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
            
            rollMultiple()

            while True:
                print('')
                repeat = input("Again? (Y/N) ")
                print('')
                if repeat.upper() == 'Y':
                    rollMultiple()
                elif repeat.upper() == 'N':
                    print("Okay, bye!")
                    break
                else:
                    print("Write Y (Yes) or N (No) ")
            break
        else:
            print("Please choose a valid option")