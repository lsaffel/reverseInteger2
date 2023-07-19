def reverseinteger(num):
    if num < 0:
        isNeg = True
    else:
        isNeg = False

    absNum = abs(num)

    # convert num to a string
    strValue = str(absNum)

    # reverse the string
    reversedString = strValue[::-1]

    # convert string to an integer
    reversedInt = int(reversedString)

    if isNeg == False:
        return reversedInt
    else:
        return -abs(reversedInt)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reverseinteger(1234))
    print(reverseinteger(-1234))
    print(reverseinteger(100))
