#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

FNAME = 'Alex'
NTYPE = '*amazing*'
RNUM = 5678
NEWS = 'Hi {friend}! I have {0} news!I won the raffle with number {1:06.0f}!'
EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
