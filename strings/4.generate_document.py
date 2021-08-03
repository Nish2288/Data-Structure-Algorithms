# Best solution: O(C + D)
def generateDocument(characters, document):
    charCounts = {}

    for char in characters:
        if char not in charCounts:
            charCounts[char] = 0
        charCounts[char] += 1

    for char in document:
        if char not in charCounts or charCounts[char] == 0:
            return False

        charCounts[char] -= 1

    return True


# solution 2: O(U * (D+C))
# def getCharacterCount(char, document):
#     freq = 0
#     for docChar in document:
#         if docChar == char:
#             freq += 1
#     return freq
#
#
# def generateDocument(characters, document):
#     charCount = 0
#     docCount = 0
#     uniqueChar = []
#
#     for char in document:
#         if char not in uniqueChar:
#             uniqueChar.append(char)
#             docCount = getCharacterCount(char, document)
#             charCount = getCharacterCount(char, characters)
#
#     if docCount > charCount:
#         return False
#
#     return True


# Solution 1 : O(D * (D+C))
# def getCharacterCount(char, document):
#     freq = 0
#     for docChar in document:
#         if docChar == char:
#             freq += 1
#     return freq
#
#
# def generateDocument(characters, document):
#     charCount = 0
#     docCount = 0
#
#     for char in document:
#         docCount = getCharacterCount(char, document)
#         charCount = getCharacterCount(char, characters)
#
#     if docCount > charCount:
#         return False
#
#     return True







characters = 'abcabc'
document = 'aabbcc'

print(generateDocument(characters, document))