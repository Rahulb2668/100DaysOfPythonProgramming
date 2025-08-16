from art import logo
import os
print(logo)

# TODO-1: Ask the user for input
bid_dict = {}

continue_bid = True

def find_final_bidder(final_dict):
    highest_bidder = ""
    highest_bid = 0
    for bidder, bid in final_dict.items():
        if bid > highest_bid:
            highest_bid = bid
            highest_bidder = bidder
    return highest_bidder, highest_bid


while continue_bid :
    bidder_name = input("Enter the name of the bidder")
    bidding_amount = int(input("Enter the bidding amount"))

# TODO-2: Save data into dictionary {name: price}
    bid_dict[bidder_name] = bidding_amount
# TODO-3: Whether if new bids need to be added

    continue_or_not = input("Are there any more bidder Yes or No").lower()

    if continue_or_not == "no":
        continue_bid= False
        bidder, bid = find_final_bidder(bid_dict)
        print(f"The bidding is won by {bidder} for {bid}")
    else:
        os.system('cls' if os.name == "nt" else "clear")

# TODO-4: Compare bids in dictionary


