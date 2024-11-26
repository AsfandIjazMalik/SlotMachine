# Slot Machine
Python Programming 
# Royal Jackpot Slots - Slot Machine Game
Welcome to the **Royal Jackpot Slots**! This Python-based slot machine game lets players place bets, spin the reels, and track their winnings and losses in a fun and engaging way. The game simulates a classic slot machine experience where players can win or lose money based on randomly generated symbols. <br>
## Features:
- Players can deposit money to start playing. <br>
- The game allows betting on 1 to 3 lines. <br>
- Bet amounts can be customized within a set range. <br>
- The game features 3 random symbols: 💛, 💘, 💚, 💙, and 💜. <br>
- Players can win based on matching 2 or 3 symbols on a line. <br>
- Tracks total winnings, losses, and updates the player’s balance. <br>
## Python Concepts Used
This project demonstrates several Python programming concepts: <br>
### 1. **Variables and Constants**
   - **Global Variables**: `global_balance`, `total_earnings`, and `total_losses` track the player's current balance and total winnings or losses. <br>
   - **Constants**: `MAX_LINES`, `MIN_BET`, and `MAX_BET` define game settings that remain constant throughout the game. <br>
### 2. **Input and Validation**
   - **User Input**: The game prompts the user for deposit amounts, the number of lines to bet on, and the bet amount per line. <br>
   - **Input Validation**: Ensures that the user input is numeric and within the acceptable range (e.g., bet amount, number of lines). <br>
### 3. **Randomization**
   - **Random Module**: The game uses the `random.choice()` function to randomly select symbols for each line during the slot spin. <br>
### 4. **Loops and Iteration**
   - **While Loops**: Used for validating user input and ensuring valid deposit amounts, bet amounts, and number of lines. <br>
   - **For Loops**: Used to spin the slot machine for each line, generating three random symbols per line. <br>
### 5. **Conditional Statements**
   - **If-Else Statements**: Check the outcome of the slot machine spin (e.g., if all three symbols match, if two symbols match, or if there’s no match) and update the player's balance accordingly. <br>
### 6. **Functions**
   - **Modular Functions**: The game is broken into modular functions such as `display_game_rules()` to show the game rules, and `play_slot_machine()` to handle the main gameplay. <br>
### 7. **Global Scope**
   - **Global Variables**: The `global` keyword is used inside functions like `play_slot_machine()` to modify global variables such as `global_balance`, `total_earnings`, and `total_losses`.<br>
### 8. **String Manipulation**
   - **String Formatting**: The game uses f-strings to display dynamic information like balances, bet amounts, and game results in a user-friendly format. <br>
   - **String Joining**: Symbols for each line are combined using the `' '.join()` method to create readable outputs of the spin results. <br>
###Gameplay Instructions
1.	On starting the game, you will be prompted to deposit money. <br>
2.	After depositing, choose the number of lines to bet on (1-3). <br>
3.	Enter the bet amount per line within the specified limits. <br>
4.	Spin the slot machine to see if you win or lose. <br>
5.	The game will display your winnings or losses after each spin, and update your balance. <br>



# Royal Jackpot Slots - Gameplay Example<br><br>
********************************************<br>
    WELCOME TO THE Royal Jackpot Slots<br>
********************************************<br><br>
Menu Options: <br>
1. Press P to Play Royal Jackpot Slots (or press 1) <br>
2. Press R to Read Game Rules (or press 2) <br>
3. Press E to Exit the Game (or press 3) <br>
