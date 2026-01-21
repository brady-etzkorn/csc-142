import random

# Move a card from deck to hand

def draw_card(hand, deck):

    hand.append(deck.pop())  # take last card from deck

def hand_value(hand):
    total = 0
    aces = 0

    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        elif card == 'A':
            aces += 1
            total += 11
        else:
            total += int(card)
    
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    
    return total


 

def main():

    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    player_hand = []

    dealer_hand = []

    random.shuffle(deck)

    # Draw two cards to the players hand

    draw_card(player_hand, deck)
    draw_card(player_hand, deck)

    print("Player hand:", player_hand)

    draw_card(dealer_hand, deck)
    print("Dealer hand:", dealer_hand)

    while True:
        decide = input("Do you want to hit or stand?")
        if decide.lower() == 'hit':
            draw_card(player_hand, deck)
            print("You drew:", player_hand[-1])
            print("Your hand:", player_hand)
            print("Value:", hand_value(player_hand))
            
            if hand_value(player_hand) > 21:
                print("You lose!")
                player_busted = True
                break

        elif decide.lower() == 'stand':
            print("You are standing.")
            player_busted = False
            break

    
    if not player_busted:
        print("Dealer's hand value:", hand_value(dealer_hand))
        
        while hand_value(dealer_hand) < 17:
             draw_card(dealer_hand, deck) 
             print("Dealer drew:", dealer_hand[-1])
             print("Dealer hand:", dealer_hand)
    
    # Time to check the results 
        print("Player hand:", hand_value(player_hand))
        print("Dealer hand:", hand_value(dealer_hand))

        if hand_value(dealer_hand) > 21:
            print("Dealer Busts! You Win!")
        elif hand_value(dealer_hand) < hand_value(player_hand):
            print("You Win!")
        elif hand_value(dealer_hand) > hand_value(player_hand):
            print("You Lose!")
        elif hand_value(dealer_hand) == hand_value(player_hand):
            print("Push, you have the same value.")


        


    
    

    ...

    # more stuff here; draw starting cards and start the game loop

 

if __name__ == "__main__":

    main()