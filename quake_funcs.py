# Name:         Acacia Moran
# Course:       CPE 101
# Instructor:   Nupur Garg
# Assignment:   Project 5
# Term:         Spring 2017

from urllib.request import urlopen
from json import loads
from datetime import datetime
from operator import attrgetter


# GIVEN FUNCTIONS: Use these two as-is and do not change them
def get_json(url):
    """Function to get a JSON dictionary from a website.

    Args:
        url (str): The url from which to get the JSON

    Returns:
        A Python dictionary containing the information from the JSON object
    """
    with urlopen(url) as response:
        html = response.read()
    htmlstr = html.decode("utf-8")
    return loads(htmlstr)


def time_to_str(time):
    """Converts integer seconds since unix epoch to a string.

    Args:
        time (int): Unix time

    Returns:
        A nicely formated time string
    """
    return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

# TODO: Add Earthquake class definition here
class Earthquake:
    "A class to model a earthquake Attributes: place, mag, longitude, latitude, time"
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place.strip()
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __str__(self):
        return "({1:.2f}) {0:>40} at {4} ({2:8.3f}, {3:6.3f})".format(self.place, self.mag, self.longitude, self.latitude, time_to_str(self.time))

    def __eq__(self, other):
        return (self.place == other.place and self.mag == self.mag and self.longitude == other.longitude and self.latitude == other.latitude and self.time == self.time)

def read_file(filename):
    fp = open(filename, 'r')
    quakes = []
    for line in fp:
        earthquakelist = line.split(" ",4)
        quake = Earthquake(earthquakelist[4], float(earthquakelist[0]), float(earthquakelist[1]), float(earthquakelist[2]), int(earthquakelist[3]))
        quakes.append(quake)
    fp.close()
    return quakes
def write_file(filename, quakes_filtered):
    fp = open(filename, 'w')
    for line in quakes_filtered:
        string = earthquake_to_str(line)
        fp.write(string)
        fp.write("\n")
    fp.close()

def earthquake_to_str(earthquake):
    place = str(earthquake.place)
    time = str(earthquake.time)
    mag = str(earthquake.mag)
    latitude = str(earthquake.latitude)
    longitude = str(earthquake.longitude)
    list = [mag, longitude, latitude, time, place]
    string = " ".join(list)
    return string


# TODO: Required function - implement me!
def filter_by_mag(quakes, low, high):
    goodmagnitude = []
    for earthquake in quakes:
        if earthquake.mag >= low and earthquake.mag <= high:
            goodmagnitude.append(earthquake)
    return goodmagnitude




# TODO: Required function - implement me!
def filter_by_place(quakes, word):
    foundword = []
    for earthquake in quakes:
        place = earthquake.place
        lowercase_place = place.lower()
        lowercase_word = word.lower()
        if lowercase_place.find(lowercase_word) != -1:
            foundword.append(earthquake)
    return foundword

def sort(quakes):
        sorted_by = str(input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? "))
        print("")
        sorted_by = sorted_by.lower()
        if sorted_by == "m":
            quakes.sort(key = attrgetter("mag"), reverse = True)
        elif sorted_by == "t":
            quakes.sort(key = attrgetter("time"), reverse = True)
        elif sorted_by == "l":
            quakes.sort(key = attrgetter("longitude"))
        elif sorted_by == "a":
            quakes.sort(key = attrgetter("latitude"))
        return quakes

def filter_quakes(quakes):
    filterby = str(input("Filter by (m)agnitude or (p)lace? "))
    filterby = filterby.lower()
    if filterby == 'm':
        lower = float(input("Lower bound: "))
        upper = float(input("Upper bound: "))
        print("")
        quakes_by_mag = filter_by_mag(quakes, lower, upper)
        return quakes_by_mag
    elif filterby == 'p':
        word = str(input("Search for what string? "))
        print("")
        quakes_by_place = filter_by_place(quakes, word)
        return quakes_by_place

def printing_function(quakes_filtered):
    print("Earthquakes:")
    print("------------")
    for quake in quakes_filtered:
        print(quake)
    print("\nOptions:")
    print(" (s)ort")
    print(" (f)ilter")
    print(" (n)ew quakes")
    print(" (q)uit")
    choice = str(input("\nChoice: "))
    choice = choice.lower()
    return choice
# TODO: Required function for final part - implement me too!
def quake_from_feature(feature):
    place = feature["properties"]["place"]
    mag = feature["properties"]["mag"]
    time = feature["properties"]["time"]
    latitude = feature["geometry"]["coordinates"][0]
    longitude = feature["geometry"]["coordinates"][1]
    quake = Earthquake(place, float(mag), float(latitude), float(longitude), int((time)/1000))
    return quake


