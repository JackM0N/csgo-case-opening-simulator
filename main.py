import noCase as nc

print('')
print("Hello! Welcome to my CS:GO Case Opening Simulator!")
print('')
print("0. Generic case (No skin names, just rarity and wear)")
print('')

while True:

    choice = input("Which case would you like to open?")

    if choice.isdigit() and int(choice)>=0 and int(choice)<=0:
        choice = int(choice)
        break
    else:
        print("Please insert a viable number!")

if choice == 0:
    nc.run()
