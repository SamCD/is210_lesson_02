#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number 0000{1}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = str(42)

EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
print EMAIL
