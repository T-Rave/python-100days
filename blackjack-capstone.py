import random

# Gather human players and setup players dict. Deal two cards to start game
def game_setup():
    player_count = int(input("How many players?\n"))
    for player in range(player_count):
        player_name = input(f"Name of player {player + 1}: ")
        players[player_name] = {'cards_in_hand' : [],'card_total': 0, 'hit_status' : True}
    players['computer'] = {'cards_in_hand' : [],'card_total': 0, 'hit_status' : False}
    deal_deck()
    first_hand = 0
    while first_hand < 2:
        for player in players:
            deal(player)
        first_hand += 1

# Deal cards to players and dealer
def deal(player_name):
    dealt_card = random.choice(dealer_cards)
    players[player_name]['cards_in_hand'].append(dealt_card)
    dealer_cards.remove(dealt_card)
    print(players[player_name]['cards_in_hand'])
    card_total(player_name,royalty(player_name,dealt_card))
  
# Check if player has bust or not
def bust(player):
    if players[player]['card_total'] > 21:
        players[player]['hit_status'] = False
        return True
    else:
        return False
        
# calculate players hand total for int 
def card_total(player,add_card):
    global players
    players[player]['card_total'] += add_card
    
# take the count of cards in the deck and insert into a list that the "dealer" can deal from
def deal_deck():
    deck_count = int(input('Number of decks to play with: '))
    for card in decks:
        decks[card] *= deck_count
        for count in range(decks[card]):
            dealer_cards.append(card)
    random.shuffle(dealer_cards)

# Check for royal cards or Ace and appropriately convert to int value
def royalty(player_name,card):
    royal_cards = ['Jack', 'Queen', 'King']
    if card in royal_cards:
        return 10
    elif card == 'Ace':
        ace_choice = int(input(f"{player_name} have have been dealt an Ace. Would you like it to be a 1 or 11?\n"))
        return ace_choice
    else:
        return card

# Hit for the players
def player_hit(player_name):
    player_hand(player_name)
    if players[player_name]['hit_status'] == True:
        hit_choice = input('Would you like to hit? (y/n)\n')
        if hit_choice == 'y':
            deal(player_name)
            bust(player_name)
            print("finish yes hit")
            return
        elif hit_choice == 'n':
            players[player_name]['hit_status'] = False
            print("finish NO hit")
            return
    else:
        return
# hit for the dealer
def computer_hit():
    while players['computer']['card_total'] < 17:
        deal('computer')
        print(f"Dealer has: {players['computer']['cards_in_hand']}")
    return

# Deal until all players no longer want to hit
def continue_dealing():
    keep_dealing = True
    for player in players:
        if players[player]['hit_status'] == True:
            return True
        elif players[player]['hit_status'] == False:
            keep_dealing = False
    return keep_dealing

# Easily print the players hand
def player_hand(player_name):
    print(f"{player_name} you have: {players[player_name]['cards_in_hand']}\nCard total: {players[player_name]['card_total']}")

# Extract the players from the dealer in the players dict
def human_players():
    humans = []
    for player in players:
        if player != 'computer':
            humans.append(player)
    return humans

# calculate per player if they have won or not
def end_game():
    for player in human_players():
        player_total = int(players[player]['card_total'])
        dealer_total = int(players['computer']['card_total'])
        if bust(player):
            print(f'{player} bust with {player_total}. You lose!')
        elif dealer_total > 21:
            print("Dealer busts. You win!")
        elif player_total >= dealer_total:
            print(f"{player} you win with {player_total}.")
        else:
            print(f"{player} your {player_total} loses to the dealers {dealer_total}. ")

def game_play():
    # create players and decks to play from
    game_setup()
    # hit players
    keep_dealing = True
    while keep_dealing:
        for player in human_players():
            player_hit(player)
            bust(player)  
        keep_dealing = continue_dealing()
    # hit dealer
    computer_hit()
    # calculate winers
    end_game()

decks = {2 : 4,3 : 4,4 : 4,5 : 4, 6 : 4,7 : 4,8 : 4,9 : 4,10 : 4, 'Jack' : 4, 'Queen' : 4, 'King' : 4, 'Ace' : 4}
dealer_cards = []
card_totals = {}
players = {}


# start the game
game_play()
