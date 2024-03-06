'''
Branching Paths: 
Defeat the f-eminists, wrestle fire breathing alligators, play blackjack with a bunch of hobos, and get the EIGHT FOOT MAN EATING BUNNY.
Visit an asylum and help some inmates escape. Visit a restaurant, and use the bad food as a weapon.blackmail a criminal mastermind for a tommy gun
Slap the goblin king and fight him directly  ( Hard Boss battle)     EXCEPTION
Both of these stories lead to:
An old lady has the crown and he steals it from her.
One of the inmates betrays them, commits political fraud and informs the Goblin King of their intentions.
The Goblin King comes at them and you have to defeat him.
Ending: 
You defeat the Goblin King and inherent the lost manuscript
You lose to the Goblin King and 

'''
# Imports
import os
import time
import random
import Ascii_Art

def clear():
  os.system('clear')

def moving_text(text):
  for letter in text:
    print(letter, end="", flush=True) #Flush got from online
    time.sleep(0.1)

# Main Code
def main():
  health = 100
  inventory = []
  has_manuscript = False
  name = input("What's your name?: ")
  clear()
  time.sleep(1)

  print(f"Welcome to Grimffe {name}")# Temporary name

  moving_text("Welcome to Grimffe")
  
  time.sleep(1)
  

main()


