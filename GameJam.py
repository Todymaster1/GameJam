# Imports
import os
import time
import random


def clear():
    os.clear()


def main():
    name = input("What's your name?: ")

    time.sleep(1)
    print("""
                                                                                                                               
                                                                                                                       
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/   
                                                                                                                       
                                                                                                                       
 __      __       .__                                    __               ________      .__         _____  _____       
/  \    /  \ ____ |  |   ____  ____   _____   ____     _/  |_  ____      /  _____/______|__| ______/ ____\/ ____\____  
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \    \   __\/  _ \    /   \  __\_  __ \  |/     \   __\ |   __\/ __ \ 
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/     |  | (  <_> )   \    \_\  \  | \/  |  Y Y  \  |   |  | \  ___/ 
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >    |__|  \____/     \______  /__|  |__|__|_|  /__|   |__|  \___  >
       \/       \/          \/            \/     \/                             \/               \/                 \/ 
                                                                                                                       
                                                                                                                       
  ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   ______   
 /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/  /_____/   
                                                                                                                       
                                                                                                                       
        """)
    print(f"Welcome to Grimffe, {name}")  # Temporary name
    time.sleep(1)


main()


def adventure_game():
    print("Antagonist: The Goblin King")
    print("Protagonist: An outlaw")
    print("Setting: An abandoned toy factory")

    choice = input("Choose your path: [1] Defeat the f-eminists, [2] Wrestle fire-breathing alligators,\
 [3] Play blackjack with a bunch of hobos, [4] Get the EIGHT FOOT MAN EATING BUNNY: ")

    if choice == '1':
        print("You defeated the f-eminists!")
        print("""
        
                                      ,-.. _. ,. ,._
                                  .-'         .     '.
                                 /             .      /_./.
                                '                        '.
                               .                           '
                              '            =\ : , \         \ 
                             '            '` `   `  =        '
                             |,.        _\           ',       \ 
                             /   \    ."               ',.    /
                            || ,' `  ,                  ' \_.'
                            |\ -. / ,       `'":,      /
                          ,-= .   ,'       '_   `;.    |
                         /  /  -'            "'`    ,:,
                      _,/|,'    ,                   '
               ___,--' | |                    (    /
          _,-'`        . .      .            , '- _'          .-.
        ,'              \        .       `,'"`';/.          ,'   )
      ,`                 .'       :     /  ';\ \   '.     ,'    .'
    ,'                   |.\       ';.'.,. .;.\ \  ,..:_'_    .
   /  .                    '.       .'';_:;'`  '_(        ' '-.
   |   .                     '.'.,-'   ,       (    '" - ._    )
  / .   `                      '.             _,'-._        ` (
 /    .       [lf]             _ |   '      .' '.    ' .  _    )
                              (:)          '      '        '   '
        """)
        print()
    elif choice == '2':
        print("You wrestled fire-breathing alligators!")
        print("""
                    _.---._     .---.
            __...---' .---. `---'-.   `.
        .-''__.--' _.'( | )`.  `.  `._ :
      .'__-'_ .--'' ._`---'_.-.  `.   `-`.
             ~ -._ -._``---. -.    `-._   `.
                  ~ -.._ _ _ _ ..-_ `.  `-._``--.._
                               -~ -._  `-.  -. `-._``--.._.--''.
                                    ~ ~-.__     -._  `-.__   `. `.
                                          ~~ ~---...__ _    ._ .` `.
                                                      ~  ~--.....--~`
⠀                                                       ⣠⣿⣿⣿⣿⣦⣀⠀⣦⡀⠀   ⠀⠀⠀⠀⠀⢀⣤⣤⣤⣄⡀⠀⠀
⠀⠀                                                       ⠙⢿⣿⣿⣿⣿⣿⣷⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠞⠛⢿⣿⣿⣿⣆⠀
⠀⠀                                                       ⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⠀
⠀⠀                                                        ⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀
⠀⠀                                                         ⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿⣷⣤⣀⠀⠀⢀⣴⣿⣿⣿⣿⠀
⠀                                                       ⠀⠀⠀  ⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀                                                         ⠀⠀⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀                                                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀                                                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀                                                     ⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀                                                      ⠀⠀⠀⠸⣿⣦⣄⣀⣀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⠀                                                    ⠀⠀⠀⠀⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀
""")
        print()
    elif choice == '3':
        print("You played blackjack with a bunch of hobos!")
        print("""
              _,,,,_
           .(((()()()(
           ())()()))())
          ((,.""-,(()())
          \ @ ) @  )/)()
          .'-. -   (C))
          (  (_. ` .))
          \ .___.   .'
         __`.____.' \_____
       /(  " /))_\.-'  (  `\ 
      / ( _  o/(o "  _ \   `.
     (  /. . o)/o       (    \ 
    /   ( . o/(o .  "  .)\    )
   (   )( _ o)\o  _   . )(    )
   (   (.' o)/o    `.   )/   /
    \ ( . "o((o .  . ` _/   )
     (/)____o)/o______(c`-.)
      |)_|__[H]___|___(//)'
      (   )  : \  )    `''
      (_)  (  )    \ (_ )
      (      .   (      )
     (  ( )   (\  /  )  )
      (    (   (       )
      (  ( ) ./ \ ( .( )
       (     )  (     )
       |"^"")    ("^"")
       |    /    \    |
       ),,,,)    |,,,,/
       /,,,,(    ),,,,(
    .-',,,,,)    /,,,,\ 
   ((((_).-'    (_)())))
        """)
        print()
    elif choice == '4':
        print("You got the EIGHT FOOT MAN EATING BUNNY!")
        print("""

        """)
        print()
    else:
        print("Invalid choice. Choose again.")
        print()

    print("You visit an asylum and help some inmates escape.")
    print()

    print("You visit a restaurant and use the bad food as a weapon.")
    print()

    print("You blackmail a criminal mastermind for a tommy gun.")
    print()

    print("You slap the Goblin King and engage in a hard boss battle.")
    print()

    print("Both paths lead to the old lady having the crown stolen from her.")

    if random.choice([True, False]):
        print("One of the inmates betrays you, commits political fraud, and informs the Goblin King.")
        print()
    else:
        print("No betrayal occurred.")
        print()

    print("The Goblin King comes to fight you.")

    if random.choice([True, False]):
        print("You defeat the Goblin King and inherit the lost manuscript.")
        print()
    else:
        print("You lose to the Goblin King and die.")
        print()


adventure_game()

