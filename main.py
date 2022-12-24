# Initializes the empty bidding record dictionary
bidding_record = {}

# Used while loop to continue the program for as long as there are bidders to be added
while True:
    # Takes in user input
    name = input("What is your name?: ")
    price = input("What is your bid? $: ")
    # Forces user to type integer for price
    if price.isdigit():
        price = int(price)
        # Updates the bidding record dictionary with the name of the bidder and their bid
        bidding_record.update({name: price})
        morebidders = input("Are there any other bidders?(y/n)").lower()

        # Program will only break if user answers 'n' or 'no'
        if morebidders.startswith('n'):
            # Used built-in max function to determine the name of the user with the maximum bid!
            winner = max(bidding_record, key=bidding_record.get)
            max_bid = max(bidding_record.values())

            print(f"The winner of the auction is {winner} with a bid of {max_bid} dollars!")
            break
    else:
        print("Please type in a integer for your bid")
