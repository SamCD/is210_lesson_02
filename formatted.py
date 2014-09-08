#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {{friend}}! I have {{1}} news! I won the raffle with number {0}!'.format("000042")
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
