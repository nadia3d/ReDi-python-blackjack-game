# 52 cards (only 1 deck)
# 2 players - dealer & player (user)
# 4 card families - Hearts, Spades, Diamonds, Clubs
# card values - 2,3,4,5,6,7,8,9,10
# face cards - Ace, J, Q, K  -- J, Q, K == 10 && Ace could be 1 or 11



# dealer
# player (name of the player)
 
# rules of the game
# Ace could be 1 or 11

# create the deck
# for each card family, create a list of cards
# a loop that runs over 4 times (families), and assign it to a card value


# deal cards - 2 cards initially

# take the dealt cards out of the deck

# check the value of player's cards, sum up the cards
# if sum of dealer's card <= 16 -- dealer has to take one more card
# ask the player (hit or stand)
# while (sum of cards < 16)
  # if the player says hit and (sum of cards is less than/equal to 16):
    # deal one more card
    # remove that card from the deck
  # if the player says stand:
    # do nothing

# check if sum of cards is equal to 21
  # You Won Blackjack!!!

# check if player's hand is greater than 21 
  # player loses

# ask the player if he wants to show cards
  # sum of player's card VS sum of dealer's cards
  # compare which is closer to 21