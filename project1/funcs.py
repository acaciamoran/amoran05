# Name:        Acacia Moran
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 1
# Term:       Spring 2017
import math

def pounds_to_kg(pounds):

    kilograms = (float(pounds)* float(0.453592))

    return kilograms


def get_mass_object(obj):
   
    if obj == "t":
        return (0.1)
    
    elif obj == "p":
        return (1.0)
    
    elif obj == "r":
        return (3.0)
    
    elif obj == "g": 
        return (5.3)
   
    elif obj == "l":
        return (9.07)
    
    else:
        return (float(0.0))


def get_velocity_object(distance):
    
    velocity_object = math.sqrt((float(9.8)*float(distance))/float(2.0))
    
    return velocity_object


def get_velocity_skater(mass_skater, mass_object, velocity_object):

    velocity_skater = (float(mass_object)*float(velocity_object))/(float(mass_skater))
 
    return velocity_skater

