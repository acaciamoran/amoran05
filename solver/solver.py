# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 2
# Term:         Spring 2017
from solver_funcs import *


def get_cages():
    cage = []
    cages = []
    number_of_cages = input("Number of cages: ")
    for value in range(int(number_of_cages)):
        each_cage = input("Cage number {0}: ".format(value))
        cage_as_list = each_cage.split(" ")
        for i in range(len(cage_as_list)):
            cage.append(int(cage_as_list[i]))
        cages.append(cage)
        cage = []
    return cages


def main():
    cages = get_cages()
    puzzle = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
    row = 0
    column = 0
    backtrack = 0
    value = 0
    checks = 0
    while row < len(puzzle) and column < len(puzzle[0]):
        puzzle[row][column] += 1
        validity = check_valid(puzzle, cages)
        checks += 1
        if validity:
            if column == 4:
                row += 1
                column = 0
            else:
                column += 1
        else:
            value = puzzle[row][column]
            if value >= 5:
                while value == 5:
                    value = 0
                    puzzle[row][column] = value
                    if column == 0:
                        row -= 1
                        column = 4
                    else:
                        column -= 1
                    backtrack += 1
                    value = puzzle[row][column]
    print("\nSolution:\n")
    for i in range(len(puzzle)):
        list1 = puzzle[i]
        string1 = " ".join(str(a) for a in list1)
        print(string1 + " ")
    print("\nchecks: {0:3} backtracks: {1:2}".format(checks, backtrack))
    return None




if __name__ == '__main__':
   main()
