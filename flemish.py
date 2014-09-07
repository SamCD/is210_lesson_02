#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

SPANISH = inquisition.SPANISH
FISHY = SPANISH.replace('surprise', 'haddock')
print FISHY

OLD = 'Spanish'
print len(OLD)
print SPANISH.index(OLD)
BEG = SPANISH[:18]
END = SPANISH[27:]
MID = ' Flemish '
FLEMISH = BEG + MID + END
print FLEMISH