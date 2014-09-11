#!/usr/bin/env python
# -*- coding: utf-8 -*-

FLOATVAR = 0.1
from decimal import Decimal
from fractions import Fraction
DECIMALVAR = Decimal("0.1")
FRACTIONVAR = Fraction(1,10)
EQUALITY_DF = (DECIMALVAR == FRACTIONVAR)
ARE_INEQUAL = (DECIMALVAR != FRACTIONVAR != FLOATVAR)
