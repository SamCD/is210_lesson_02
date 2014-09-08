#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

import inquisition

SPANISH = inquisition.SPANISH
FISHY = SPANISH.replace('surprise', 'haddock')
print FISHY

OLD = 'Spanish'
L = len(OLD)
I = FISHY.index(OLD)
BEG = FISHY[:I]
END = FISHY[I+L:]
MID = ' Flemish '
FLEMISH = BEG + MID + END
print FLEMISH