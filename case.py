import noCase as nc
import random

class Case():
    def __init__(self, blues, purples, pinks, reds, knifes, kpatterns):
        self.blue = blues
        self.purple = purples
        self.pink = pinks
        self.red = reds
        self.goldknife = knifes 
        self.goldpattern =  kpatterns

    def rollWear(self):
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

    def rollSkin(self):
        res = ""
        rarity = nc.rollRarity()

        if (random.randint(1,10) == 1):
            res += "StatTrak™ "

        if rarity == "Blue":
            res += self.blue[random.randint(0, len(self.blue)-1)]
        elif rarity == "Purple":
            res += self.purple[random.randint(0, len(self.purple)-1)]
        elif rarity == "Pink":
            res += self.pink[random.randint(0, len(self.pink)-1)]
        elif rarity == "Red":
            res += self.red[random.randint(0, len(self.red)-1)]    
        elif rarity == "Gold":
            res += self.goldknife[random.randint(0, len(self.goldknife)-1)]
            res += self.goldpattern[random.randint(0, len(self.goldpattern)-1)]

        return res

    def raritySkin(self, rarity):
        res = ""

        if rarity == "Blue":
            roll = random.randint(0, len(self.blue)-1)
            res = self.blue[roll]
        elif rarity == "Purple":
            roll = random.randint(0, len(self.purple)-1)
            res = self.purple[roll]
        elif rarity == "Pink":
            roll = random.randint(0, len(self.pink)-1)
            res = self.pink[roll]
        elif rarity == "Red":
            roll = random.randint(0, len(self.red)-1)
            res = self.red[roll]
        elif rarity == "Gold":
            roll = random.randint(0, len(self.goldknife)-1)
            res = self.goldknife[roll]
            pat = random.randint(0,len(self.goldpattern)-1)
            res += self.goldpattern[pat]

        return res
    
    def rollMultiple(self):
        while True:
            nrOfRolls = input("How many skins would you like to open? ")

            if nrOfRolls.isdigit() and int(nrOfRolls) > 0:
                nrOfRolls = int(nrOfRolls)
                break
            else:
                print("Please input a number thats bigger than 0!")

        stats = {"Blue":0,"Purple":0,"Pink":0,"Red":0,"Gold":0}

        for i in range(nrOfRolls):
            st = ""
            if random.randint(1,10) == 1:
                st = "StatTrak™ "
            rarity = nc.rollRarity()
            wear = nc.rollWear()
            skin = st + ' ' + self.raritySkin(rarity) + " " + wear
            print(skin.strip())
            stats = nc.rarityStats(rarity, stats)

        print('')
        print("Your statistics look like this:")
        print(stats)

    def run(self):
        while True:
            simType = input("Would you like to roll single skin each time (S) or simulate opening multiple skins (M)? (Type S or M) ")

            if simType.upper() == 'S':
                print('')
                print("Single it is!")
                print('')
                print(self.rollSkin()+ " " + self.rollWear())
                nrOfRolls = 1
                while True:
                    print('')
                    repeat = input("Again? (Y/N) ")
                    print('')
                    if repeat.upper() == 'Y':
                        nrOfRolls += 1
                        print("(Roll number: " + str(nrOfRolls) + ")")
                        print(self.rollSkin()+ " " + self.rollWear())
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
                
                self.rollMultiple()

                while True:
                    print('')
                    repeat = input("Again? (Y/N) ")
                    print('')
                    if repeat.upper() == 'Y':
                        self.rollMultiple()
                    elif repeat.upper() == 'N':
                        print("Okay, bye!")
                        break
                    else:
                        print("Write Y (Yes) or N (No) ")
                break
            else:
                print("Please choose a valid option")