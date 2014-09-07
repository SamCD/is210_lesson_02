#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""

#Task 11
import inquisition
inquisition.SPANISH

SPANISH = inquisition.SPANISH
FISHY = SPANISH.replace('surprise', 'haddock')
print FISHY

x = 'Spanish'
print len(x)
print SPANISH.index(x)
beg = SPANISH[:18]
end = SPANISH[27:]
f = ' Flemish '
FLEMISH =beg + f + end 
print FLEMISH