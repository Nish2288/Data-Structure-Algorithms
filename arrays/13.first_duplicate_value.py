''' Return first duplicate value.
    if no duplicate then return -1
'''

def firstDuplicateValue(array):
    for val in array:
        if array[abs(val) - 1 ] < 0:
            return abs(val)
        array[abs(val) - 1] *= -1
    return -1


# # O(N)
# def firstDuplicateValue(array):
#     arrayList = []
#     for a in array:
#         if a in arrayList:
#             return a
#         else:
#             arrayList.append(a)
#     return -1


array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))