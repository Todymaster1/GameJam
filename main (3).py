# Imports
import os
import random
import time
import Ascii_Art
import Blackjack


def clear():
    os.system('cls') #Change to cls


def moving_text(text):
    for letter in text:
        print(letter, end="", flush=True)
        time.sleep(0.07)
    print()
    print()


def add_to_inventory(inventory, item):
    inventory.append(item)


def inventory_show(inventory):
    moving_text("Your inventory contains: ")
    for item in inventory:
        print(item)


def door(inventory):
    for item in inventory:
        if "key" in inventory:
            return True


def black_jack_knowledge():
    cards = [
        "Ace |", "2 |", "3 |", "4 |", "5 |", "6 |", "7 |", "8 |", "9 |", "10 |",
        "Jack |", "Queen |", "King |"
    ]
    values = [
        "1 or 11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"
    ]

    knowledge = int(input("Hobo: Do you know how to play BlackJack? [1] Yes [2] No: "))
    if knowledge == 2:
        clear()
        moving_text(
            """In blackjack, the player's goal is to have a hand with value closer to 21 than the dealer's without exceeding 21 or by the dealer's hand going over 21. Value of cards are also different. \n\nCard Values are as follows: \n""")
        for cards, values in zip(cards, values):
            print(cards, values)
        exit = input("\n(When ready, press enter to start playing.) ")
        if exit == "":
            clear()


