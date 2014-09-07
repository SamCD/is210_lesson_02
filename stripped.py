#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The cat must have slept on the keyboard!!!

Strip this terribly formatted string of its excess characters.
"""


NERVOUS_AS = """




 //////////A long-tailed cat in a room full of rockin' chairs.,,,,,,,,,, 





"""

#Task 8 part 1
NERVOUS_AS = NERVOUS_AS.strip( )

#Task 8 part 2
NERVOUS_AS = NERVOUS_AS.rstrip(',').lstrip('/')
print NERVOUS_AS
