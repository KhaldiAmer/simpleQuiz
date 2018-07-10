#!/usr/bin/env python
# -*- coding: utf-8 -*-

# paragraphs for levels 
easy = "word word word [missing word 1] word word word word word word [missing word 2], word word [missing word 3], word word word word [missing word 4]"
medium = "word word word [missing word 1] word word word word word word [missing word 2], word word [missing word 3], word word word word [missing word 4]"
hard = "word word word [missing word 1] word word word word word word [missing word 2], word word [missing word 3], word word word word [missing word 4]"
# answers for levels 
easy_answers = ["word1","word2","word3","word4"]
medium_answers = ["word1","word2","word3","word4"]
hard_answers = ["word1","word2","word3","word4"]

def select_level():
	print("Hello to Amer's quiz")
	level = raw_input("Please select a level: easy or medium or hard \r\n")
	if level == "easy": 
		return go(easy,easy_answers)
	elif level == "medium":
		return go(medium,medium_answers)
	elif level == "hard":
		return go(hard,hard_answers)
	print "You should choose again"
	return select_level()
# Starts the quiz, checks answers, limits users input
def go(text, answers):
	print(text)
	x = 0
	while x < len(answers):
		answer = raw_input("What is {}?\r\n".format(x+1))
		if answer == answers[x]:
			print("Awesome! next one!")
		else:
			print("Wrong answer")
			continue
		x += 1
	retry = raw_input("You got it all right! want to try again? y or n\r\n")
	if retry == "y":
		select_level()
	exit()
select_level()

