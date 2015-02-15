#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides variables for formatting."""

NEWS = 'Hi {friend}! I have {} news! I won the raffle with number {:0>6d}!'
FNAME = 'Pat'
NTYPE = '*amazing*'
RNUM = 42
EMAIL = NEWS.format(NTYPE, RNUM, friend=FNAME)
