
''' Problem statement:

 Write a function that takes in a non-empty array of distinct integers and an
 *   integer representing a target sum. If any two numbers in the input array sum
 *   up to the target sum, the function should return them in an array, in any
 *   order. If no two numbers sum up to the target sum, the function should return
 *   an empty array.
 *
 *   Note that the target sum has to be obtained by summing two different integers
 *   in the array; you can't add a single integer to itself in order to obtain the
 *   target sum.
 *
 *   You can assume that there will be at most one pair of numbers summing up to
 *   the target sum.

 '''



''' Solution 1 - Best solution: Time complexity : O(N)'''
def twoNumberSum(array, targetSum):
    startIdx = 0
    endIdx = len(array) - 1
    while startIdx < endIdx:
        sum = array[startIdx] + array[endIdx]
        if sum > targetSum:
            endIdx -= 1
        elif sum < targetSum:
            startIdx += 1
        else:
            return([array[startIdx], array[endIdx]])
    return []

# **************************** ##### ***********************************

''' Solution 2:  Time complexity : O(N^2)'''
'''def twoNumberSum(array, targetSum):
    for i in range(len(array) - 1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                return [array[i], array[j]]'''

# **************************** ##### ***********************************
''' Solution 3: TIme Complexity : O(N)'''
'''def twoNumberSum(array, targetSum):
    nums = []
    for num in array:
        if targetSum - num in nums:
            return [targetSum - num , num]
        else:
            nums.append(num)'''



#inputs

array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
print("output is:")
print(twoNumberSum(array, targetSum))


# output
#[-1, 11]