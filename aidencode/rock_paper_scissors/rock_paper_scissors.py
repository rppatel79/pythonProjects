import random

who_won_values = ("Tie", "Computer", "Human")
items = ("rock", "paper", "scissors")


def generate_human_guess() -> str:
    ''' Asks the user for to guess a value '''
    human_guess = input("What do you select?")
    print(human_guess)
    # validate human guess
    while human_guess not in set(items):
        print("The value [", human_guess, "] is not a validate guess.  Please enter:", items)
        human_guess = input("What do you select?")
    return human_guess


def generate_computer_guess() -> str:
    ''' Generates a value for the computer '''
    random_digit = random.randint(0, 2)
    return items[random_digit]


def who_won(human_guess: str, computer_guess: str) -> str:
    ''' Determine who won the game'''
    if human_guess == computer_guess:
        return who_won_values[0]
    elif ((human_guess == items[1] and computer_guess == items[0]) or
          (human_guess == items[0] and computer_guess == items[2]) or
          (human_guess == items[2] and computer_guess == items[1])):
        return who_won_values[2]
    else:
        return who_won_values[1]


games_played =0
human_wins =0
computer_wins =0
ties=0
while True:
    games_played+=1
    print("Welcome to Game [",games_played,']')

    human_guess = generate_human_guess()
    computer_guess = generate_computer_guess()

    result = who_won(human_guess, computer_guess)
    print("The human guessed [", human_guess, "] and computer guessed [", computer_guess, "].  The winner is [",result,"]")

    #update the score
    if (result == who_won_values[0]):
        ties+=1
    elif (result == who_won_values[1]):
        computer_wins+=1
    else:
        human_wins+=1
    print("Human wins [",human_wins,"], Computer wins [",computer_wins,"] and Ties [",ties,"]")
    print()