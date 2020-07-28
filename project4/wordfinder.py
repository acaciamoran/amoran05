# Name:         Acacia Moran
# Course:       CPE 101
# Instructor:   Nupur Garg
# Assignment:   Project 4
# Term:         Spring 2017

from finder_funcs import *

def main():
    puzzle_string = input()
    list_of_words = input()
    print("Puzzle:\n")
    list_of_puzzle = get_rows(puzzle_string)
    for characters in list_of_puzzle:
        print(characters)
    print("")
    list_words = list_of_words.split(" ")
    for index in range(len(list_words)):
        word = list_words[index]
        if wordsearch(puzzle_string, word) != None:
            (row, column, direction) = wordsearch(puzzle_string, word)
            print("{0}: ({1}) row: {2} column: {3}".format(word, direction, row, column))
        else:
            print("{0}: word not found".format(word))
    return None

if __name__ == '__main__':
    main()
