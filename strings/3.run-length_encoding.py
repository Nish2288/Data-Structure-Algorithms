def runLengthEncoding(string):
    encodedString = []
    runningCount = 1
    for i in range(1, len(string)):
        if string[i - 1] != string[i]:
            prevValue = string[i - 1]
            encodedString.append(str(runningCount))
            encodedString.append(prevValue)
            runningCount = 0

        runningCount += 1
    encodedString.append(str(runningCount))
    encodedString.append(string[i])

    return "".join(encodedString)


string = 'AAABBC'
print(runLengthEncoding(string))