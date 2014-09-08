#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import decimal
from decimal import*
import fractions
from fractions import Fraction
FLOATVAR = 0.1
DECIMALVAR = Decimal(0.1)
FRACTIONVAR = Fraction(1, 10)
DF_EQUALITY = DECIMALVAR == FRACTIONVAR
ARE_INEQUAL = FLOATVAR != DECIMALVAR != FRACTIONVAR
