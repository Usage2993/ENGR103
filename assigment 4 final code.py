#######################################################################
# Program Filename: population_growth_simulator.py
# Author: Alexander Vogs
# Date: May 2025
# Description: This program simulates population growth using both geometric and logistic models over 100 time steps
# Input: User inputs for birth rate, death rate, carrying capacity, and initial population
# Output: Population values at every 10 time steps for each model
#######################################################################

# Function: validate_float_input
# Description: Gets and validates a float input between a min and max value
# Parameters: prompt (str), min_val (float), max_val (float)
# Return values: float
# Pre-Conditions: User must enter a number in the valid range
# Post-Conditions: Returns a valid float
def validate_float_input(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print("Error: value must be between", min_val, "and", max_val)
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function: validate_positive_int_input
# Description: Gets and validates a positive integer input
# Parameters: prompt (str)
# Return values: int
# Pre-Conditions: User must enter a positive integer
# Post-Conditions: Returns a valid integer
def validate_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: value must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")


# Function: simulate_population
# Description: Runs a 100-step population simulation
# Parameters: r (float), K (int), initial_pop (int), model_type (str)
# Return values: list of tuples (time_step, population)
# Pre-Conditions: r is a valid growth rate, model_type must be 'geometric' or 'logistic'
# Post-Conditions: Returns population values every 10 steps
def simulate_population(r, K, initial_pop, model_type):
    population = initial_pop
    results = []

    for step in range(1, 101):
        if model_type == "geometric":
            population += r * population
        elif model_type == "logistic":
            population += r * (1 - population / K) * population

        if population < 0:
            population = 0  # Prevent negative population

        if step % 10 == 0:
            results.append((step, population))

    return results


# Function: main
# Description: Collects input, runs simulations, and prints output
# Parameters: None
# Return values: None
# Pre-Conditions: User runs the program and provides valid input
# Post-Conditions: Prints population values at every 10 steps
def main():
    print("Population Growth Simulation\n")

    birth_rate = validate_float_input("Enter birth rate (0-1): ", 0.0, 1.0)
    death_rate = validate_float_input("Enter death rate (0-1): ", 0.0, 1.0)
    carrying_capacity = validate_positive_int_input("Enter carrying capacity: ")
    initial_population = validate_positive_int_input("Enter initial population: ")

    r = birth_rate - death_rate

    geometric_results = simulate_population(r, carrying_capacity, initial_population, "geometric")
    logistic_results = simulate_population(r, carrying_capacity, initial_population, "logistic")

    print("\nGeometric and Logistic Growth Results:\n")
    for geo, log in zip(geometric_results, logistic_results):
        print(f"At time step {geo[0]}:")
        print(f"  Geometric model population = {geo[1]:.2f}")
        print(f"  Logistic model population  = {log[1]:.2f}")
        print()

main()
