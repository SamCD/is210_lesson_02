#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Practice using number types"""

from decimal import Decimal
from fractions import Fraction

FLOATVAR = 0.1
DECIMALVAR0 = Decimal(.01)
DECIMALVAR = '{0:4.2f}'.format(DECIMALVAR0)
FRACTIONVAR = Fraction(1, 10)

DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
