import noCase as nc
import skins as s
import case as c

print('')
print("Hello! Welcome to my CS:GO Case Opening Simulator!")
print('')
print("0. Generic case (No skin names, just rarity and wear)")
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

while True:

    choice = input("Which case would you like to open? ")

    if choice.isdigit() and int(choice)>=0 and int(choice)<=10:  # <---Dont forget to update this number!
        choice = int(choice)
        break
    else:
        print("Please insert a viable number!")

if choice == 0:
    nc.run()
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


#Future idea: make it posible to input values of keys and chests to display how much money was spent (Maybe even scrape Steam values of chests and skins from marketplace)