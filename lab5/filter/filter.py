def are_positive(nums):
    positive = []
    index = 0
    while   index < len(nums):
        if nums[index] > 0:
            positive.append(nums[index])
        index +=1
    return positive

def are_greater_than_n(nums, value):
    greater = []
    for num in nums:
        if num > value:
            greater.append(num)
    return greater


def are_divisible_by_n(nums, value):
    return [num for num in nums if num % value == 0]
