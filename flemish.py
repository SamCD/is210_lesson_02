#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
STR = 'Spanish'
STRLEN = len(STR)
STRIND = FISHY.index(STR)
FISH1 = FISHY[:STRIND]
FISH2 = FISHY[STRIND:]
FLEMISH = FISH1 + 'Flemish' + FISH2[STRLEN:]
