import noCase as nc
import dreamsAndNightmares as dan

print('')
print("Hello! Welcome to my CS:GO Case Opening Simulator!")
print('')
print("0. Generic case (No skin names, just rarity and wear)")
print("1. Dreams & Nightmares Case")
print('')

while True:

    choice = input("Which case would you like to open? ")

    if choice.isdigit() and int(choice)>=0 and int(choice)<=1:
        choice = int(choice)
        break
    else:
        print("Please insert a viable number!")

if choice == 0:
    nc.run()
elif choice == 1:
    dan.run()

#Future idea: make terminal output display correct rarity color!
