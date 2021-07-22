''' Traverse the marix in clockwise direction and Print the number. '''

def spiralTraverse(array):
    result = []
    rowStart = 0
    rowEnd = len(array)
    colStart = 0
    colEnd = len(array[0])

    while rowStart < rowEnd and colStart < colEnd:
        for col in range(rowStart, colEnd):
            result.append(array[rowStart][col])

        for row in range(rowStart+1, rowEnd):
            result.append(array[row][colEnd-1])

        for col in reversed(range(rowStart, colEnd-1)):
            result.append(array[rowEnd-1][col])

        for row in reversed(range(rowStart+1, rowEnd-1)):
            result.append(array[row][colStart])

        rowStart = rowStart + 1
        rowEnd = rowEnd - 1
        colStart = colStart + 1
        colEnd = colEnd - 1

    return result


array= [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]



print(spiralTraverse(array))