from replit import clear
import art

print(art.logo)
print("Welcome to the secret auction program.")
name = input("What is your name? ")
bid = input("What's your bid? ")

bids = {}
bids[name] = bid

other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")

if other_bidders.lower() == "yes":
  while other_bidders.lower() == "yes":
    clear()
    name = input("What is your name? ")
    bid = input("What's your bid? ")
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")

clear()

biggest_bid = 0
bidder = ''

for key in bids:
  if int(bids[key][1::]) > biggest_bid:
    biggest_bid = int(bids[key][1::])
    bidder = key

print(f"The winner is {bidder.title()} with a bid of ${biggest_bid}")