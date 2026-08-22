#imports "random" module
import random

#imports "time" module for typing effect on prints
import time

#typing effect function
def type_text(text):
    for character in text:
        print(character, end="", flush=True)
        time.sleep(0.03)
    print()




#start of user-visible text
type_text("It's time to roll the dice.\nLet the fun lil math rocks decide your fate.")

#switch to activate dice roller
diceroller_active = 1

while diceroller_active == 1:

    type_text('\nYou can roll a d6, d8, d10, d12, d20, or d100.\nYou can also type "quit" to quit.\n', )
    die_choice = input("\nWhich die would you like to roll? ")

#d20 roller
    if die_choice == "d20":
        d20_roll = random.randint(1, 20)
        if d20_roll == 20:
            #CRITICAL HIT!
            type_text("\aAwww yeah, it's a critical hit!\n\nNAT 20!!!!")
        else:
            type_text(f"\nyou rolled a {d20_roll}")
    
#d6 roller
    elif die_choice == "d6":
        
        type_text(f"\nYou rolled a {random.randint(1, 6)}")

#d8 roller
    elif die_choice == "d8":
        type_text(f"\nYou rolled a {random.randint(1, 8)}")

#d10 roller
    elif die_choice == "d10":
        type_text(f"\nYou rolled a {random.randint(1, 10)}")

#d12 roller
    elif die_choice == "d12":
        type_text(f"\nYou rolled a {random.randint(1, 12)}")

#d100 roller
    elif die_choice == "d100":
        type_text(f"\nYou rolled a {random.randint(1, 100)}")

    elif die_choice == "quit":
        exit_switch = input("Do you want to exit the die roller?", )
        if exit_switch == "yes":
            diceroller_active = 0

quit()
