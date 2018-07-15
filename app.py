#!/usr/bin/env python
# -*- coding: utf-8 -*-

from constants import *

def startQuiz():
	""" starts the quiz and directs the user to the specified level. """
	print("Hello to Eminem's words quiz")
	level = raw_input("Please select a level: easy or medium or hard \r\n")
	if level == "easy": 
		return redirectTo(easy,easy_answers)
	elif level == "medium":
		return redirectTo(medium,medium_answers)
	elif level == "hard":
		return redirectTo(hard,hard_answers)
	else:
		print("You should choose again")
		return startQuiz()


def redirectTo(level, answers):
	""" Loops through the quiz answers to get the unfilled words. """
	print(level)
	x = 0
	while x < len(answers):
		answer = raw_input("What is [TO_BE_FILLED_{}]?\r\n".format(x+1))
		if answer == answers[x]:
			print("Awesome! next one!")
			level = level.replace("[TO_BE_FILLED_{}]".format(x+1),answers[x])
			print(level)
		else:
			print("Wrong answer")
			continue
		x += 1
	retry = raw_input("You got it all right! want to try again? y or n\r\n")
	if retry == "y":
		startQuiz()
	exit()
startQuiz()

