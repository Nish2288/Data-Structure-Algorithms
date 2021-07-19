'''
Given two arrays of integers, I am asked to write a function that finds two numbers, where one number comes from the first
array and another number comes from the second array, with smallest absolute difference, and returns them in an array.
In the resulting array, the number from the first array should come first.

For example,

arrayOne = [-1, 5, 10, 20, 28, 3];
arrayTwo = [26, 134, 135, 15, 17];
The output is [28, 26].

O(nlogn + mlogm)
'''



def smallestDifference(arrayOne, arrayTwo):
    smallest = float("inf")
    current = float("inf")
    smallestPair = []
    leftIdx = 0
    rightIdx = 0

    while leftIdx < len(arrayOne) and rightIdx < len(arrayTwo):
        firstNumber = arrayOne[leftIdx]
        secondNumber = arrayTwo[rightIdx]

        if firstNumber > secondNumber:
            current = firstNumber - secondNumber
            rightIdx += 1
        elif secondNumber > firstNumber:
            current = secondNumber - firstNumber
            leftIdx += 1
        else:
            return [firstNumber, secondNumber]

        if current < smallest:
            smallest = current
            smallestPair = [firstNumber, secondNumber]

    return smallestPair









arrayOne = [-1, 5, 10, 20, 28, 3]
arrayTwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayOne, arrayTwo))