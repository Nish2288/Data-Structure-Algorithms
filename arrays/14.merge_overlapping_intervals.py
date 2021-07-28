def mergeOverlappingIntervals(intervals):
    mergeInterval = []
    sortedIntervals = sorted(intervals, key=lambda x: x[0])
    currentInterval = sortedIntervals[0]
    mergeInterval.append(currentInterval)

    for nextInterval in sortedIntervals:
        currentIntervalStart, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergeInterval.append(currentInterval)

    return mergeInterval





intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(mergeOverlappingIntervals(intervals))
