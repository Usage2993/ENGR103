#######################################################################
# Program Filename: planting_schedule.py
# Author: Alexander Vogs
# Date: June 2025
# Description: This program generates a planting schedule for a given
#              crop based on the start date, days to maturity, and a
#              frost deadline of October 1.
# Input: Crop name, start month, start day, days to maturity
# Output: A list of valid planting dates before the frost deadline
#######################################################################

# Constants
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 30, 30, 30]
FROST_MONTH = 10
FROST_DAY = 1
HARVEST_BUFFER = 14  # days for harvesting and soil prep

#######################################################################
# Function: get_valid_int
# Description: Prompts user until they enter a valid integer within a range
# Parameters: prompt (str), min_val (int), max_val (int)
# Return values: int - validated user input
# Pre-Conditions: min_val < max_val
# Post-Conditions: Returns a valid integer between min_val and max_val
#######################################################################
def get_valid_int(prompt, min_val, max_val):
    while True:
        try:
            value = int(input(prompt))
            if value < min_val or value > max_val:
                print(f"Enter a value between {min_val} and {max_val}.")
            else:
                return value
        except ValueError:
            print("Invalid input. Enter a whole number.")

#######################################################################
# Function: get_valid_day
# Description: Validates that the day entered is valid for the month
# Parameters: month (int)
# Return values: int - validated day input
# Pre-Conditions: month must be 1–12
# Post-Conditions: Returns a valid day in that month
#######################################################################
def get_valid_day(month):
    max_day = MONTH_DAYS[month - 1]
    return get_valid_int(f"Enter start day (1–{max_day}): ", 1, max_day)

#######################################################################
# Function: calculate_next_plant_date
# Description: Adds growth + harvest time to current date and returns next start date
# Parameters: month (int), day (int), total_days (int)
# Return values: (int, int) - next planting month and day
# Pre-Conditions: month and day must be valid
# Post-Conditions: Returns next valid planting date
#######################################################################
def calculate_next_plant_date(month, day, total_days):
    day += total_days
    while day > MONTH_DAYS[month - 1]:
        day -= MONTH_DAYS[month - 1]
        month += 1
        if month > 12:
            break
    return month, day

#######################################################################
# Function: before_frost
# Description: Checks if a date is before October 1
# Parameters: month (int), day (int)
# Return values: bool - True if before frost date
# Pre-Conditions: month and day must be valid
# Post-Conditions: Returns True if the planting date is acceptable
#######################################################################
def before_frost(month, day):
    if month < FROST_MONTH:
        return True
    elif month == FROST_MONTH and day < FROST_DAY:
        return True
    return False

#######################################################################
# Function: print_planting_schedule
# Description: Prints the final planting schedule
# Parameters: crop (str), months (list), days (list)
# Return values: None
# Pre-Conditions: Lists must be the same length
# Post-Conditions: Prints formatted schedule
#######################################################################
def print_planting_schedule(crop, months, days):
    print("\nPlanting Schedule for", crop)
    print("Planting Number\tMonth\tDay")
    for i in range(len(months)):
        print(f"{i+1}\t\t{months[i]}\t{days[i]}")

#######################################################################
# Main Program
#######################################################################
def main():
    crop_name = input("Enter crop name: ")

    start_month = get_valid_int("Enter start month (1–12): ", 1, 12)
    start_day = get_valid_day(start_month)
    days_to_mature = get_valid_int("Enter days to maturity: ", 1, 999)

    planting_months = []
    planting_days = []

    current_month = start_month
    current_day = start_day

    while before_frost(current_month, current_day):
        planting_months.append(current_month)
        planting_days.append(current_day)
        current_month, current_day = calculate_next_plant_date(
            current_month, current_day, days_to_mature + HARVEST_BUFFER)

    print_planting_schedule(crop_name, planting_months, planting_days)

main()
