#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')

#Task 4
STATEMENTS = THE_GREAT_QUESTION.split('. ')
print STATEMENTS

#Task 5
ARTISTS = STATEMENTS[0:4]
print ARTISTS

#Task 6 part 1
NUM_ARTISTS = len(ARTISTS)
print NUM_ARTISTS

#Task 6 part 2
CHARACTERS = len(THE_GREAT_QUESTION)
print CHARACTERS

#Task 7
HAS_CREATORS = 'Creators' in THE_GREAT_QUESTION
print HAS_CREATORS

HAS_SPLINTERS = 'Splinters' in ARTISTS
print HAS_SPLINTERS