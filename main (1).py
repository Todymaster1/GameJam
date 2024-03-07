# Imports
import os
import time
import random
#import Ascii_Art
import Blackjack

def clear():
    os.system('clear')


def moving_text(text):
    for letter in text:
        print(letter, end="", flush = True)
        time.sleep(0.07)


def add_to_inventory(inventory, item):
    inventory.append(item)


def actions():
  moving_text(f"Actions: [1] Inventory, [2] Attack, [3] Run, [4] Pick Up Item")
  input("What action do you wanna take?: ")

def door(inventory):
  for item in inventory:
    if "key" in inventory:
      return True

# Main Code
def main():
    # Vars
    health = 100
    inventory = ["Hat", "Wallet"]
    has_manuscript = False
    can_pickup = False

    # Intro to the game
    name = input("What's your name?: ")
    clear()
    moving_text(f"Welcome to Grimffe {name}")
    time.sleep(2)
    clear()

    # Storyline
    moving_text("""In the heart of a sleepy town nestled amidst rolling hills, there stood an ancient toy factory, its weathered facade a testament to bygone days of childhood wonder. It was within the confines of this forgotten place that my journey began, waking up amidst a sea of discarded toys, the faint echoes of laughter still lingering in the air.
""")
  
    time.sleep(2)
    clear()

    moving_text("""Off to the side you spy a dumpster. It may hold something valuable.""")

    dumpster_search = int(input("Do you want to search the dumpster? [1] Yes [2] No: "))
    if dumpster_search == 1:
      moving_text("""You find a gun in the dumpster. How strange. You check it and see that it still has a magazine of 10 rounds. You place the gun in your back pocket.""")
      add_to_inventory(inventory, "Gun")
    elif dumpster_search == 2:
      moving_text("A pity, you lost out on something cool for your future endeavors.")
    else:
      moving_text("You didn't pick a valid option. You lost out on something cool for your future endeavors.")

    time.sleep(2)
    clear()
    moving_text(""As you rubbed the sleep from your eyes, you found yourself drawn to three ornately carved doors standing sentinel at the far end of the factory floor. Each door seemed to hold a promise of adventure, beckoning you with whispered secrets and untold mysteries.
""")
    time.sleep(2)
    

  
        
  
  

  

    # Inventory
    print()
    choice = actions()
    if choice == 1:
        for item in inventory:
            print(item)
        time.sleep(1)
        clear()

    item = "key"
    print(f"You found {item}")
    if actions() == 4:
      inventory = add_to_inventory(inventory, item)
    else:
      moving_text("You can't do that")







main()