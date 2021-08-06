#from replit import clear
#HINT: You can call clear() to clear the output in the console.
#from art import logo
# import only system from os
from os import system, name
  
# define our clear function
def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


#print(logo)
other_bidders = True
bids_placed = {}
while other_bidders:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))
    bids_placed = {name: bid}
    bidders = input('Are there any other bidders? (y/n) ')
    if bidders == 'n':
        other_bidders = False
    clear()
highest_bidder = ""
highest_bid = 0
for person in bids_placed:
    bid_amount = bids_placed[person]
    if bid_amount > highest_bid:
        highest_bidder = person
        highest_bid = bid_amount
winner= [highest_bidder, highest_bid]
print(f"The winner of the auction was {winner[0]} at ${winner[1]}")