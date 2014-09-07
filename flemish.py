#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
ONE_FISH = 'Spanish'
TWO_FISH = len(ONE_FISH)
SPANISH_FISHY = expectation.FISHY.index(ONE_FISH, 0, len(expectation.FISHY))
FLEMISH_INQUISITION = expectation.FISHY[:19] + 'Flemish' + expectation.FISHY[26:]
