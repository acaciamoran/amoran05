# Name:       Acacia Moran
# Course:     CPE 101
# Instructor: Nupur Garg
# Assignment: Project 1
# Term:       Spring 2017

def get_rows(puzzle_string):
    list_of_strings = []
    for i in range(10):
        start = i * 10
        end = (i+1) * 10
        row_string = get_row(puzzle_string, start, end)
        list_of_strings.append(row_string)
    return list_of_strings

        
def get_row(puzzle_string, start, end):
    string_of_values = ""
    for index in range(start, end):
        string_of_values += puzzle_string[index]
    return string_of_values

def get_columns(puzzle_string):
    columns = []
    for index in range(10):
        column = get_column(puzzle_string, index)
        columns.append(column)
    return columns




def get_column(puzzle_string, start):
    string_of_column = ""
    for index in range(start, len(puzzle_string), 10):
        string_of_column += puzzle_string[index]
    return string_of_column

def wordsearch(puzzle_string, word):

    if rows_check(puzzle_string, word) != None:
        (row, column, direction) = rows_check(puzzle_string, word)
        return (row, column, direction)
    if columns_check(puzzle_string, word) != None:
        (row, column, direction) = columns_check(puzzle_string, word)
        return (row, column, direction)
    return None

def row_check(word, row):
    validforward = row.find(word)
    validbackward = row.rfind(reverse_word(word))
    if validbackward != -1:
        validbackward += len(word) - 1
    return (validforward, validbackward)

def reverse_word(word):
        rev = []
        for idx in range(len(word)):
            final_idx = len(word) - idx - 1
            rev.append(word[final_idx])
        return ''.join(rev)

def rows_check(puzzle_string, word):
    rows = get_rows(puzzle_string)
    for index in range(len(rows)):
        (validforward, validbackward) = row_check(word, rows[index])
        if validforward != -1:
            return (index, validforward, 'FORWARD')
        if validbackward != -1:
            return (index, validbackward, 'BACKWARD')

def column_check(word, column):
    validdown = column.find(word)
    validup = column.rfind(reverse_word(word))
    if validup != -1:
        validup += len(word) - 1
    return (validdown, validup)

def columns_check(puzzle_string, word):
    columns = get_columns(puzzle_string)
    for index in range(len(columns)):
        (validdown, validup) = column_check(word, columns[index])
        if validdown != -1:
            return (validdown, index, 'DOWN')
        if validup != -1:
            return (validup, index, 'UP')




        


