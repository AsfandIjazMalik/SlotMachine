import random

# Constants for game settings
MAX_LINES = 3  # Maximum number of lines a player can bet on
MIN_BET = 500  # Minimum allowed bet per line
MAX_BET = 50000  # Maximum allowed bet per line
global_balance = 0  # Player's balance
total_earnings = 0  # Tracks total winnings
total_losses = 0  # Tracks total losses

# Display the welcome message
print('********************************************\n'
      '\tWELCOME TO THE Royal Jackpot Slots\n'
      '********************************************\n')

# Function to display the game rules
def display_game_rules():
    """
    Displays the rules and guidelines of the Royal Jackpot Slots game.
    """
    print("\nGAME RULES:\n\n"
          f"1. You start with a balance of PKR 0 and can deposit money to play.\n"
          f"2. The minimum deposit is PKR {MIN_BET}.\n"
          f"3. You can bet on 1 to {MAX_LINES} lines.\n"
          f"4. The bet per line must be between PKR {MIN_BET} and PKR {MAX_BET}.\n"
          "5. Each line will show 3 random symbols from a set (💛, 💘, 💚, 💙, 💜).\n"
          "6. Matching all 3 symbols on a line wins 3 times your bet for that line.\n"
          "7. Matching 2 symbols on a line wins 2 times your bet for that line.\n"
          "8. If no symbols match on a line, you lose 1.5 times your bet for that line.\n"
          "9. Your balance updates after each spin based on outcomes.\n"
          "10. Keep playing to increase your balance or stop whenever you want.\n")

# Main function for the slot machine game
def play_slot_machine():
    """
    Handles the main gameplay, including deposits, betting, spinning, 
    and updating player balances based on outcomes.
    """
    global global_balance, total_earnings, total_losses  # Access global variables

    # Allow the player to deposit money to start playing
    while True:
        deposit_amount = input(f"Enter the amount you want to deposit (minimum PKR {MIN_BET}): ")
        if deposit_amount.isdigit():
            deposit_amount = int(deposit_amount)
            if deposit_amount >= MIN_BET:
                global_balance += deposit_amount  # Add deposit to player's balance
                break
            else:
                print(f"Deposit amount must be at least PKR {MIN_BET}.\n")
        else:
            print("Please enter a valid numeric amount.\n")

    print(f"\nCurrent Balance: PKR {global_balance}")

    # Allow the player to choose the number of lines to bet on
    while True:
        lines_to_bet = input(f"How many lines would you like to bet on? (1-{MAX_LINES}): ")
        if lines_to_bet.isdigit():
            lines_to_bet = int(lines_to_bet)
            if 1 <= lines_to_bet <= MAX_LINES:
                break
            else:
                print(f"Please select a number between 1 and {MAX_LINES}.\n")
        else:
            print("Please enter a valid number.\n")

    # Allow the player to specify the bet amount per line
    while True:
        bet_per_line = input(f"Enter your bet amount per line (PKR {MIN_BET}-{MAX_BET}): ")
        if bet_per_line.isdigit():
            bet_per_line = int(bet_per_line)
            if MIN_BET <= bet_per_line <= MAX_BET:
                break
            else:
                print(f"Bet amount must be between PKR {MIN_BET} and PKR {MAX_BET}.\n")
        else:
            print("Please enter a valid numeric amount.\n")

    # Ensure sufficient balance for the bet
    total_bet = lines_to_bet * bet_per_line
    if total_bet > global_balance:
        print(f"Insufficient balance! You need at least PKR {total_bet} to place this bet.\n")
        return

    global_balance -= total_bet  # Deduct the total bet amount from the balance

    # Initialize symbols for the slot machine
    slot_symbols = ['💛', '💘', '💚', '💙', '💜']
    print("Spinning the slot machine...\n")

    line_results = []  # Stores results for each line

    # Spin and calculate outcomes for each bet line
    for line_number in range(1, lines_to_bet + 1):
        spin_result = [random.choice(slot_symbols) for _ in range(3)]  # Random symbols for the line
        print(f"Line {line_number}: {' '.join(spin_result)}")

        # Check the outcome for the line
        if spin_result[0] == spin_result[1] == spin_result[2]:
            winnings = bet_per_line * 3
            global_balance += winnings
            total_earnings += winnings
            line_results.append((line_number, "Win", winnings))
            print(f"Line {line_number}: All 3 symbols matched! You won PKR {winnings}.\n")
        elif spin_result[0] == spin_result[1] or spin_result[1] == spin_result[2] or spin_result[0] == spin_result[2]:
            winnings = bet_per_line * 2
            global_balance += winnings
            total_earnings += winnings
            line_results.append((line_number, "Win", winnings))
            print(f"Line {line_number}: 2 symbols matched! You won PKR {winnings}.\n")
        else:
            loss = int(bet_per_line * 1.5)
            global_balance -= loss
            total_losses += loss
            line_results.append((line_number, "Loss", loss))
            print(f"Line {line_number}: No symbols matched. You lost PKR {loss}.\n")

    # Display detailed results for each line
    print("\nLine Outcomes:")
    for result in line_results:
        line, outcome, amount = result
        print(f"Line {line}: {outcome} - {'WON' if outcome == 'Win' else 'LOST'} PKR {amount}")

    # Display game summary
    print(f"\nGame Summary:")
    print(f"Total Winnings: PKR {total_earnings}")
    print(f"Total Losses: PKR {total_losses}")
    print(f"Final Balance: PKR {global_balance}\n")

# Main menu for the game
while True:
    user_choice = input(
        "1. Press P to Play Royal Jackpot Slots (or press 1)\n"
        "2. Press R to Read Game Rules (or press 2)\n"
        "3. Press E to Exit the Game (or press 3)\n\n"
        "Enter your choice (P/R/E or 1/2/3): "
    ).lower()

    if user_choice in ['r', '2']:
        display_game_rules()
    elif user_choice in ['p', '1']:
        play_slot_machine()
    elif user_choice in ['e', '3']:
        print("You have exited the game. Thank you for playing Royal Jackpot Slots!")
        break
    else:
        print("Invalid input. Please choose a valid option.\n")