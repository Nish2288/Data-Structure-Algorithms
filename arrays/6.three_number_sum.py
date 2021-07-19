'''
Given an array of distinct integers and an integer representing a target sum, write a function that find all combinations
 of three numbers in the array that add up to the target sum. The function should return a 2-dimensional array of all these combinations.
The numbers in each combination should be ordered in ascending order, and the combinations themselves should also be ordered in ascending order,
 for instance: [[-8, 2, 6],[-8, 3, 5], [-6, 1, 5]]. If there is no such combination, return an empty array.

Time Complexity : O(N^2)
 '''


def threeNumberSum(array, targetSum):
    array.sort()
    finalArray = []
    for idx in range(len(array)):
        leftIdx = idx + 1
        rightIdx = len(array) - 1
        currentValue = array[idx]
        while leftIdx < rightIdx:
            sum = currentValue + array[leftIdx] + array[rightIdx]
            if sum > targetSum:
                rightIdx = rightIdx - 1
            elif sum < targetSum:
                leftIdx = leftIdx + 1
            else:
                finalArray.append([currentValue, array[leftIdx], array[rightIdx]])
                leftIdx = leftIdx + 1
                rightIdx = rightIdx - 1

    return finalArray


array = [12, 3, 1, 2, -6, 5, -8, 6]
targetSum = 0

print(threeNumberSum(array, targetSum))