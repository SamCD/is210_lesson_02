#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {0} news! I won the raffle with number {1}!'.format("*drab","000042",friend="Alex")
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
EMAIL = NEWS.format(NTYPE, RNUM, friend= FNAME)
