import driver

def letter(row, col):
    if (row>col):
        return 'T'
    else:
        return 'W'
if __name__ == '__main__':
    driver.compare_patterns(letter)
