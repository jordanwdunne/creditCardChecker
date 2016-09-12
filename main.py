import random
import sys

def digitMap(number):
    return list(map(int, str(number)))

def checkSum(cardNumber):
    digits = digitMap(cardNumber)
    oddDigits = digits[-1::-2]
    evenDigits = digits[-2::-2]
    total = sum(oddDigits)
    for digit in evenDigits:
        total += sum(digitMap(2 * digit))
    checkSumValue = total % 10
    return checkSumValue

def isValid(cardNumber):
    if checkSum(cardNumber) == 0 and len(str(cardNumber)) == 16:
        return True
    else:
        return False

def getCheckDigit(partialCardNumber):
    checkDigit = checkSum(int(partialCardNumber) * 10)
    return checkDigit if checkDigit == 0 else 10 - checkDigit

def generateValidCard():
    firstDigits = random.randrange(100000000000000, 999999999999999, 1)
    checkDigit = getCheckDigit(firstDigits)
    validNumber = firstDigits * 10 + checkDigit
    return validNumber

def getCardPrefix(startDigitLength, cardNumber):
    digitString = str(cardNumber)
    return int(digitString[:startDigitLength])

def lookupCardType(cardNumber):
    oneDigit = getCardPrefix(1, cardNumber)
    twoDigits = getCardPrefix(2, cardNumber)
    threeDigits = getCardPrefix(3, cardNumber)
    fourDigits = getCardPrefix(4, cardNumber)
    sixDigits = getCardPrefix(6, cardNumber)
    if twoDigits == 34 or twoDigits == 37:
        return "American Express"
    elif twoDigits == 62 or twoDigits == 88:
        return "China UnionPay"
    elif threeDigits in range(300,305) or threeDigits in range(54,55):
        return "DinersClub"
    elif sixDigits == 6011 or sixDigits in range(622126,622925) or threeDigits in range(644,649) or twoDigits == 65:
        return "Discover Card"
    elif fourDigits in range(3528,3589):
        return "JCB"
    elif fourDigits == 6304 or fourDigits == 6706 or fourDigits == 6771 or fourDigits == 6709:
        return "Laser"
    elif fourDigits == 5018 or fourDigits == 5020 or fourDigits == 5038 or fourDigits == 5612 or fourDigits == 5893 or fourDigits == 6304 or fourDigits == 6759 or fourDigits == 6761 or fourDigits == 6762 or fourDigits == 6763 or fourDigits == 0604 or fourDigits == 6390:
        return "Maestro"
    elif fourDigits == 5019:
        return "Dankort"
    elif twoDigits in range(50,55):
        return "MasterCard"
    elif oneDigit == 4:
        return "Visa"
    elif fourDigits == 4026 or sixDigits == 417500 or fourDigits == 4405 or fourDigits == 4508 or fourDigits == 4844 or fourDigits == 4913 or fourDigits == 4917:
        return "Visa Electron"
    else:
        return "Unknown"

def generateValidCardWithInfo():
    cardNumber = generateValidCard()
    cardType = lookupCardType(cardNumber)
    print "Generated Card Number:", str(cardNumber), cardType


def generateValidCardWithKnownCompany():
    cardType = "Unknown"
    while cardType == "Unknown":
        cardNumber = generateValidCard()
        cardType = lookupCardType(cardNumber)
    print "Generated Card Number:", str(cardNumber), cardType

def generateValidCardWithUnknownCompany():
    cardType = "Known"
    while cardType == "Known":
        cardNumber = generateValidCard()
        cardType = lookupCardType(cardNumber)
        if lookupCardType(cardNumber) != "Unknown":
            cardType = "Known"

    print "Generated Card Number:", str(cardNumber), cardType

def printUsage():
    print "Usage:"
    print "-H -- Help/Usage"
    print "-K -- Generate a valid card number with a valid company"
    print "-U -- Generate a valid card number with an unknown company"
    print "-C -- Check a given card number for validity (ex. main.py -C 94304056966994)"

def main(argv):
    if len(argv) == 0:
        printUsage()
    elif len(argv) == 1:
        if argv[0] == "-K" or argv[0] == "-k":
            generateValidCardWithKnownCompany()
        elif argv[0] == "-U" or argv[0] == "-u":
            generateValidCardWithUnknownCompany()
        elif argv[0] == "-H" or argv[0] == "-h":
            printUsage()
    elif len(argv) == 2 and argv[0] == "-C" or argv[0] == "-c":
        if isValid(int(argv[1])):
            print "Entered Card Number is Valid, Company is", str(lookupCardType(int(argv[1])))
        else:
            print "Entered Card Number is not Valid"
    else:
        printUsage()

if __name__ == "__main__":
    main(sys.argv[1:])
