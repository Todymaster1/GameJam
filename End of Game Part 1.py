import Ascii_Art

print()
print("After continuing for sometime, you find yourself back in the toy factory,"
      "\nbut something has changed. Now, only one door remains."
      "\nBefore you can check this out, you glimpse… something."
      "\nTucked away in the darkest corner of the factory, hidden from prying eyes,"
      "\nlay a single toy, a crown, untouched by the ravages of time.")
print()

print("With trembling hands, you reach out to grasp it,"
      "\nfeeling a surge of warmth flood through you as you hold it close."
      "\nIn that moment, you understand the true power of toys – not simply as playthings,"
      "\nbut as vessels of imagination and wonder,"
      "\ncapable of transcending even the darkest of times.")
print()

print("But my moment of revelation was short-lived as I heard a sudden commotion behind me."
      "\nWhirling around, I saw an old lady, her eyes blazing with fury."
      "\nIn a flash, she lunged towards me, intent on reclaiming what was hers.")
print()

print("1: Knock the lady down and run to the door."
      "\n2: Hesitate and get knocked unconscious by the old lady.")

print()
final_choice = input("What will you do (1, 2)? ")

if final_choice == "2":
    print("You got knocked down. Game Over.")
    exit()
else:
    print("You choose to knock her down and run.")
print()

print("You want to feel bad about hurting her,"
      "\nbut that moment is short lived and you rush to the door."
      "\nWith shaking hands, you place the crown on your head and the door opens."
      "\nWith a deep breath, you close your eyes and enter")

print()
print("When you open them, you find yourself in a massive throne room."
      "\nInside is a dark figure. As it comes into the light,"
      "\nyou realize with a surge of fear that this is the Goblin King."
      "\nYou somehow know that he has been waiting for you this entire time.")

print()
print("You will have to defeat him to continue.")
print()
print("Goblin King")
Ascii_Art.Goblin_King()
print()

bullet = 10
print(f"1: Use your gun. {bullet} bullets")
print("2: Throw your hat at him.")
print("3: Jump at him an knock him into a pit.")
attack_goblin = input("What do you want to do (1, 2, 3)? ")


if attack_goblin == "1":
    print(f"You choose option {attack_goblin}")
    print("You used your gun an defeated the Goblin King")

elif attack_goblin == "2":
    print(f"You choose option {attack_goblin}")
    print("You threw your hat at him.")
    print("It was secretly a bomb and the Goblin King blows up.")

elif attack_goblin == "3":
    print(f"You choose option {attack_goblin}")
    print("You knock him into the pit.")
    print("He has fallen and can't get up.")

else:
    print("You failed to choose correctly.")
    Ascii_Art.defeat()

print("You Win!!!")
Ascii_Art.victory()
