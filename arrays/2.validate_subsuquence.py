''' Time Complexity is : O(N) '''
'''
Implement a function that takes two arrays of integers as input and finds whether all the numbers in the sequence array
appear in the first array and they appear in the same order.
In other words, the function need to find out if we can get the sequence array, when we delete some or no elements in
the first array without changing the order of the remaining elements.

Example:
array = [5, 1, 22, 25, 6, -1, 8, 10];
sequence = [1, 6, -1, 10];

The output should be true.
'''

def isValidSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while seqIdx < len(sequence) and arrIdx < len(array):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx += 1
        arrIdx += 1

    return seqIdx == len(sequence)


# Solution 2: O(N)
# def isValidSubsequence(array, sequence):
#     seqIdx = 0
#     for value in array:
#         if seqIdx == len(sequence):
#             break
#         if sequence[seqIdx] == value:
#             seqIdx += 1
#
#     return seqIdx == len(sequence)


array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [5, 1, 22, 22, 25, 6, -1, 8, 10]
print(isValidSubsequence(array, sequence))
