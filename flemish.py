#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition
FISHY = inquisition.SPANISH.replace('surprise', 'haddock')
WHERE = FISHY.index('Spanish')
FIRST = FISHY[:(WHERE)]
WORD = 'Flemish'
END = FISHY[WHERE+len('Spanish'):]
FLEMISH = FIRST + WORD + END
