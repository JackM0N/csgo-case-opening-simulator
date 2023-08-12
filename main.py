import skins as s
import case as c

print('')
print("Hello! Welcome to my CS:GO Case Opening Simulator!")

while True:

    while True:

        print('')
        print("0. None (Exit)")
        print("1. Dreams & Nightmares Case")
        print("2. Riptide")
        print("3. Fracture")
        print("4. Chroma")
        print("5. Chroma 2")
        print("6. Chroma 3")
        print("7. CS20")
        print("8. Prisma")
        print("9. Danger Zone")
        print("10. Revolution")
        print('')
        choice = input("Which case would you like to open? ")

        if choice.isdigit() and int(choice)>=0 and int(choice)<=10:  # <---Dont forget to update this number!
            choice = int(choice)
            break
        else:
            print("Please insert a viable number!")

    if choice == 0:
        print("Okay! Cya!")
        break
    elif choice == 1:
        blue, purple, pink, red, goldknife, goldpattern = s.dreamsAndNightmaresSkins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 2:
        blue, purple, pink, red, goldknife, goldpattern = s.riptideSkins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 3:
        blue, purple, pink, red, goldknife, goldpattern = s.fractureSkins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 4:
        blue, purple, pink, red, goldknife, goldpattern = s.chromaSkins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 5:
        blue, purple, pink, red, goldknife, goldpattern = s.chroma2Skins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 6:
        blue, purple, pink, red, goldknife, goldpattern = s.chroma3Skins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 7:
        blue, purple, pink, red, goldknife, goldpattern = s.cs20Skins()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 8:
        blue, purple, pink, red, goldknife, goldpattern = s.prismaCase()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)
    elif choice == 9:
        blue, purple, pink, red, goldknife, goldpattern = s.dangerZoneCase()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)    
    elif choice == 10:
        blue, purple, pink, red, goldknife, goldpattern = s.revolutionCase()
        cscase = c.Case(blue, purple, pink, red, goldknife, goldpattern)

    cscase.run()

#Started 100 cases: 18.30 finished: crashed at 65th case