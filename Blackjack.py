#Blackjack game (Made it myself from previous class)
def black_jack():
  dealer = []
  player = []

  #Lists

  #Variables
  player_card_total = 0
  dealer_card_total = 0

  def get_random_card():
    """
    Gets a random card
    Arguments:
        None
    Returns:
        The card
    """
    number = random.randint(2, 11)
    house = random.choice(["Hearts", "Spades", "Clubs", "Diamonds"])
    card = number, "of", house
    return card

  #Print cards
  def print_cards(hand, face_cards):
    """
    prints the card
    Arguments:
        The hand and also if there are face cards (Jack, Queen, or King) then it uses that
    Returns:
        None
    """
    for row in hand:
      print(" ")
      for col in row:
        if col == 11:
          col = "Ace"
        elif col == 10:
          col = face_cards
        print(col, end=" ")
    print("\n")

  jack_queen_king = random.choice(["Jack", "Queen", "King"])

  #Checks for blackjack
  def check_win(card_total):
    """
    Checks if you have won
    Arguments:
        Cards total
    Returns:
        True if card total = 21
    """
    if card_total == 21:
      return True

  def check_bust(card_total):
    """
    Checks bust (Lost)
    Arguments:
        Cards total
    Returns:
        True if card total > 21
    """
    if card_total > 21:
      return True


#Shows value card and description if player doesn't know how to play blackjack

  cards = [
      "Ace |", "2 |", "3 |", "4 |", "5 |", "6 |", "7 |", "8 |", "9 |", "10 |",
      "Jack |", "Queen |", "King |"
  ]
  values = [
      "1 or 11", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"
  ]

  knowledge = input("Do you know how to play BlackJack?: ").lower()
  if knowledge == "no":
    clear()
    print(
        "In blackjack, the player's goal is to have a hand with value closer to 21 than the dealer's without exceeding 21 or by the dealer's hand going over 21. Value of cards are also different. \n\nCard Values are as follows: \n"
    )
    for cards, values in zip(cards, values):
      print(cards, values)
    exit = input("\nWhen ready, press enter to start playing. ")
    if exit == "":
      clear()

  clear()

  #Gives dealer cards and put in list
  while len(dealer) < 1:
    dealer.insert(0, get_random_card())

  print("Hobo's cards:")
  print_cards(dealer, jack_queen_king)

  dealer_card_total += dealer[-1][0]

  #Gives players cards and put in list
  while len(player) < 2:
    player.insert(0, get_random_card())

  print("Your cards: ")
  print_cards(player, jack_queen_king)

  #Adds total of player
  player_card_total += player[0][0] + player[1][0]
  if check_win(player_card_total):
    print("BlackJack! You win!")

  #Only allows the ace to use be used only once
  uses = 0

  #Hit or stand, if hit then loops back unless the player wins or loses, else if stand, then breaks loop
  while True:
    if check_bust(player_card_total) and ((11 in player[0]) or
                                          (11 in player[1]) or
                                          (11 in player[2])) and uses == 0:
      player_card_total = player_card_total - 10
      uses += 1
    if check_win(player_card_total) or check_bust(player_card_total):
      clear()
      break
    else:
      hit_or_stand = input("Hit or Stand?: ")
      if hit_or_stand.lower() == "hit":
        player.append(get_random_card())
        player_card_total += player[-1][0]
        clear()
        print("Hobo's cards: ")
        print_cards(dealer, jack_queen_king)
        print("Your cards: ")
        print_cards(player, jack_queen_king)
      elif hit_or_stand.lower() == "stand":
        clear()
        break

  #Dealer's turn
  while dealer_card_total < 17 and player_card_total < 21:
    dealer.append(get_random_card())
    dealer_card_total += dealer[-1][0]
    if dealer_card_total > 21 and ((11 in dealer[0]) or
                                   (11 in dealer[1])) and uses == 0:
      dealer_card_total = dealer_card_total - 10
      uses += 1

  print("Hobo's cards:")
  print_cards(dealer, jack_queen_king)

  print("Your cards:")
  print_cards(player, jack_queen_king)

  #Prints out results of game
  if player_card_total < dealer_card_total and (
      not check_bust(dealer_card_total)) or check_bust(player_card_total):
    return False
  elif player_card_total > dealer_card_total and (
      not check_bust(player_card_total)) or check_bust(dealer_card_total):
    return True
  elif player_card_total == dealer_card_total:
    print("You tied!")
