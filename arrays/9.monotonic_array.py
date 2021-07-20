''' Find monotonic array '''

''' O(N)'''
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True

    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing = False
        if array[i] < array[i-1]:
            isNonDecreasing = False

    return isNonDecreasing or isNonIncreasing







array =[-10,-5,2,4,8,9]
print(isMonotonic(array))