Story Line:
(Black is story line, Red is user input, Blue is If Else statements)
In the heart of a sleepy town nestled amidst rolling hills, there stood an ancient toy factory, its weathered facade a testament to bygone days of childhood wonder. It was within the confines of this forgotten place that my journey began, waking up amidst a sea of discarded toys, the faint echoes of laughter still lingering in the air.
Off to the side you spy a dumpster. It may hold something valuable.
Do you want to search the dumpster?
If Yes:
You find a gun in the dumpster. How strange. You check it and see that it still has a full magazine of 10 bullets. You place the gun in your back pocket.
Add the gun to inventory.
If No:
A pity, you lost out on something cool for your future endeavors.

As you rubbed the sleep from your eyes, you found yourself drawn to three ornately carved doors standing sentinel at the far end of the factory floor. Each door seemed to hold a promise of adventure, beckoning you with whispered secrets and untold mysteries.

Door 1: You sense you have to defeat the f-eminists and fire breathing alligators. You will have to play blackjack with a bunch of hobos and then find the EIGHT FOOT MAN EATING BUNNY.

Door 2: You will discover an asylum and help some inmates escape. Then visit a restaurant, and use the bad food as a weapon. And finally blackmail a criminal mastermind with his family for a tommy gun.

Door 3: You are unsure of what is behind this door. It emits an ominous presence and you feel that it will be dangerous to continue.

Choose which door to enter:

Door 1 Storyline:
You find a group of fierce f-eminists threatening to disrupt the peace. They threaten to rip you to shreds for saying you don’t like women, but with your quick wit and strategic thinking, you navigate through their arguments, finding common ground and diffusing the tension peacefully.

Venturing into the untamed wilderness, you found yourself face to face with fire-breathing alligators guarding the path ahead. Undeterred, you square his shoulders and engage in a fierce battle of strength and agility. With cunning maneuvers and sheer determination, you emerge victorious, the fiery beasts vanquished.

You stumble upon a group of hobos engaged in a heated game of blackjack. Ever the opportunist, you join the game.

How much do you want to wager?

Blackjack WIN:
	# You win the amount you bet.
Blackjack LOSE:
	# You lose the amount you bet.

	if money == 50:
		print(“You have won the game”)
	else:
		bet = input(“How much do you want to wager? ”)
		random.randint() TO DECIDE IF THEY WIN OR LOSE
		if win:
			money += bet
			print(f”You made {bet} dollars”)
			print(f”Your total is {money}”)
		if lose:
			money += bet
			print(f”You lost {bet} dollars”)
			print(f”Your total is {money}”)

Continues until you have made 50 dollars or you lose all your money.
If you lose all your money it is game over.

Using your sharp mind to outwit your opponents and emerge victorious once more. With a handful of winnings in his pocket, you press on, your sights set on the ultimate prize. Finally, after overcoming countless obstacles and adversaries, you arrive at your destination: a hidden cave deep in the heart of the forest. Inside, you find the legendary eight-foot man-eating bunny, a creature of immense power and ferocity.

Door 2 Storyline:
After entering the door, you find yourself in a forest. After adventuring for a bit you come across an old asylum. Inside, you found a group of inmates, their eyes haunted by years of confinement. With compassion guiding your actions, you help them escape their prison, leading them through winding corridors and past locked doors until you emerge into the cool night air. You don’t know how they survived this long without food or water, but a voice inside you tells you not to question it.

Looking down you spy something hidden in a shadow. On the ground is a set of keys. You could have sworn that they were not there a second ago, but you choose to ignore the feeling. The keys feel mystical and call to you. You have a strange desire to pick them up.

Do you want to pick the key up?
if key is picked up:
	print(“You take the keys. They feel a bit comforting. Almost as they were a close friend, telling you that it was all right.”)
	Add keys to inventory.

else key is not picked up:
	print(“You leave the key on the ground. You are a bit disappointed in yourself, but something tells you you will need it later.”)
	print(“As you turn away, the keys suddenly appear in front of you. You stop and stare. ‘)

While loop:
If key is not in inventory:
	print(“You hear a voice telling you to pick the keys up. ”)
Do you want to pick the key up?
else if key is in inventory:
	continue


Hungry from your escape, you make your way to a nearby restaurant, its neon sign flickering in the darkness like a beacon of hope.

The door is locked. You realize you have a key

Do you want to use the key?
if true:
	(“The door opens and you go inside.”)
	.remove key from inventory.
If false:
	Loop back through and ask again.

You go inside and Yet, as you sample the food, your hopes are dashed by the taste of disappointment and despair. Anger rising within you, you know that you have to take action. You store the food in your inventory. Where did this come from?

With your rescued inmates in tow, you head to the light in the distance and discover a brightly lit, industrial building. Inside you come face to face with a mafia boss. With determination burning in your veins, you confronted him.

1: Use your secret weapon.
2: Use the terrible food you found.
What do you want to do?

If secret weapon:
	Check if gun in inventory
	if true:
		print(“Used gun to win. (3 Bullets used.)”)
Add map to inventory.
	If false:
		print(“You don’t have that”)
		print(“You now have to use the food”)

If food:
	print(“You forced the food down his mouth. It was so bad that he died.”)
	Add map to inventory.

After defeating the mafia boss, you find a map in your inventory. It is blank and leads to nowhere. Confused, you shrug, but still keep it.


After you complete all things in doors 1 or 2:

After continuing for sometime, you find yourself back in the toy factory, but something has changed. Now, only one door remains. Before you can check this out, you glimpse… something. Tucked away in the darkest corner of the factory, hidden from prying eyes, lay a single toy, a crown, untouched by the ravages of time.

With trembling hands, you reach out to grasp it, feeling a surge of warmth flood through you as you hold it close. In that moment, you understand the true power of toys – not simply as playthings, but as vessels of imagination and wonder, capable of transcending even the darkest of times.

But my moment of revelation was short-lived as I heard a sudden commotion behind me. Whirling around, I saw an old lady, her eyes blazing with fury. In a flash, she lunged towards me, intent on reclaiming what was hers.

1: Knock the lady down and run to the door.
2: Hesitate and get knocked unconscious by the old lady.
What do you do?

If hesitate:
print(“You got knocked down. Game Over.”)
exit()

If knock her down:
	print(“You chose to knock her down”)

You want to feel bad about hurting her, but that moment is short lived and you rush to the door. With shaking hands, you place the crown on your head and the door opens. With a deep breath, you close your eyes and enter

When you open them, you find yourself in a massive throne room. Inside is a dark figure. As it comes into the light, you realize with a surge of fear that this is the Goblin King. You somehow know that he has been waiting for you this entire time.
You come to the understanding that you will have to defeat him to continue.

1:
2:
3:
What do you want to do?
