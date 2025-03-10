import random
from collections import Counter

# Define the card ranks and suits
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Create a deck of cards
deck = [rank + ' of ' + suit for rank in ranks for suit in suits]

# Shuffle the deck
random.shuffle(deck)

# Deal two cards to each player
def deal_cards(deck, num_players=2):
    hands = {f'Player {i+1}': [deck.pop(), deck.pop()] for i in range(num_players)}
    return hands

# Deal the flop (three community cards)
def deal_flop(deck):
    return [deck.pop() for _ in range(3)]

# Deal the turn (one community card)
def deal_turn(deck):
    return deck.pop()

# Deal the river (one community card)
def deal_river(deck):
    return deck.pop()

# Function to evaluate hand strength (simplified version)
def evaluate_hand(hand, community_cards):
    all_cards = hand + community_cards
    rank_counts = Counter(card.split(' ')[0] for card in all_cards)
    most_common_rank, most_common_count = rank_counts.most_common(1)[0]
    return most_common_count

# Main function to simulate a Texas Hold'em game
def texas_holdem_game(num_players=2):
    # Shuffle the deck
    random.shuffle(deck)
    
    # Deal hands to players
    hands = deal_cards(deck, num_players)
    
    # Display hands
    print("Player Hands:")
    for player, hand in hands.items():
        print(f"{player}: {hand}")
    
    # Deal and display community cards in stages
    input("\nPress Enter to deal the Flop...")
    flop = deal_flop(deck)
    print(f"Flop: {flop}")
    
    input("Press Enter to deal the Turn...")
    turn = deal_turn(deck)
    print(f"Turn: {turn}")
    
    input("Press Enter to deal the River...")
    river = deal_river(deck)
    print(f"River: {river}")
    
    # Evaluate hands and determine winner
    community_cards = flop + [turn, river]
    hand_strengths = {player: evaluate_hand(hand, community_cards) for player, hand in hands.items()}
    
    winner = max(hand_strengths, key=hand_strengths.get)
    
    print(f"\nThe winner is {winner} with a hand strength of {hand_strengths[winner]}.")

# Run the game simulation with 2 players
texas_holdem_game(num_players=2)
