#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY = inquisition.SPANISH.replace("surprise", "haddock")
FLEM = "Flemish"
SPAN1 = FISHY[0:19]
SPAN2 = FISHY[26:]
NEW_VERS = SPAN1 + FLEM + SPAN2
