#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 420000
NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'.format(NTYPE, RNUM, friend=FNAME)
