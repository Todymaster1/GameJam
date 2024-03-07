# ----------------------------------------------------------------------
# Project: CSC121
# Author: yagulbeden
# Date: 3/7/2024
# ----------------------------------------------------------------------
#Visit the Asylum, help inmates escape, use inmates to play at arcade at the worst restaurant in the world. option to blackmail an interior designer to obtain a tommy gun
import random
import time
import os
import sys
import time
import random
import getpass

def asylum():
    ("A mental asylum appears out of nowhere right behind you, conveniently. A feeling of deja reve rushes over you. You have been here before but you also haven't... somehow")
    beginChoice = input(print('Do you want to go left, or charge in the hospital and break all the inmates out(input yes)?'))
    beginChoice.lower()

    if beginChoice == "left":
        beginChoice = input('Do YOU WANT to go left, or charge into the hospital and BREAK ALL THE INMATES OUT(input YES)?')
        if beginChoice =="left":
                beginChoice = input('DO YOU WANT TO BREAK ALL THE INMATES OUT, NO LEFT')
                if beginChoice == "left":
                    print("fine...")
                    print("You are smited by Willem DaFoe from the sky")
                    while True:
                        print("GAME OVER")

    else:
        print("Good, not left")
        pass

asylum()

print("an unsuspecting suicide nanny attacks your peaceful sword!")
time.sleep(0.5)
print("You quickly slash her alligators")
time.sleep(0.5)
var = input("Do you gut the alligators?(yes or no)").lower()
time.sleep(0.5)

var = str(var.lower())
while var != "yes":
    if var == "no":
        break
    print("please input yes or no")
    time.sleep(0.5)
    var = input("Do you gut the alligators?(yes or no)").lower()

alligatorItem = False
if var == "yes":
    print("YOU GUT THE ALLIGATOR IN FRONT OF THE CONSERVATIVE NANNY")
    alligatorItem = True


print("You dash torwards the asylum cells")


print("An interior designer asks you, whats your ID number(1-10?)")
randNum = random.randint(1,10)

guess = int(input("What's your guess?"))
count = 0
while guess != randNum:
    if guess>randNum:
        print("It's too high to be an ID number...")
        guess = int(input("interior designer: 'Are you just guessing numbers??' Guess again:"))

    if guess<randNum:
        print("It's too low to be an ID number...")
        guess = int(input("interior designer: 'Are you just guessing numbers??' Guess again:"))

    if guess == random:
        break
    if count == 2:
        while True:
            print("GAME OVER")
    count += 1
print("Oh alright, you can head down the hall")

print("An officer stands in your way")
warcry = input("What is your warcry SOLDIER")
print("officer: do you have the guts to face me? ):<")
#inv can be implemented somewhere here
if alligatorItem == True:
    print("YOU EAT THE ALLIGATOR GUTS")
    print("FILLLED WITH RAGE AND GUTS YOU DO A curtsy AND UPPERCUT HIS LEFT ARMPIT")
    print(warcry.upper())
else:
    print(warcry.upper())
    print('the officer laughs at your puny attempt and pokes your pelvis fatally')
    choice =input(("LIFESAVER: LEFT OR YES"))
    if choice == "left":
        print("ok buddy")
        while True:
                 print("GAME OVER")
    else:
        pass
print("You do a combo kickflip and lick his right ear canal 7 times!")
print("The officer passes out and you grab his keys")
print("You stand confidently for 3 minutes doing nothing")
#figuring this out
print("There are 8 prisoners and each has a random key to unlock his cell")
print("Guess the keys and free as many prisoners as you can!")

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

prisoners = 3 #DELETE AFTER DONE
print("You escape with", prisoners, "prisoners")
time.sleep(0.5)

print("You stop by the worst restaurant in the world, with food so bad it can be used as a weapon")
time.sleep(0.5)

print("You give the 'freed' meat... PRISONERS to the restaurant and they give you coins to play games in the arcade")
time.sleep(0.5)

numCoins = prisoners
print("You have",numCoins,"coins")
time.sleep(0.5)
print("You enter the arcade")


#importing the modules


#defining the functions
def clear():
    os.system('clear')
