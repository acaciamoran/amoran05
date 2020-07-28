# Name:
# Course:
# Instructor:
# Assignment:
# Term:

def main():
    table_size = get_table_size()
    while table_size != 0:
        first = get_first()
        increment = get_increment()
        show_table(table_size, first, increment)
        table_size = get_table_size()

# Obtain a valid table size from the user.
def get_table_size():
    size = int(input("Enter number of rows in table (0 to end): "))

    while size < 0:
        print("Size must be non-negative.")
        size = int(input("Enter number of rows in table (0 to end): "))

    return size

# TODO: Enhancement 1 - Add input validation to this function.
# Obtain the first table entry from the user.
def get_first():
    first = int(input("Enter the value of the first number in the table: "))
    
    while first < 0:
        print("First must be non-negative.")
        first = int(input("Enter the value of the first number in the table: "))
    return first

# Display the table of cubes.
def show_table(size, first, increment):
    print("A cube table of size {:d} will appear here starting with {:d}.".format(size, first))
    print("Number  Cube")
    sum_of_cubes = 0
    while size > 0:
        print("{0:d}{1:10d}".format(first, first ** 3))
        size = size - 1
        sum_of_cubes = sum_of_cubes + (first ** 3)
        first = first + increment
    print("The sum of cubes is: {0}".format(sum_of_cubes))
    return 

    # TODO: Enhancement 2 - Insert loop here.
def get_increment():
    increment = int(input("Enter the increment between rows: "))
    
    while increment < 0:
        print("Increment must be non-negative.")
        increment = int(input("Enter the increment between rows: "))
    return increment

if __name__ == "__main__":
    main()
