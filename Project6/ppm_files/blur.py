# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 6
# Term:         Spring 2017
import sys
def main():
    command_line = sys.argv
    try:
        reach = command_line[2]
    except IndexError:
        reach = 4
    try:
        fp = open(command_line[1], 'r')
    except IOError:
        print("Unable to open {0}".format(command_line[1]))
        return None
    except IndexError:
        print("Usage: python3 blur.py <image> [<reach>]")
        return None
    file_p = open("blurred.ppm", 'w')
    file_name = command_line[1]
    read = read_file(fp, file_p)
    list_of_pixels = read[0]
    line_two = read[1]
    stripped = line_two.strip()
    list_size = stripped.split()
    grid = get_grid(list_of_pixels, list_size)
    row = 0
    column = 0
    for rowindex in range(len(grid)):
        for colindex in range(len(grid[rowindex])):
            pixel = grid[rowindex][colindex]
            list_of_pixel_needed = average_pixel(pixel, reach, grid, rowindex, colindex, list_size)
            total_red = 0
            total_green = 0
            total_blue = 0
            for pixel in list_of_pixel_needed:
                red = pixel[0]
                green = pixel[1]
                blue = pixel[2]
                total_red += int(red)
                total_green += int(green)
                total_blue += int(blue)
            avg_red = int(total_red) / int(len(list_of_pixel_needed))
            avg_green = int(total_green) / int(len(list_of_pixel_needed))
            avg_blue = int(total_blue) / int(len(list_of_pixel_needed))
            averaged_pixel= [int(avg_red), int(avg_green), int(avg_blue)]
            write_function(file_p, averaged_pixel)


def read_file(fp,file_p):
    remainder = []
    list_of_pixels = []
    line = fp.readline()
    file_p.write(line)
    line_two = fp.readline()
    file_p.write(line_two)
    line_three = fp.readline()
    file_p.write(line_three)
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
                list_of_pixels.append(one_group_of_three)
    return [list_of_pixels, line_two]

def average_pixel(pixel, reach, grid, rowindex, colindex, list_size):
    averaged = []
    for row in range((int(rowindex) - int(reach)), (int(rowindex) + int(reach) + 1)):
        for col in range((int(colindex) - int(reach)), (int(colindex) + int(reach) +1)):
            validity = out_of_bounds(row, col, list_size)
            if validity == True:
                pixel = grid[row][col]
                averaged.append(pixel)
    return averaged


def out_of_bounds(row, column, list_size):
    width = list_size[0]
    height = list_size[1]
    if int(row) <= int(height) - 1 and int(column) <= int(width) - 1:
        if int(row) >= 0 and int(column) >= 0:
            return True
    return False



def write_function(file_p, averaged_pixel):
    string = "{0} {1} {2}\n".format(int(averaged_pixel[0]),int(averaged_pixel[1]), int(averaged_pixel[2]))
    file_p.write(string)
def get_grid(list_of_pixels, line_two):
    width = line_two[0]
    height = line_two[1]
    row = []
    grid = []
    value = 0
    for pixel in list_of_pixels:
        row.append(pixel)
        value += 1
        if int(value) == int(width):
            grid.append(row)
            value = 0
            row = []
    return grid

def groups_of_three(line):
    return [line[i:i+3] for i in range(0, len(line), 3)]
if __name__ == '__main__':
        main()
