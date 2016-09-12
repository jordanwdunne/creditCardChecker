from main import *

def runTests():
    passedTests = True

    #test validation function works
    if isValid(3379513561108795) != True:
        print "Failed Validation Tests"
        passedTests = False

    #test checkdigit generation function works
    if getCheckDigit(337951356110879) != 5:
        print "Failed CheckDigit Generation Test"
        passedTests = False

    #test card number generation function works
    testNumber = generateValidCard()

    if isValid(generateValidCard()) != True:
        print "Failed Valid Card Number Generation Test"
        passedTests = False

    #test cards are matched to the correct carriers
    if "Visa" != lookupCardType(4):
        print "Failed Card Recognition Test Visa"
        passedTests = False

    if "China UnionPay" != lookupCardType(62):
        print "Failed Card Recognition Test UnionPay"
        passedTests = False

    if "DinersClub" != lookupCardType(301):
        print "Failed Card Recognition Test DinersClub"
        passedTests = False

    if "Discover Card" != lookupCardType(6011):
        print "Failed Card Recognition Test Discover"
        passedTests = False

    if "JCB" != lookupCardType(3545):
        print "Failed Card Recognition Test JCB"
        passedTests = False

    if "Laser" != lookupCardType(6304):
        print "Failed Card Recognition Test Laser"
        passedTests = False

    #generate several random card numbers that should be valid, and check for validity
    for testCase in range(0,100):
        testNumber = generateValidCard()
        if isValid(generateValidCard()) != True:
            print "Failed Valid Card Number Generation Test"
            passedTests = False
            print "Failed Number:", str(testNumber)
        else:
            print "Tested Number", str(testNumber), "is Valid and belongs to", lookupCardType(testNumber), "company"

    #notify if all tests passed
    if passedTests == True:
        print "All Tests Passed"
        return True
    else:
        return False

runTests()
