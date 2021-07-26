def longestPeak(array):
    i = 1
    maxLength = 0
    while i < len(array) - 1:
        isPeak = array[i-1] < array[i] > array[i+1]

        if not isPeak:
            i += 1
            continue

        if isPeak:
            leftIdx = i - 2
            while leftIdx >=0 and array[leftIdx - 1] < array[leftIdx]:
                leftIdx = leftIdx - 1

            rightIdx = i + 2
            while rightIdx < len(array) and array[rightIdx] > array[rightIdx - 1]:
                rightIdx = rightIdx + 1

        currentLength = rightIdx - leftIdx - 1
        maxLength = max(maxLength, currentLength)

        i = rightIdx

    return maxLength










array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(longestPeak(array))
