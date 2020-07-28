# Name:         Acacia Moran
# Course:       CPE 101
# Instructor:   Nupur Garg
# Assignment:   Project2
# Term:         Spring 2017

def show_welcome():
    print( "\nWelcome aboard the Lunar Module Flight Simulator\n"
           "\n   To begin you must specify the LM's initial altitude\n"
           "   and fuel level.  To simulate the actual LM use\n"
           "   values of 1300 meters and 500 liters, respectively.\n\n"
            "   Good luck and may the force be with you!\n")
    return ""
def get_altitude():
    altitude = float(input("Enter the initial altitude "
                    "of the LM (in meters): "))
    while  altitude >= 9999 or altitude <= 0:
        print("ERROR: Altitude must be between 1 and 9999,"
                " inclusive, please try again\n")
        altitude = float(input("Enter the initial altitude"
                            "of the LM (in meters): "))

    return altitude  

def get_fuel():
    fuel = int(input("Enter the initial amount of fuel on board "
                        "the LM (in liters): "))
    while fuel <= 0:
       print("ERROR: Amount of fuel must be positive, please try again\n")
       fuel = int(input("Enter the initial amount of fuel on board " 
                            "the LM (in liters): "))
    return fuel
    

   
def display_LM_state(elapsed_time, altitude, velocity, fuel_amount, fuel_rate):
    print("Elapsed Time: {0:4d}".format(elapsed_time), "s")
    print("        Fuel: {0:4d}".format(fuel_amount), "l")
    print("        Rate: {0:4d}".format(fuel_rate), "l/s")
    print("    Altitude: {0:7.2f}".format(altitude), "m")
    print("    Velocity: {0:7.2f}".format(velocity), "m/s")


def get_fuel_rate(current_fuel):
    fuel_rate = int(input("Enter fuel rate (0-9, 0=freefall, "
                    "5=constant velocity, 9=max thrust): "))
    if fuel_rate > current_fuel:
        fuel_rate = current_fuel
    while fuel_rate<0 or fuel_rate>9:
        print("ERROR: Fuel rate must be between 0 and 9, inclusive")
        fuel_rate = print(input("Enter fuel rate (0-9, 0=freefall, "
                    "5=constant velocity, 9=max thrust): "))
    return fuel_rate
 
def update_acceleration(gravity, fuel_rate):
    gravity = float(1.62)
    acceleration = (gravity) * ((fuel_rate/5) - 1)
    return float(acceleration)

	
def update_altitude(altitude, velocity, acceleration):
    altitude = (altitude + velocity + (acceleration/2))
    return altitude

def update_velocity(velocity, acceleration):
    velocity = (velocity + acceleration)
    return velocity

def update_fuel(fuel, fuel_rate):
    fuel = (fuel - fuel_rate)
    return fuel

def display_LM_landing_status(velocity):
    if velocity >= 0 or velocity >= -1:
        print("Status at landing - The eagle has landed!")
    elif velocity > -10:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("Status at landing - Ouch - that hurt!")



