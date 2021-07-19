'''
Move a given number to the end of the array.

Time Complexity : O(N)
'''

def moveElementToEnd(array, toMove):
    endIdx = len(array) - 1
    startIdx = 0
    while startIdx < endIdx:
        startValue = array[startIdx]
        endValue = array[endIdx]
        if startValue == toMove and endValue != toMove:
            array[startIdx], array[endIdx] = array[endIdx], array[startIdx]
            startIdx += 1
            endIdx -= 1
        elif startValue != toMove and endValue != toMove:
            startIdx += 1
        else:
            endIdx -= 1

    return array



array = [2, 1, 2, 2, 2, 3, 4, 2]
toMove = 2

print(moveElementToEnd(array, toMove))