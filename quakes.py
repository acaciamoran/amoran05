# Name:         Acacia Moran
# Course:       CPE 101
# Instructor:   Nupur Garg
# Assignment:   Project 5
# Term:         Spring 2017

from quake_funcs import *
import quakes
import quake_funcs

def main():
    filename = 'quakes.txt'
    quakes = read_file(filename)
    quakes_filtered = read_file(filename)
    choice = 'a'
    while choice != 'q':
        choice = printing_function(quakes_filtered)
        if choice == 'f':
             quakes_filtered = filter_quakes(quakes)
        elif choice == 's':
            quakes_filtered = sort(quakes)
        elif choice == 'n':
            quakes_dict = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
            features = quakes_dict["features"]
            list_of_new_quakes = []
            for feature in features:
                new_earthquake = quake_from_feature(feature)
                if new_earthquake not in quakes:
                    list_of_new_quakes.append(new_earthquake)
            if len(list_of_new_quakes) != 0:
                print("\nNew quakes found!!!\n")
                for quake in list_of_new_quakes:
                    quakes.append(quake)
                quakes_filtered = quakes
        else:
            choice = choice
        write_file('quakes.txt', quakes_filtered)
    return None




        


if __name__ == '__main__':
    main()
