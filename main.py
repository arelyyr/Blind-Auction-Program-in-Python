# Importing necessary libraries
from replit import clear  # Importing clear function from replit module
from art import logo  # Importing logo from art module

# Displaying the logo
print(logo)

# Initializing an empty dictionary to store bids and a flag for bidding completion
bids = {}
bidding_finished = False

# Function to find the highest bidder
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

# Bidding process loop
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: $"))
  bids[name] = price  # Storing the bid in the bids dictionary
  should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")

  if should_continue == "no":  # If no more bidders, determine the winner
    bidding_finished = True
    find_highest_bidder(bids)  # Calling function to find the highest bidder
  elif should_continue == "yes":  # If there are more bidders, continue
    clear()  # Clearing the console for the next bidder