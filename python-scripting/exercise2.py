#!/usr/bin/env python3.6
from math import pi
from os import getenv

digits = int(getenv("DIGITS") or 10)
print("%.*f" % (digits, pi))

