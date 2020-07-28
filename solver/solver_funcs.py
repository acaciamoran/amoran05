# Name:         Acacia Moran
# Course:       CPE 101
# Instructure:  Nupur Garg
# Assignment:   Project 2
# Term:         Spring 2017

def check_valid(puzzle, cages):
    if check_cages_valid(puzzle, cages) == False:
        return False
    if check_columns_valid(puzzle) == False:
        return False
    if check_rows_valid(puzzle) == False:
        return False
    return True


def check_cages_valid(puzzle, cages):
    for i in range(len(cages)):
        cage = cages[i]
        if check_cage_valid(puzzle,cage) == False:
            return False
    return True
        
def check_cage_valid(puzzle, cage):
    total, zero = get_cage_value(puzzle, cage)
    if total != cage[0] and zero == 0:
        return False
    if total >= cage[0] and zero == 1:
        return False

    return True

def get_cage_value(puzzle, cage):
    value = 0
    zeros = 0
    for i in range(2, len(cage)):
        cell = cage[i]
        row = cell//len(puzzle[0])
        column = cell%len(puzzle[0])
        if puzzle[row][column] == 0:
            zeros = 1
        value += puzzle[row][column]
        
    return (value, zeros)



def check_columns_valid(puzzle):
    column_puzzle = column1(puzzle)
    for col in range(len(column_puzzle)):
        check_column_valid(column_puzzle[col])
        if check_column_valid(column_puzzle[col]) == False:
            return False
    return True

def check_column_valid(col):
    for index1 in range(len(col)):
        for index2 in range(len(col)):
            if  col[index1] == col[index2] and index1 != index2 and col[index1] != 0:
                return False
    return True


def column1(puzzle):
    column = []
    i = 0
    for i in range(5):
        column.append([row[i] for row in puzzle])
    return column




def check_rows_valid(puzzle):
    for row in range(len(puzzle)):
        check_row_valid(puzzle[row])
        if check_row_valid(puzzle[row]) == False:
            return False
    return True

def check_row_valid(row):
    for index1 in range(len(row)):
        for index2 in range(len(row)):
            if  row[index1] == row[index2] and index1 != index2 and row[index1] != 0:
                return False
    return True

            
