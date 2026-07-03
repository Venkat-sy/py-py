"""
Project 5: Binary Search Algorithm
External Requirements: None
"""
def binary_search(list, element):
    start, end = 0, len(list)
    steps = 0
    while start < end:
        print("Step", steps, ":", str(list[start:end]))
        steps += 1
        mid = (start + end) // 2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            start = mid + 1
        else:
            end = mid
    return -1

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
binary_search(my_list, target)
