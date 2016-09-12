# Credit Card Number Checker

This is a small command line utility offering some functions related to credit card number validation.

## With it, you can:

 - Generate valid credit card numbers
 - Check which companies cards belong to
 - Check if an entered number is valid

## How the Algorithm Works

 Credit card and debit card numbers are checked with [Luhn's](https://en.wikipedia.org/wiki/Hans_Peter_Luhn) Algorithm. Luhn's Algorithm is a simple checksum formula, and is used to catch simple transcription errors in card numbers when they're entered. It's not perfect; if too many digits are changed, or switched, then it can incorrectly verify a number as correct.

 The algorithm relies on doubling every even digit in the number, adding the individual results together (so 6 * 2 = 12, and 1+2 = 3), adding all of those results, and then comparing the mod of that sum with the check digit. In the case of a credit card number, that check digit is the last number in the credit card number.

 For a more thorough explanation of how this works, with a few examples, the [Wikipedia article](https://en.wikipedia.org/wiki/Luhn_algorithm) on the subject is quite good.

## Usage:

 - -H -- Help/Usage
 - -K -- Generate a valid card number with a valid company
 - -U -- Generate a valid card number with an unknown company
 - -C -- Check a given card number for validity (ex. python main.py -C 94304056966994)