'''
def password():
    clear()
    print("Welcome to the password function")
    print("Please enter your username")
    username = input("Username: ")
    print("Please enter your password")
    password = getpass.getpass("Password: ")
    if username == "admin" and password == "admin":
        print("Welcome admin")
        time.sleep(2)
        clear()
    else:
        print("Incorrect username or password")
        time.sleep(2)
        clear()
        password()



#defining the main function
def main():
    clear()
    print("Welcome to the main function")
    print("Please enter your username")
    username = input("Username: ")
    print("Please enter your password")
    password = getpass.getpass("Password: ")
    if username == "admin" and password == "admin":
        print("Welcome admin")
        time.sleep(2)
        clear()
    else:
        print("Incorrect username or password")
        time.sleep(2)
        clear()
        main()

  #calling the main function
main()

  #make an arcade in python with multiple games you can choose from
#the code starts below
    #make an arcade in python with multiple games you can choose from. it is all text based
#the code starts below

#importing modules
import time
import random
import sys

#defining variables

#defining functions
def print(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    os.system('clear')
    print("You have just entered the arcade.")
    print("You see a sign that says 'Welcome to the Arcade'")
    print("You see a sign that says 'Please choose a game'")
    print("You see a sign that says '1. Tic Tac Toe'")
    print("You see a sign that says '2. Rock Paper Scissors'")
    print("You see a sign that says '3. Guess the Number'")
    print("You see a sign that says '4. Exit'")

def valid_input(prompt, option1, option2, option3, option4):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        elif option3 in response:
            break
        elif option4 in response:
            break
        else:
            print("Sorry, I don't understand.")
    return response

def tic_tac_toe():
    os.system('clear')
    print("You have chosen Tic Tac Toe")
    print("You will be playing against the computer")
    print("You will be X and the computer will be O")
    print("You will be going first")
    print("The board will look like this:")
    print("1 | 2 | 3")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("7 | 8 | 9")
    print("You will be choosing a number to place your X")
    print("The computer will then place an O")
    print("The first person to get 3 in a row wins")
    print("Good luck!")
    print("The game will now start")
    #game function starts below
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    def print_board():
        print(board[0] + " | " + board[1] + " | " + board[2])
        print("---------")
        print(board[3] + " | " + board[4] + " | " + board[5])
        print("---------")
        print(board[6] + " | " + board[7] + " | " + board[8])
    def check_win():
        if board[0] == board[1] == board[2]:
            return True
        elif board[3] == board[4] == board[5]:
            return True
        elif board[6] == board[7] == board[8]:
            return True
        elif board[0] == board[3] == board[6]:
            return True
        elif board[1] == board[4] == board[7]:
            return True
        elif board[2] == board[5] == board[8]:
            return True
        elif board[0] == board[4] == board[8]:
            return True
        elif board[2] == board[4] == board[6]:
            return True
        else:
            return False
    def check_tie():
        if "1" not in board and "2" not in board and "3" not in board and "4" not in board and "5" not in board and "6" not in board and "7" not in board and "8" not in board and "9" not in board:
            return True
        else:
            return False
    def player_turn():
        while True:
            player_choice = input("Where would you like to place your X? ")
            if player_choice in board:
                board[int(player_choice) - 1] = "X"
                break
            else:
                print("Sorry, that is not a valid choice")
    def computer_turn():
        while True:
            computer_choice = random.randint(0, 8)
            if board[computer_choice] != "X" and board[computer_choice] != "O":
                board[computer_choice] = "O"
                break
    while True:
        print_board()
        player_turn()
        if check_win() == True:
            print_board()
            print("You have won!")
            break
        elif check_tie() == True:
            print_board()
            print("It is a tie!")
            break
        computer_turn()
        if check_win() == True:
            print_board()
            print("The computer has won!")
            break
        elif check_tie() == True:
            print_board()
            print("It is a tie!")
            break
    #game function ends above
    print("Would you like to play again?")
    response = valid_input("Please enter yes or no.\n", "yes", "no", "", "")
    if "yes" in response:
        tic_tac_toe()
    elif "no" in response:
        print("Thank you for playing!")
        intro()

def rock_paper_scissors():
    os.system('clear')
    print("You have chosen Rock Paper Scissors")
    print("You will be playing against the computer")
    print("You will be going first")
    print("The game will now start")
    #game function starts below
    def check_win(player_choice, computer_choice):
        if player_choice == "rock" and computer_choice == "scissors":
            return True
        elif player_choice == "paper" and computer_choice == "rock":
            return True
        elif player_choice == "scissors" and computer_choice == "paper":
            return True
        else:
            return False
    def check_tie(player_choice, computer_choice):
        if player_choice == computer_choice:
            return True
        else:
            return False
    while True:
        player_choice = input("Please choose rock, paper, or scissors. ").lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        if check_win(player_choice, computer_choice) == True:
            print("You have won!")
            break
        elif check_tie(player_choice, computer_choice) == True:
            print("It is a tie!")
            break
        else:
            print("The computer has won!")
            break
    #game function ends above
    print("Would you like to play again?")
    response = valid_input("Please enter yes or no.\n", "yes", "no", "", "")
    if "yes" in response:
        rock_paper_scissors()
    elif "no" in response:
        print("Thank you for playing!")
        intro()

def guess_the_number():
    print("You have chosen Guess the Number")
    print("You will be playing against the computer")
    print("The computer will choose a number between 1 and 10")
    print("You will have to guess the number")
    print("You will have 3 tries to guess the number")
    print("The game will now start")
    #game function starts below
    while True:
        computer_choice = random.randint(1, 10)
        print("The computer has chosen a number")
        print("You will now have 3 tries to guess the number")
        for i in range(3):
            player_choice = int(input("Please guess a number between 1 and 10. "))
            if player_choice == computer_choice:
                print("You have guessed the number!")
                break
            elif player_choice > computer_choice:
                print("Your guess is too high")
            elif player_choice < computer_choice:
                print("Your guess is too low")
        if player_choice == computer_choice:
            break
        else:
            print("You have run out of tries")
            print("The computer has won!")
            break
    #game function ends above
    print("Would you like to play again?")
    response = valid_input("Please enter yes or no.\n", "yes", "no", "", "")
    if "yes" in response:
        guess_the_number()
    elif "no" in response:
        print("Thank you for playing!")
        intro()

#defining game flow
def game_flow():
    os.system('clear')
    response = valid_input("Please enter 1, 2, 3, or 4.\n", "1", "2", "3", "4")
    if "1" in response:
        tic_tac_toe()
    elif "2" in response:
        rock_paper_scissors()
    elif "3" in response:
        guess_the_number()
    elif "4" in response:
        print("Thank you for playing!")
        print("The game will now end")
        sys.exit()

#calling functions
intro()
game_flow()
'''

print("end")