# Name: Acacia Moran
# Course: CPE 101
# Instructor: Nupur Garg
# Assignment: Project 2
# Term: Spring 2017


from lander_funcs import *


def main():
    show_welcome()
    get_altitude()
    get_fuel()
    display_LM_state(12, 1034.278, -54.3333, 486, 7)
    
    # Call twice to test with requesting too much fuel.
    rate = get_fuel_rate(45)
    print('rate:', rate)
    rate = get_fuel_rate(4)
    print('rate:', rate)
    
    # Call three times to display each possible comment.
    display_LM_landing_status(-.2)
    display_LM_landing_status(-9)
    display_LM_landing_status(-19)


if __name__ == '__main__':
    main()

