# ----------------------------------------------------------------------
# Project: CSC121
# Author: yagulbeden
# Date: 3/7/2024
# ----------------------------------------------------------------------
#Visit the Asylum, help inmates escape, use inmates to play at arcade at the worst restaurant in the world. option to blackmail an interior designer to obtain a tommy gun
import time
import os
import sys
import time
import random
def clear():
  os.system('clear')
clear()
print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n ")

def moving_text(text):
    for letter in text:
        print(letter, end="", flush = True)
        time.sleep(0.06)
    print()

def asylum():
  moving_text("A mental asylum appears out of nowhere right behind you, conveniently. A feeling of deja reve rushes over you. You have been here before but you also haven't... somehow")
  moving_text("Do you want to go left[1], or charge in the hospital and break all the inmates out[2]?")
  beginChoice = input()
  beginChoice.lower()
  clear()
  if beginChoice == "1":
      beginChoice = input('Do YOU WANT to go left[1], or charge into the hospital and BREAK ALL THE INMATES OUT[2]?: ')
      clear()
      if beginChoice =="1":
            beginChoice = input('DO YOU WANT TO BREAK ALL THE INMATES OUT[2], NO LEFT: ')
            clear()
            if beginChoice == "1":
              moving_text("fine...")
              moving_text("You are smited by Willem DaFoe from the sky")
              while True:
                moving_text("GAME OVER")
                clear()


  else:
      pass
  moving_text("Good, not left")
clear()
asylum()

moving_text("An unsuspecting nanny attacks your peaceful sword!")

moving_text("You quickly slash her alligators")
moving_text("You are now a master swordsman")
var = input("Do you gut the alligators?(yes[1] or no[2]: )").lower()
clear()

var = str(var.lower())
while var != "1":
    if var == "2":
        break
    moving_text("Please input 1 or 2: ")

    var = input("Do you gut the alligators?(yes[1] or no[2]: )").lower()

alligatorItem = False
if var == "1":
    moving_text("YOU GUT THE ALLIGATOR IN FRONT OF THE CONSERVATIVE NANNY")
    alligatorItem = True


moving_text("You dash torwards the asylum cells")

clear()
moving_text("An interior designer asks you, whats your ID number(1-10?)")
randNum = random.randint(1,10)

guess = int(input("What's your guess?: "))
count = 0
while guess != randNum:
    if guess>randNum:
        moving_text("It's too high to be an ID number...")
        guess = int(input("interior designer: 'Are you just guessing numbers??' Guess again: "))

    if guess<randNum:
        moving_text("It's too low to be an ID number...")
        guess = int(input("Interior designer: 'Are you just guessing numbers??' Guess again: "))

    if guess == random:
        break
    if count == 2:
        while True:
            moving_text("GAME OVER")
    count += 1
moving_text("Oh alright, you can head down the hall")
clear()
moving_text("An officer stands in your way")
warcry = input("What is your warcry SOLDIER: ")
clear()
moving_text("officer: do you have the guts to face me? ):<")
#inv can be implemented somewhere here
if alligatorItem == True:
    moving_text("YOU EAT THE ALLIGATOR GUTS")
    moving_text("FILLLED WITH RAGE AND GUTS YOU DO A curtsy AND UPPERCUT HIS LEFT ARMPIT")
    moving_text(warcry.upper())
else:
    moving_text(warcry.upper())
    moving_text('the officer laughs at your puny attempt and pokes your pelvis fatally')
    choice =input(("LIFESAVER: LEFT OR YES: "))
    if choice == "left":
        moving_text("ok buddy")
        while True:
                moving_text("GAME OVER")
    else:
        pass
moving_text("You do a combo kickflip and lick his right ear canal 7 times!")
moving_text("The officer passes out and you grab his keys")
clear()
moving_text("There are 8 prisoners and each has a random key to unlock his cell")
moving_text("Guess the keys and free as many prisoners as you can!")

prisoners = 8
freed = 0
while prisoners>0:
    print("Prisoner",prisoners)
    randomThing = random.randint(1,3)
    guess = int(input("Guess which key to use(1-3)"))
    randomThing = 1
    if guess == randomThing:
        freed +=1
        print("Prisoner unlocked:",prisoners)
    print("You have freed",freed,"prisoners")
    prisoners -=1

clear()
moving_text("You escape with", prisoners, "prisoners")


moving_text("You stop by the worst restaurant in the world, with food so bad it can be used as a weapon")


moving_text("7 GOONS AMBUSH YOU")
moving_text("YOU RUSH THEM WITH YOUR INMATES TO TAKE THE TOMMY GUN THAT IS RIGHTFULLY YOUR UnCLE'S")

foo = ['brave brigadiers', 'mad cow', 'specific pacific', 'imaginary menagerie', 'which witch is which']
foop = random.choice(foo)
moving_text("You cast spells to enhance the effect of your attacks!")
count = 0
chocholate = 0
goon = 0
while count < 3:
    foop = random.choice(foo)
    goon+=1
    moving_text("QUICK ACTION, TYPE:",foop)
    quickaction = input()
    if quickaction == foop:
      moving_text("Goon",goon," falls to the ground, he explodes")
      count +=1
    else:
      moving_text("The goons BITE YOU, you take heavy damage")
      chocholate +=1
    if chocholate == 4:
        while True:
            print("GAME OVER")
moving_text("The Goons retreat and you take your Tommy Gun and mow them all down")
moving_text("Now to challenge the GOBLIN KING")

#importing the modules


#defining the functions
def clear():
    os.system('clear')

moving_text("end")