#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practice using number types"""

from decimal import Decimal
from fractions import Fraction

FLOATVAR = 0.1
DECIMALVAR = 0.1
FRACTIONVAR = 1/10

DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
