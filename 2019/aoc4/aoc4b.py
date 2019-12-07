def testTwoOfDigit(guess):
    # Shortcut: Since the separate test requires that digits cannot decrease, it is not possible
    # for a valid guess to have two or more of the same digit without them being together.
    # Therefore, if this test finds that there are exactly two of any given digit, and the other test
    # finds that no digits decrease then the two of the same digit must be together.
    
    for digitInt in range(10):
        digit = str(digitInt)
        if (guess.count(digit) == 2):
            # Exactly two of a digit found
            return True

    # Got to end, no two adjacent found
    return False

def testNoDecrease(guess):
    for index in range(5):
        if (guess[index] > guess[index + 1]):
            # Decrease found
            return False

    # Got to end, no decrease found.
    return True

def main():
    possibleMatches = []

    MinGuess = 206938
    MaxGuess = 679128

    for guessInt in range(MinGuess, MaxGuess + 1):
        
        guess = str(guessInt)

        twoOfDigit = testTwoOfDigit(guess)
        noDecrease = testNoDecrease(guess)

        if (twoOfDigit and noDecrease):
            #possible match!
            possibleMatches.append(guess)
            print(f"Possible match: {guess}")

    print(f"Found {len(possibleMatches)} Possible matches")


# Execute the program
if __name__ == "__main__":
    main()