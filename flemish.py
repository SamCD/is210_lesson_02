#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

FISHY = inquisition.SPANISH.replace("surprise", "haddock")

INQ = len(inquisition.SPANISH)
FL1 = inquisition.SPANISH[0:inquisition.SPANISH.index("Spanish")] + "Flemish"
FL2 = inquisition.SPANISH[len(FL1): INQ]
FLEMISH = FL1 + FL2
