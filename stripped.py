#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""

NERVOUS_AS = NERVOUS_AS.strip()
<<<<<<< HEAD
NERVOUS_AS = NERVOUS_AS.lstrip("/").rstrip(",")
=======
NERVOUS_AS = NERVOUS_AS.rstrip(',').lstrip('/)
>>>>>>> 98f4cf33f15c59cbc0a55577d4d9ef65651c58cb