# Main Code
def main():
    # Vars
    inventory = ["Hat", "Wallet"]
    money = 20
    gun_ammo = 10

    # Intro to the game
    name = input("What's your name?: ")
    clear()
    Ascii_Art.welcome()
    time.sleep(2)
    clear()

    # Storyline
    moving_text("""You are in the heart of a sleepy town nestled amidst rolling hills, there stood an ancient toy factory, its weathered facade a testament to bygone days of childhood wonder. It was within the confines of this forgotten place that my journey began, waking up amidst a sea of discarded toys, the faint echoes of laughter still lingering in the air.
""")

    time.sleep(2)
    clear()

    moving_text("""Off to the side you spy a dumpster. It may hold something valuable.""")

    time.sleep(2)
    clear()

    dumpster_search = int(input("Do you want to search the dumpster? [1] Yes [2] No: "))

    if dumpster_search == 1:
        clear()
        moving_text(
            """You find a gun in the dumpster. How strange. You check it and see that it still has a magazine of 10 rounds. You place the gun in your back pocket.""")
        add_to_inventory(inventory, "Gun")
        inventory_show(inventory)
        time.sleep(2)
        clear()
    elif dumpster_search == 2:
        clear()
        moving_text("A pity, you lost out on something cool for your future endeavors.")
    else:
        clear()
        moving_text("You didn't pick a valid option. You lost out on something cool for your future endeavors.")

    time.sleep(2)
    clear()

    moving_text("""As you rubbed the sleep from your eyes, you found yourself drawn to three ornately carved doors standing sentinel at the far end of the factory floor. Each door seemed to hold a promise of adventure, beckoning you with whispered secrets and untold mysteries.
""")
    time.sleep(2)
    clear()

    moving_text(
        """Door 1: You sense you have to defeat the f-eminists and fire breathing alligators. You will have to play blackjack with a bunch of hobos and then find the EIGHT FOOT MAN EATING BUNNY.""")
    time.sleep(2)

    moving_text(
        """Door 2: You will discover an asylum and help some inmates escape. Then visit a restaurant, and use the bad food as a weapon. And finally blackmail a criminal mastermind with his family for a tommy gun.""")
    time.sleep(2)

    moving_text("""Door 3: You are unsure of what is behind this door. It emits an ominous presence and you feel that it will be dangerous to continue.
""")
    time.sleep(2)

    clear()
    moving_text("""You enter the first door and you find a group of fierce f-eminists threatening to disrupt the peace. They threaten to rip you to shreds for saying you don’t like women, but with your quick wit and strategic thinking, you navigate through their arguments, finding common ground and diffusing the tension peacefully.
  """)
    time.sleep(2)
    clear()
    moving_text(
        """Venturing into the untamed wilderness, you found yourself face to face with fire-breathing alligators guarding the path ahead. Undeterred, you square his shoulders and engage in a fierce battle of strength and agility. With cunning maneuvers and sheer determination, you emerge victorious, the fiery beasts vanquished.""")
    time.sleep(2)
    clear()
    moving_text(
        """You stumble upon a group of hobos engaged in a heated game of blackjack. Ever the opportunist, you join the game. You have to get $50 to win.""")
    time.sleep(2)
    clear()
    black_jack_knowledge()
    clear()
    while money <= 50 or money >= 0:
        bet = int(input(f"You have ${money}. How much do you wanna bet? (Whole numbers): "))
        win_or_lose = Blackjack.black_jack()
        if win_or_lose == True:
            money += bet
            moving_text(f"You won ${bet}! You now have ${money}")
            time.sleep(2)
            clear()
        elif win_or_lose == False:
            money -= bet
            moving_text(f"You lost ${bet}! You now have ${money}")
            time.sleep(2)
            clear()
        else:
            moving_text(f"Tie! You still have ${money}")
            time.sleep(2)
            clear()

    if money == 0:
        moving_text("You are broke. Game over.")
        Ascii_Art.defeat()
        exit()

    def asylum():
        moving_text(
            """A mental asylum appears out of nowhere right behind you, conveniently. A feeling of deja reve rushes over you. You have been here before but you also haven't... somehow""")
        moving_text("Do you want to go left [1], or charge in the hospital and break all the inmates out[2]?")
        beginChoice = input()
        beginChoice.lower()
        clear()
        if beginChoice == "1":
            beginChoice = input(
                'Do YOU WANT to go left[1], or charge into the hospital and BREAK ALL THE INMATES OUT[2]?: ')
            clear()
            if beginChoice == "1":
                beginChoice = input('DO YOU WANT TO BREAK ALL THE INMATES OUT[2], NO LEFT: ')
                clear()
                if beginChoice == "1":
                    moving_text("fine...")
                    moving_text("You are smited by Willem DaFoe from the sky")
                    while True:
                        moving_text("GAME OVER")
                        Ascii_Art.defeat()
        else:
            pass
        moving_text("Good, not left")

    clear()
    asylum()

    moving_text("An unsuspecting nanny attacks your peaceful sword!")

    moving_text("You quickly slash her alligators")
    moving_text("You are now a master swordsman")
    var = input("Do you gut the alligators? [1] Yes [2] No: ").lower()
    clear()

    var = str(var.lower())
    while var != "1":
        if var == "2":
            break
        moving_text("Please input 1 or 2: ")

        var = input("Do you gut the alligators? [1] Yes [2] No: ").lower()

    alligatorItem = False
    if var == "1":
        moving_text("YOU GUT THE ALLIGATOR IN FRONT OF THE CONSERVATIVE NANNY")
        alligatorItem = True

    moving_text("You dash towards the asylum cells")

    clear()
    moving_text("An interior designer asks you, whats your ID number(1-10?)")
    randNum = random.randint(1, 10)

    guess = int(input("What's your guess?: "))
    count = 0
    while guess != randNum:
        if guess > randNum:
            moving_text("It's too high to be an ID number...")
            guess = int(input("interior designer: 'Are you just guessing numbers??' Guess again: "))

        if guess < randNum:
            moving_text("It's too low to be an ID number...")
            guess = int(input("Interior designer: 'Are you just guessing numbers??' Guess again: "))

        if guess == random:
            break
        if count == 2:
            while True:
                moving_text("GAME OVER")
                Ascii_Art.defeat()
        count += 1
    moving_text("Oh alright, you can head down the hall")
    clear()
    moving_text("An officer stands in your way")
    warcry = input("What is your warcry SOLDIER: ")
    clear()
    moving_text("officer: do you have the guts to face me? ):<")
    # inv can be implemented somewhere here
    if alligatorItem == True:
        moving_text("YOU EAT THE ALLIGATOR GUTS")
        moving_text("FILLLED WITH RAGE AND GUTS YOU DO A curtsy AND UPPERCUT HIS LEFT ARMPIT")
        moving_text(warcry.upper())
    else:
        moving_text(warcry.upper())
        moving_text('the officer laughs at your puny attempt and pokes your pelvis fatally')
        choice = input(("LIFESAVER: LEFT OR YES: "))
        if choice == "left":
            moving_text("ok buddy")
            while True:
                moving_text("GAME OVER")
                Ascii_Art.defeat()
        else:
            pass
    moving_text("You do a combo kickflip and lick his right ear canal 7 times!")
    moving_text("The officer passes out and you grab his keys")
    clear()
    moving_text("There are 8 prisoners and each has a random key to unlock his cell")
    moving_text("Guess the keys and free as many prisoners as you can!")

    prisoners = 8
    freed = 0
    while prisoners > 0:
        print("Prisoner", prisoners)
        randomThing = random.randint(1, 3)
        guess = int(input("Guess which key to use(1-3): "))
        randomThing = 1
        if guess == randomThing:
            freed += 1
            print("Prisoner unlocked:", prisoners)
        print("You have freed", freed, "prisoners")
        prisoners -= 1

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
        goon += 1
        moving_text("QUICK ACTION, TYPE:", foop)
        quickaction = input()
        if quickaction == foop:
            moving_text("Goon", goon, " falls to the ground, he explodes")
            count += 1
        else:
            moving_text("The goons BITE YOU, you take heavy damage")
            chocholate += 1
        if chocholate == 4:
              print("GAME OVER")
              Ascii_Art.defeat()
    moving_text("The Goons retreat and you take your Tommy Gun and mow them all down")
    moving_text("Now to challenge the GOBLIN KING")

    time.sleep(2)
    clear()
    moving_text(
        """After continuing for sometime, you find yourself back in the toy factory, but something has changed. Now, only one door remains. Before you can check this out, you glimpse... something. Tucked away in the darkest corner of the factory, hidden from prying eyes, lay a single toy, a crown, untouched by the ravages of time.""")
    time.sleep(2)
    clear()

    moving_text(
        """With trembling hands, you reach out to grasp it, feeling a surge of warmth flood through you as you hold it close. In that moment, you understand the true power of toys – not simply as playthings, but as vessels of imagination and wonder, capable of transcending even the darkest of times.""")
    time.sleep(2)
    clear()

    moving_text(
        """But my moment of revelation was short-lived as I heard a sudden commotion behind me. Whirling around, I saw an old lady, her eyes blazing with fury. In a flash, she lunged towards me, intent on reclaiming what was hers.""")
    time.sleep(2)
    clear()

    time.sleep(2)
    clear()
    final_choice = int(input(
        "What will you do? [1] Knock the lady down and run to the door [2] Hesitate and get knocked unconscious by the old lady: "))

    if final_choice == 2:
        moving_text("You got knocked down. Game Over.")
        exit()
    else:
        moving_text("You choose to knock her down and run.")
    time.sleep(2)
    clear()

    moving_text(
        """You want to feel bad about hurting her, but that moment is short lived and you rush to the door. With shaking hands, you place the crown on your head and the door opens. With a deep breath, you close your eyes and enter""")

    time.sleep(2)
    clear()
    moving_text(
        """When you open them, you find yourself in a massive throne room. Inside is a dark figure. As it comes into the light, you realize with a surge of fear that this is the Goblin King. You somehow know that he has been waiting for you this entire time.""")

    time.sleep(2)
    clear()
    moving_text("You will have to defeat him to continue.")
    time.sleep(2)
    clear()
    moving_text("Goblin King")
    # Ascii_Art.Goblin_King()
    time.sleep(2)
    clear()

    for item in inventory:
        if 'Gun' in inventory:
            attack_goblin = input(f"What do you want to do? [1] Use your gun. {gun_ammo} bullets [2] [3]")
            if attack_goblin == 1:
                moving_text(f"You choose option {attack_goblin}")
                moving_text("You used your gun and defeated the Goblin King")

            elif attack_goblin == 2:
                moving_text(f"You choose option {attack_goblin}")
                time.sleep(2)
                clear()
            elif attack_goblin == 3:
                moving_text(f"You choose option {attack_goblin}")
                time.sleep(2)
                clear()
            else:
                moving_text("You failed to choose correctly.")
                Ascii_art.defeat()
        else:
            attack_goblin = input(f"What do you want to do? [1] [2]")
            if attack_goblin == 1:
                moving_text(f"You choose option {attack_goblin}")
                moving_text("You threw your hat at him. It was secretly a bomb and the Goblin King blows up.")
                time.sleep(2)
                clear()
                Ascii_Art.victory()
            elif attack_goblin == 2:
                moving_text(f"You choose option {attack_goblin}")
                print("You knock him into the pit. He has fallen and can't get up.")
                time.sleep(2)
                clear()
                Ascii_Art.victory()
            else:
                moving_text("You failed to choose correctly.")
                Ascii_art.defeat()

main()
