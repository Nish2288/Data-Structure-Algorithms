
# O(N)
def isPalindrome(string):
    leftIdx = 0
    rightIdx = len(string) - 1

    while leftIdx < rightIdx:
        if string[leftIdx] != string[rightIdx]:
            return False

        leftIdx = leftIdx + 1
        rightIdx = rightIdx - 1
    return True


# O(N^2)
# def isPalindrome(string):
#     newString = ""
#     for i in reversed(range(len(string))):
#         newString += string[i]
#
#     return string == newString



# O(N)
# def isPalindrome(string):
#     reversedString = string[::-1]
#
#     return string == reversedString



string = "abcdcba"
print(isPalindrome(string))