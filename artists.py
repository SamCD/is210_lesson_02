#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Asks the great question."""


THE_GREAT_QUESTION = ('Michaelangelo. Leonardo. Rafael. Donatello. Turtles? '
                      'Creators of the great works? Both? You be the judge!')
<<<<<<< HEAD
STATEMENTS = THE_GREAT_QUESTION.split(". ")
=======
STATEMENTS = THE_GREAT_QUESTION.split(".")
>>>>>>> 98f4cf33f15c59cbc0a55577d4d9ef65651c58cb
ARTISTS = STATEMENTS[:4]
NUM_ARTISTS = len(ARTISTS)
CHARACTERS = len(THE_GREAT_QUESTION)
HAS_CREATORS = 'Creators' in THE_GREAT_QUESTION
HAS_SPLINTER = 'Splinter' in ARTISTS
