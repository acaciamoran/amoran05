def square_all(nums):
    squares = []
    for num in nums:
        squares.append(num * num)
    return squares

def add_n_all(nums, value):
    add = []
    index = 0
    while len(add) < len(nums) :
        add.append(nums[index] + value)
        index += 1
    return add



def even_or_odd_all(nums):
    return [num % 2 == 0 for num in nums]
