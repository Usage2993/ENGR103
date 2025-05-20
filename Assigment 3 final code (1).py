# Blood Pressure Analyzer
# Author: Alexander Vogs
# Description: Calculates pulse pressure and mean arterial pressure from SP and DP values

# Function to calculate pulse pressure based on user entered systolic and diastolic pressures
# It returns the difference between systolic and diastolic values
def calculate_pulse_pressure(systolic, diastolic):
    return systolic - diastolic

# Function to evaluate the level of pulse pressure
# Prints whether the pulse pressure is high or normal based on the threshold of 80 mmHg
def evaluate_pulse_pressure(pp):
    if pp > 80:
        print(f"Your pulse pressure is high: {pp:.2f} mmHg")
    else:
        print(f"Your pulse pressure is normal: {pp:.2f} mmHg")

# Function to calculate the mean arterial pressure (MAP)
# It uses the formula MAP = DP + (1/3) * PP
def calculate_mean_arterial_pressure(diastolic, pulse_pressure):
    return diastolic + (1/3) * pulse_pressure

# Function to evaluate the mean arterial pressure result
# Informs the user if their MAP is within an acceptable range or too low
def evaluate_mean_arterial_pressure(map_value):
    print(f"Your mean arterial pressure is: {map_value:.2f} mmHg")
    if map_value < 60:
        print("You should seek medical assistance.")
    else:
        print("Your mean arterial pressure is within acceptable limits.")

# Main program function that collects input, validates data,
# performs calculations using the helper functions, and displays results
def main():
    try:
        sp_input = input("Enter your systolic pressure (mmHg): ")
        dp_input = input("Enter your diastolic pressure (mmHg): ")

        systolic = float(sp_input)
        diastolic = float(dp_input)

        if systolic <= 0 or diastolic <= 0:
            print("Invalid input. Pressures must be positive numbers.")
            return
        if systolic <= diastolic:
            print("Systolic pressure must be greater than diastolic pressure.")
            return

        pp = calculate_pulse_pressure(systolic, diastolic)
        evaluate_pulse_pressure(pp)

        map_value = calculate_mean_arterial_pressure(diastolic, pp)
        evaluate_mean_arterial_pressure(map_value)

    except ValueError:
        print("Invalid input. Please enter numeric values.")

main()
