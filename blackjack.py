# Param Gattupalli
# COP 3502C Project 1: Blackjack

import random as rng


# Converts face cards' value to 10
def get_value(card_number):
    if card_number > 10:
        card_number = 10
    return card_number

# Generate player's card and prints it
def draw_card():
    deck = ['ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'JACK', 'QUEEN', 'KING']
    player_card = rng.randint(0, 13) + 1
    print(f'\nYour card is a {deck[player_card - 1]}!')
    return player_card

start_game, choice, game_number, player_wins, dealer_wins, ties, games_played  = True, 1, 1, 0, 0, 0, 0
# Executes until user selects exit option
while choice!=4:
    if start_game:
        print(f'START GAME #{game_number}')
        hand_value = 0
        choice = 1
    else:
        # Display menu and get user decision
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit\n")
        choice = int(input("Choose an option: "))

    if choice == 1:
        # Draw new card and add value to hand
        hand_value += get_value(draw_card())
        print(f'Your hand is: {hand_value}\n')

        # Display winning message if player wins
        if hand_value == 21:
            print("BLACKJACK! You win!\n")
            game_number += 1
            player_wins += 1
            games_played += 1
            start_game = True
        # Display losing message if player loses
        elif hand_value > 21:
            print("You exceeded 21! You lose.\n")
            game_number += 1
            dealer_wins += 1
            games_played += 1
            start_game = True
        else:
            start_game = False
    elif choice == 2:
        # Generate dealer's hand value
        dealer = rng.randint(0, 11) + 16
        print(f'\nDealer\'s hand: {dealer}')
        print(f'Your hand is: {hand_value}\n')

        # Print game's outcome
        if dealer < hand_value or dealer > 21:
            print("You win!\n")
            player_wins += 1
        elif dealer == hand_value:
            print("It's a tie! No one wins!\n")
            ties += 1
        elif dealer > hand_value:
            print("Dealer wins!\n")
            dealer_wins += 1
        games_played += 1
        game_number += 1
        start_game = True
    elif choice == 3:
        print("\nNumber of Player wins:", player_wins)
        print("Number of Dealer wins:", dealer_wins)
        print("Number of tie games:", ties)
        print("Total # of games played is:", games_played)
        print(f'Percentage of Player wins: {player_wins/games_played*100:.1f}%\n')
    elif choice == 4:
        exit()
    else:
        print("\nInvalid input!\nPlease enter an integer value between 1 and 4.\n")


