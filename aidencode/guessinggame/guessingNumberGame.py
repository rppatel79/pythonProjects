import random

TOTAL_NUMBER_OF_GAMES = 2
PLAYERS = 2

player1Tries = 0
player2Tries = 0

for playerId in range(1, PLAYERS + 1):

    for gameId in range(1, TOTAL_NUMBER_OF_GAMES + 1):
        humanTriesInAGame = 1

        # the computer makes a guess
        computerGuess = int(random.random() * 10)
        # print("Computer guessed:  " + str(computerGuess))

        # reset humanGuess
        humanGuess = -1

        # loop
        while humanGuess != computerGuess:
            # player makes a guess
            humanGuess = int(input("Player["+str(playerId)+"]-Game["+str(gameId)+"] What is your guess (try[" +
                                   str(humanTriesInAGame) + "])? :"))

            if humanGuess == computerGuess:
                print("You guessed right!!")
            else:
                print("You loser, try again.")
                humanTriesInAGame += 1

        print("Player["+str(playerId)+"]-Game [" + str(gameId) + "] over")

        if playerId == 1:  # Player 1's turn
            player1Tries += humanTriesInAGame
        else:
            player2Tries += humanTriesInAGame

    if playerId == 1:  # Player 1's turn
        print("Player[" + str(playerId) + "] -Your games are over- Your total score was [" + str(player1Tries) + "]")
    else:
        print("Player[" + str(playerId) + "] -Your games are over- Your total score was [" + str(player2Tries) + "]")
