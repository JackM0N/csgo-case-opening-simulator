import noCase as nc
import dreamsAndNightmares as dan
import riptide as rip
import fracture as fr

print('')
print("Hello! Welcome to my CS:GO Case Opening Simulator!")
print('')
print("0. Generic case (No skin names, just rarity and wear)")
print("1. Dreams & Nightmares Case")
print("2. Riptide")
print("3. Fracture")
print('')

while True:

    choice = input("Which case would you like to open? ")

    if choice.isdigit() and int(choice)>=0 and int(choice)<=3:  # <---Dont forget to update this number!
        choice = int(choice)
        break
    else:
        print("Please insert a viable number!")

if choice == 0:
    nc.run()
elif choice == 1:
    dan.run()
elif choice == 2:
    rip.run()
elif choice == 3:
    fr.run()

#Future idea: make terminal output display correct rarity color!
#Future idea: make it posible to input values of keys and chests to display how much money was spent (Maybe even scrape Steam values of chests and skins from marketplace)