# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 6
# Term:         Spring 2017
import sys

def main():
    command_line = sys.argv
    try:
        fp = open(command_line[1], 'r')
    except IOError:
        print("Unable to open {0}".format(command_line[1]))
        return None
    except IndexError:
        print("Usage: python3 decode.py <image>")
        return None

    file_name = command_line[1]
    read_ppm(fp, command_line)


def groups_of_three(line):
    return [line[i:i+3] for i in range(0, len(line), 3)]

def read_ppm(fp, file_name):
    remainder = []
    file_p = open("decoded.ppm", 'w')
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
                red = int(one_group_of_three[0]) * 10
                if red > 255:
                    red = 255
                one_group_of_three = [red, red, red]
                write_function(file_p, one_group_of_three)
    fp.close()
    file_p.close()

def write_function(file_p, one_group_of_three):
    string = "{0} {1} {2}\n".format(one_group_of_three[0],one_group_of_three[1], one_group_of_three[2])
    file_p.write(string)
        
if __name__ == '__main__':
        main()

        
