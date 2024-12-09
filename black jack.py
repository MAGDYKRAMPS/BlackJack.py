import random

deck = {
    'Ace': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
}

def draw_card():
   
    return random.choice(list(deck.keys()))

def calculate_total(hand):
    
    total = sum(deck[card] for card in hand)
    # Check if the hand contains an Ace and adding 10 if the total is 11 or less
    if 'Ace' in hand and total + 10 <= 21:
        total += 10
    return total

def play_blackjack():
   
    # Initial deal
    player_hand = [draw_card(), draw_card()]
    dealer_hand = [draw_card(), draw_card()]
    
    while True:
        # Calculate and display player's total
        player_total = calculate_total(player_hand)
        print("Player's cards:", player_hand)
        print("Player's total:", player_total)
        
        # Check if player has bust
        if player_total > 21:
            print("Player busts. Sorry You Lost!")
            return
        
        # Ask player for their move
        choice = input("Do you want to hit or stand? ").lower()
        
        if choice == "hit":
            # Draw a new card for the player
            player_hand.append(draw_card())
        elif choice == "stand":
            # Player has chosen to stand, dealer's turn
            break
        else:
            print("Please try again.")
    
    # Dealer's turn
    while calculate_total(dealer_hand) < 17:
        dealer_hand.append(draw_card())
    
    # Calculate and display dealer's total
    dealer_total = calculate_total(dealer_hand)
    print("\nDealer's cards:", dealer_hand)
    print("Dealer's total:", dealer_total)
    
    # Check if dealer has bust
    if dealer_total > 21:
        print("Dealer busts. You win!")
    elif dealer_total > player_total:
        print("HURRAY..YOU WON!")
    elif dealer_total < player_total:
        print("CONGRATULATION...!")
    else:
        print("OOOPS IT'S A TIE, TRY AGAIN!")
    

# Start the game
play_blackjack()

