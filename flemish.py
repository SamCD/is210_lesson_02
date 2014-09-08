#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
ONE_FISH = 'Spanish'
TWO_FISH = len(ONE_FISH)
SPANISH_FISHY = FISHY.index(ONE_FISH, 0, len(FISHY))
FLEMISH_INQUISITION = FISHY[:19] + 'Flemish' + FISHY[26:]
