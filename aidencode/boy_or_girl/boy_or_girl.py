def scoreAnswer1(answer) -> int:
    switcher = {
        "blue": 90,
        "pink": 10,
        "red": 50
    }
    return switcher.get(answer, 50)


def scoreAnswer2(answer) -> int:
    switcher = {
        "long": 10,
        "medium": 60,
        "short": 90
    }
    return switcher.get(answer, 50)


# First question
answer1 = input("What colour do you like?")
scoreAnswer1=scoreAnswer1(answer1)
print("Your answer was [" + answer1 + "] that has the score [" + str(scoreAnswer1) + "]")
# 2question
answer2 = input("is your hair long, medium short?")
scoreAnswer2=scoreAnswer2(answer2)
print("Your answer was [" + answer2 + "] that has the score [" + str(scoreAnswer2)+ "]")

total = scoreAnswer1 + scoreAnswer2
if total > 100:
    print("Your total was [" + str(total) + "].  We guess you are a boy.")
else:
    print("Your total was [" + str(total) + "].  We guess you are a boy.")
