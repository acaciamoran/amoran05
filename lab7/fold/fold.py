
def sum(list1):
    total = 0
    for i in range(len(list1)):
        total += list1[i]
    return total

def index_of_smallest(list1):
    if len(list1) == 0:
        return -1
    else:
        smallest = list1[0]
        smallest_index = 0
        for i in range(1, len(list1)):
            if list1[i] < smallest:
                smallest_index = i
                smallest = list1[i]
        return smallest_index 
                


