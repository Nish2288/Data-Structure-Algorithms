def caesarCipherEncryptor(string, key):
    newUnicode = []
    for c in string:
        unicode = ord(c) + key % 26
        if unicode > 122:
            newUnicode.append(chr((96 + unicode % 122)))
        else:
            newUnicode.append(chr(unicode))

    return ("".join(newUnicode))



string = "xyz"
key = 2

print(caesarCipherEncryptor(string, key))