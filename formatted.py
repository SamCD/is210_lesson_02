#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = str(42).zfill(6)

#Task 19
NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'
EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
print EMAIL

#I couldn't figure out how to add the leading zeros on the NEWS variable,
#but was able to add them using .zfill() on the RNUM variable.
#Hopefully this is acceptable!  Thank you!
