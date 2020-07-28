# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 2
# Term:         Spring 2017
from lander_funcs import *


def main():
    show_welcome()
    altitude = get_altitude()
    fuel_amount = get_fuel()
    velocity = 0
    fuel_rate = 0
    print("\nLM state at retrorocket cutoff")
    elapsed_time = 0
    display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate)
    print("")
 
    while fuel_amount > 0:
        fuel_rate = get_fuel_rate(fuel_amount)
        elapsed_time = elapsed_time + 1
        fuel_amount = update_fuel(fuel_amount, fuel_rate)
        gravity = float(1.62)
        acceleration = update_acceleration(gravity, fuel_rate)
        altitude = update_altitude(altitude, velocity, acceleration)
        velocity = update_velocity(velocity, acceleration)
        if altitude < 0:
            break
        if fuel_amount > 0:
            display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate)
            print("")
    while altitude > 0:
        print("OUT OF FUEL - Elapsed Time:{0:4d} Altitude:{1:8.2f} Velocity:{2:8.2f}".format(elapsed_time, altitude, velocity))
        elapsed_time = elapsed_time + 1
        fuel_rate = 0
        acceleration = update_acceleration(gravity, fuel_rate)
        altitude = update_altitude(altitude, velocity, acceleration)
        velocity = update_velocity(velocity, acceleration)
    altitude = 0
    print("\nLM state at landing/impact")
    display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate) 
    print ("")
    display_LM_landing_status(velocity)




























if __name__ =="__main__":
    main()
