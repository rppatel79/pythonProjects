import random

TOTAL_NUMBER_OF_GAMES = 2
PLAYERS = 2



for playerId in range(1, PLAYERS+1):
    currentPlayerTries = 0
    print("Hello Player ["+str(playerId))+"]"

    for gameId in range(1, TOTAL_NUMBER_OF_GAMES+1):
        humanTriesInAGame = 1

        # the computer makes a guess
        computerGuess = int(random.random() * 10)
        #print("Computer guessed:  " + str(computerGuess))

        # reset humanGuess
        humanGuess = -1

        # loop
        while humanGuess != computerGuess:
            # player makes a guess
            humanGuess = int(input("What is your guess (try[" + str(humanTriesInAGame) + "])? :"))

            if humanGuess == computerGuess:
                print("You guessed right!!")
            else:
                print("You loser, try again.")
                humanTriesInAGame += 1

        print("Game " + str(gameId) + " over")
        currentPlayerTries += humanTriesInAGame
    print("Player[+"+str(playerId)+"] -Your games are over- Your total score was [" + str(currentPlayerTries) + "]")
