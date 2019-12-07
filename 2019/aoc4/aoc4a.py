def testTwoAdjacent(guess):
    for index in range(5):
        if (guess[index] == guess[index + 1]):
            # Two adjacent found
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

        twoAdjacent = testTwoAdjacent(guess)
        noDecrease = testNoDecrease(guess)

        if (twoAdjacent and noDecrease):
            #possible match!
            possibleMatches.append(guess)
            print(f"Possible match: {guess}")

    print(f"Found {len(possibleMatches)} Possible matches")


# Execute the program
if __name__ == "__main__":
    main()