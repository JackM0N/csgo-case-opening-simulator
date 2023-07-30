import random

def rollRarity():
    res = ""
    roll = random.randint(0, 10000)
    if roll <= 7992:
        res = "Blue"
    elif roll <= 9590:
        res = "Purple"
    elif roll <= 9910:
        res = "Pink"
    elif roll <= 9974:
        res = "Red"
    else:
        res = "Gold"
    
    return res

def rollWear():
    res = ""
    roll = random.randint(0, 100)
    if 0 <= roll <= 7 :
        res = "(Factory New)"
    elif 7 < roll <= 15:
        res = "(Minimal Wear)"
    elif 15 < roll <= 38:
        res = "(Field Tested)"
    elif 38 < roll <= 45:
        res = "(Well Worn)"
    else:
        res = "(Battle-Scarred)"
    
    return res
        
def rarityStats(skin, stats):
#    stats = {"Blue":0,"Purple":0,"Pink":0,"Red":0,"Gold":0}
    if skin == "Blue":
        stats["Blue"] += 1
    elif skin == "Purple":
        stats["Purple"] += 1
    elif skin == "Pink":
        stats["Pink"] += 1
    elif skin == "Red":
        stats["Red"] += 1
    elif skin == "Gold":
        stats["Gold"] += 1

    return stats

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
        rarity = rollRarity()
        wear = rollWear()
        print(rarity+ " " + wear)
        stats = rarityStats(rarity, stats)

    print("Your statistics look like this:")
    print(stats)


while True:
    simType = input("Would you like to roll single skin each time (S) or simulate opening multiple skins (M)? (Type S or M) ")

    if simType.upper() == 'S':
        print("Single it is!")
        print('')
        print(rollRarity()+ " " + rollWear())
        nrOfRolls = 1
        while True:
            print('')
            repeat = input("Again? (Y/N) ")
            print('')
            if repeat.upper() == 'Y':
                nrOfRolls += 1
                print("(Roll number: " + str(nrOfRolls) + ")")
                print(rollRarity()+ " " + rollWear())
            elif repeat.upper() == 'N':
                print("Okay, bye!")
                break
            else:
                print("Write Y (Yes) or N (No) ")
        break


    elif simType.upper() == 'M':
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
