# Binary search algorithm

def binary_search(list, target):
    first = 0
    last = len(list) - 1 # How you get the last index of the list

    while first <= last: 
        midpoint = (first + last)//2 # // is floor division,

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index:",index + 1)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10] # This will not work if not in numerical order

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 6)
verify(result)

