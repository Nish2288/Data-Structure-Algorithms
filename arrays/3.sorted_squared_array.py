
'''
Given an array of integers that are sorted in increasing order, write a function that squares all the integers in the array and returns them in a new array,
 also sorted in increasing order.'''

''' Best Solution: O(N)'''
def sortedSquaredArray(array):
    sortedSquared = [0 for _ in range(len(array))]
    smallValueIdx = 0
    largeValueIdx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallValue = array[smallValueIdx]
        largeValue = array[largeValueIdx]

        if abs(smallValue) > abs(largeValue):
            sortedSquared[idx] = smallValue * smallValue
            smallValueIdx += 1
        else:
            sortedSquared[idx] = largeValue * largeValue
            largeValueIdx -= 1

    return sortedSquared

#  ************ O(NlogN) **********************
# def sortedSquaredArray(array):
#     sortedSquared = []
#     for num in array:
#         sortedSquared.append(num*num)
#
#     sortedSquared.sort()
#     return sortedSquared

print(sortedSquaredArray([-7, -4, -3, 2, 6, 8, 9]))