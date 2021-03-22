import pyttsx3
import pandas as pd
import random
import json

with open("data/words.json") as json_file:
    weeklyWords = json.load(json_file)

playersName = "Aiden"
engine = pyttsx3.init()
engine.say("Hello " + playersName + "!")
engine.runAndWait()

score = 0
for randomWord in random.sample(weeklyWords["2"], len(weeklyWords["2"])):
    engine = pyttsx3.init()
    engine.say("Please spell the word:  " + randomWord)
    engine.runAndWait()
    userGuess = input("Enter your guess: ")
    if userGuess == randomWord:
        engine.say("Great job " + playersName + "!")
        score += 1
    else:
        engine.say("Sorry, that is incorrect.")
    engine.runAndWait()

engine.say("Your score was " + str(score) + " out of "+str(len(weeklyWords["2"])))
engine.runAndWait()
