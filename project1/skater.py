# Name:        Acacia Moran
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 1
# Term:       Spring 2017
from funcs import *

def main():
    
    pounds = (input("How much do you weigh (pounds)? "))
   
    mass_skater = pounds_to_kg(pounds)
    
    distance = float(input("How far away is your professor (meters)? "))
    
    which_object=input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? ")
    mass_object = get_mass_object(which_object)
    
    velocity_object = get_velocity_object(distance)

    skater_velocity = get_velocity_skater(mass_skater, mass_object, velocity_object)

    if mass_object<=0.1:
        print("\nNice throw! You're going to get an F!")
    elif mass_object > 0.1 and mass_object <= 1.0:
        print("\nNice throw! Make sure your professor is OK.")
    else:
        if distance<20:
            print("\nNice throw! How far away is the hospital?")
        elif distance>=20:
            print("\nNice throw! RIP professor.")

    print("Velocity of skater:", "{0:.3f}".format(skater_velocity), "m/s")
    if skater_velocity<.2:
        print("My grandmother skates faster than you!")
    elif skater_velocity>=0. and skater_velocity<1.0:
        print()
    elif skater_velocity>=1.0:
        print("Look out for that railing!!!")


if __name__ == "__main__":
    main()
