# Wind Turbine Power Calculator
# Author: Alexander Vogs
# Description: This program calculates the maximum and actual power output of a wind turbine
# based on wind speed, blade radius, and efficiency entered by the user.

def main():
    # Ask for inputs
    wind_speed = float(input("Enter wind speed (m/s): "))
    blade_radius = float(input("Enter blade radius (m): "))
    efficiency = float(input("Enter efficiency (0 to 100): "))

    # Constants
    pi = 3.14159265
    air_density = 1.2  # kg/m^3

    # Calculations
    area = pi * blade_radius * blade_radius  # m^2
    max_power = 0.5 * air_density * area * wind_speed * wind_speed * wind_speed  # Watts
    actual_power = (efficiency / 100) * max_power  # Watts
    max_power_kW = max_power / 1000 # Coverting max power to kW 
    actual_power_kW = actual_power / 1000 # Converting actual power to kW

    # Output results
    print("\n Wind Turbine Power Calculation")
    print("Wind Speed: " + str(wind_speed) + " m/s")
    print("Blade Radius: " + str(blade_radius) + " m")
    print("Efficiency: " + str(efficiency) + "%")
    print("Maximum Turbine Power: " + str(max_power) + " W")
    print("Actual Power Turbine: " + str(actual_power) + " W")
    print("- - - - - - - - - - - - - - - - - - - - -") # for output organization
    print("Maximum Turbine Power: " + str(max_power_kW) + " kW")
    print("Actual Power Turbine: " + str(actual_power_kW) + " kW")

main()