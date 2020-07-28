# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 6
# Term:         Spring 2017
import sys
import math

def main():
    command_line = sys.argv
    try:
        fp = open(command_line[1], 'r')
        row = command_line[2]
        column = command_line[3]
        radius = command_line[4]
    except IOError:
        print("Unable to open {0}".format(command_line[1]))
        return None
    except IndexError:
        print("Usage: python3 fade.py <image> <row> <column> <radius>")
        return None
    file_name = command_line[1]
    read_ppm(fp, command_line, row, column, radius)
    fp.close()
def groups_of_three(line):
    return [line[i:i+3] for i in range(0, len(line), 3)]

def read_ppm(fp, file_name, row, column, radius):
    remainder = []
    fade_file = open("faded.ppm", 'w')
    line = fp.readline()
    fade_file.write(line)
    line_two = fp.readline()
    fade_file.write(line_two)
    line_three = fp.readline()
    fade_file.write(line_three)
    value = 0
    for line in fp:
        string_remainder = " ".join(remainder)
        pixel = string_remainder + " " + line
        pixel = pixel.split()
        pixel_list = groups_of_three(pixel)
        if len(pixel_list[-1]) < 3:
            remainder = pixel_list[-1]
        else:
            remainder = []
        for one_group_of_three in pixel_list:
            if len(one_group_of_three) == 3:
                value += 1
                red = int(one_group_of_three[0])
                green = int(one_group_of_three[1])
                blue = int(one_group_of_three[2])
                one_group_of_three = [red, green, blue]
                stripped = line_two.strip()
                list_size = stripped.split()
                faded_pixel = fade(one_group_of_three, row, column, radius, list_size, value)
                write_function(fade_file, faded_pixel)
    
    fade_file.close()
def fade(one_group_of_three, row, column, radius, list_size, value):
    list_of_row_column = get_column_row(list_size, value)
    myrow = list_of_row_column[0]
    mycolumn = list_of_row_column[1]
    dist_x = int(row) - int(myrow)
    dist_y = int(column) - int(mycolumn)
    distance = math.sqrt((dist_x **2) + (dist_y ** 2))
    scale = (int(radius) - int(distance)) / int(radius)
    if scale < .20:
        scale = .20
    red = scale * one_group_of_three[0]
    green = scale * one_group_of_three[1]
    blue = scale * one_group_of_three[2]

    faded_pixel = [int(red), int(green), int(blue)]
    return faded_pixel
def get_column_row(list_size, value):
    width = list_size[0]
    height = list_size[1]
    row = int(value - 1) // int(width)
    column = int(value - 1) % int(width)
    return [row, column]
    



def write_function(filename, one_group_of_three):
    string = "{0} {1} {2}\n".format(one_group_of_three[0],one_group_of_three[1], one_group_of_three[2])
    filename.write(string)
        
if __name__ == '__main__':
        main()


