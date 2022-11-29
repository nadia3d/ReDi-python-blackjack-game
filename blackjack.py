from random import shuffle

def create_deck():
  card_families = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
  card_values = ['Ace', '2','3','4','5','6','7','8','9','10','J','Q','K']
  deck = []
  for family in card_families:
    for value in card_values:
      deck.append(f'{value} of {family}')
  shuffle(deck)
  return deck

def deal_card(deck):
  card = deck.pop()
  return card

def value_of_card(card):
  firstAlphabet = card[0]
  if firstAlphabet in ['J', 'Q', 'K', '1']:
    return 10
  elif firstAlphabet == 'A':
    
    # ask the user if it is 1 or 11
    pass
  else:
    return int(firstAlphabet)

def sum_of_cards(listOfCards):
  return sum(listOfCards)


# create the deck
deck = create_deck()

playerCards = []
dealerCards = []

goOn = True


for card in range(2):
  card_for_player = deal_card(deck)
  playerCards.append(value_of_card(card_for_player))
  card_for_dealer = deal_card(deck)
  dealerCards.append(value_of_card(card_for_dealer))

while goOn:

  if sum_of_cards(playerCards) <= 16:
    # ask hit or stand
    playerInput = input("Hey player! Hit or stand? (h/s)  ").lower()
    if playerInput == 'h': # hit
      card = deal_card(deck)
      playerCards.append(card)
    elif playerInput == 's':
      
      user_score = sum_of_cards(playerCards)
      dealer_score = sum_of_cards(dealerCards)

      if user_score > dealer_score:
        print(f'Your score is:  {user_score} Congratulations! You won!')
      else:
        print(f'Your score is:  {user_score} You have lost.')
        break
