#######################################################################
# Program Filename: climate_adventure_game.py
# Author: Alexander Vogs
# Date: June 2025
# Description: This program is a text-based adventure game based on
#              climate action. The user rolls a virtual die
#              to move through a list of climate events, gaining or losing
#              points. The goal is to reach the end of the list with a 
#              positive score and without hitting a game-ending event.
# Input: Pressing enter to roll the die.
# Output: Event messages, updated scores, and win/lose game status.
#######################################################################

import random

# Constants
START_SCORE = 20
MAX_DIE_ROLL = 6

# Climate-related events list
climate_events = [
    "You plant trees and gain 10 points!",
    "You start a recycling program and gain 5 points!",
    "A wildfire destroys resources. Lose 15 points.",
    "You build a solar farm. Gain 8 points!",
    "Flooding in your area. Lose 10 points.",
    "You organize a climate strike. Gain 6 points!",
    "A hurricane hits. Lose 12 points.",
    "You invent better insulation. Gain 7 points!",
    "You ignore rising sea levels. Lose 8 points.",
    "Community composting started. Gain 9 points!",
    "You face a heatwave. Lose 6 points.",
    "You install green roofs. Gain 4 points!",
    "Glacier melts and sea levels rise. Lose 9 points.",
    "You publish climate research. Gain 5 points!",
    "Carbon tax legislation fails. Lose 7 points.",
    "You retrofit buildings. Gain 10 points!",
    "You host a green tech conference. Gain 5 points!",
    "You cut funding to environmental programs. Lose 10 points.",
    "You support wind power. Gain 6 points!",
    "A drought reduces crop yield. Lose 5 points.",
    "You educate students on climate. Gain 8 points!",
    "Oil spill disaster. Game over.",
    "You help pass clean energy laws. Gain 7 points!",
    "Major ecosystem collapses. Lose 12 points.",
    "You reach net zero emissions. You win!"
]

#######################################################################
# Function: roll_die
# Description: Simulates a six-sided die roll.
# Parameters: None
# Return values: int - a number between 1 and 6
# Pre-Conditions: None
# Post-Conditions: Returns an integer for movement.
#######################################################################
def roll_die():
    return random.randint(1, MAX_DIE_ROLL)

#######################################################################
# Function: handle_event
# Description: Applies the effects of the climate event at the current
#              position on the user’s score and determines if the game ends.
# Parameters: position (int), score (int)
# Return values: tuple of updated score and game_over (bool)
# Pre-Conditions: position is within bounds of climate_events
# Post-Conditions: score is updated, game may end
#######################################################################
def handle_event(position, score):
    event = climate_events[position]
    print("\nYou landed on spot", position + 1, ":", event)

    if "gain" in event:
        points = int(event.split("gain")[1].split(" ")[1])
        score += points
    elif "Lose" in event:
        points = int(event.split("Lose")[1].split(" ")[1])
        score -= points
    elif "Game over" in event:
        print("You triggered a climate catastrophe. Game over!")
        return score, True
    elif "You win" in event:
        print("Congratulations! You successfully addressed climate action.")
        return score, True

    return score, False

#######################################################################
# Function: main
# Description: Runs the main game loop, manages position and score, and
#              controls user input and game termination.
# Parameters: None
# Return values: None
# Pre-Conditions: None
# Post-Conditions: Game ends with win or loss
#######################################################################
def main():
    print("Welcome to the Climate Action Adventure Game!")
    print("Your mission is to reach the end of the climate challenge list")
    print("without running out of points or triggering disaster.")

    position = 0
    score = START_SCORE
    game_over = False

    while not game_over:
        input("\nPress Enter to roll the die...")
        roll = roll_die()
        print("You rolled a", roll, "!")

        if position + roll < len(climate_events):
            position += roll
            score, game_over = handle_event(position, score)
            print("Current score:", score)

            if score <= 0:
                print("You've run out of points. Game over!")
                game_over = True
        else:
            print("Roll too high to land exactly on the last spot. Try again.")

# Start the program
if __name__ == "__main__":
    main()
