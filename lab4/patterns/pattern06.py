import driver

def letter(row, col):
    if ((row == 0 and col == 0) or (row == 0 and col == 6)):
        return 'X'
    elif ((row == 1 and col == 1) or (row == 1 and col == 5)):
        return 'X'
    elif ((row == 2 and col == 2) or (row == 2 and col == 4)):
        return 'X'
    elif ((row == 3 and col == 3) or (row == 3 and col == 3)):
        return 'X'
    elif ((row == 4 and col == 4) or (row == 4 and col == 2)):
        return 'X'
    elif ((row == 5 and col == 5) or (row == 5 and col == 1)):
        return 'X'
    elif ((row == 6 and col == 6) or (row == 6 and col == 0)):
        return 'X'
    else:
        return 'O'


if __name__ == '__main__':
    driver.compare_patterns(letter)
