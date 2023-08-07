import case as c

blue = ("SG 553 | Ol' Rusty", "Negev | Ultralight", "P250 | Cassette", "P2000 | Gnarled", "P90 | Freight", "PP-Bizon | Runic", "SSG 08 | Mainframe 001")
purple = ("Galil AR | Connexion", "MP5-SD | Kitbash", "Tec-9 | Brother", "MAC-10 | Allure", "MAG-7 | Monster Call")
pink = ("XM1014 | Entombed", "M4A4 | Tooth Fairy", "Glock-18 | Vogue")
red = ("AK-47 | Legion of Anubis", "Desert Eagle | Printstream")
goldknife = ("Nomad Knife | ", "Paracord Knife | ", "Skeleton Knife | ", "Survival Knife | ")
goldpattern = ("Fade", "Slaughter", "★ (Vanilla)", "Crimson Web", "Case Hardened", "Stained", "Blue Steel", "Forest DDPAT", "Night Stripe", "Boreal Forest", "Urban Masked", "Safari Mesh", "Scorched")

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