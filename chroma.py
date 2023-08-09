import case as c

blue = ("SCAR-20 | Grotto", "XM1014 | Quicksilver", "M249 | System Lock", "Glock-18 | Catacombs", "MP9 | Deadly Poison")
purple = ("Dual Berettas | Urban Shock", "Sawed-Off | Serenity", "MAC-10 | Malachite", "Desert Eagle | Naga")
pink = ("P250 | Muertos", "M4A4 | 龍王 (Dragon King)", "AK-47 | Cartel")
red = ("AWP | Man-o'-war", "Galil AR | Chatterbox")
goldknife = ("Bayonet | ", "Flip Knife | ", "Gut Knife | ", "Karambit | ", "M9 Bayonet | ")
goldpattern = ("Marble Fade", "Tiger Tooth", "Doppler", "Damascus Steel", "Ultraviolet", "Rust Coat")

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