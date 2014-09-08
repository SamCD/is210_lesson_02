# !/usr/bin/evn python
# -*- UTF-8 -*-

FLOATVAR = 0.1
import decimal
from decimal import*
DECIMALVAR = Decimal(0.1)
import fraction
from fractions import Fraction
FRACTIONVAR = Fraction(1, 10)
DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = FLOATVAR != DECIMALVAR != FRACTIONVAR
