#!/usr/bin/env python
# -*- coding: utf-8 -*-
<<<<<<< HEAD
"""Number types"""

import decimal
import fractions

FLOATVAR = float(0.1)
DECIMALVAR = decimal.Decimal(0.1)
FRACTIONVAR = fractions.Fraction(1/10)
DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = DECIMALVAR != FRACTIONVAR != FLOATVAR
=======

FLOATVAR = 0.1
from decimal import Decimal
from fractions import Fraction
DECIMALVAR = Decimal("0.1")
FRACTIONVAR = Fraction(1,10)
EQUALITY_DF = (DECIMALVAR == FRACTIONVAR)
ARE_INEQUAL = (DECIMALVAR != FRACTIONVAR != FLOATVAR)
>>>>>>> 98f4cf33f15c59cbc0a55577d4d9ef65651c58cb
