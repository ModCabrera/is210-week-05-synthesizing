#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 5 Synthesizing Task"""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Does some math and returns celcius as decimal.

    Args:
        degrees (int): Arg to be arithmetically subtracted from 32
        then multiplied by 5, and divided by 9.
    Returns:
        int: Arg is returned as a decimal representation of celsius temp.
    Examples:
        >>>fahrenheit_to_celsius(212)
        Decimal('100')        
    """
    result = decimal.Decimal((degrees-32)*5)/9
    return result


def celsius_to_kelvin(degrees):
    """Does some math and returns kelvin as decimal.

    Args:
        degrees (int): Arg to be arithmetically incremented by ABSOLUTE_DIFFERENCE.
        ABSOLUTE_DIFFERENCE (int): Arg to be airthmetically incremented by degrees.
    Returns:
        int: Arguments are returned as a decimal representation of kelvin temperature.
    Examples:
        >>>celcius_to_kevin(100)
        Decimal('373.15')        
    """
    result = decimal.Decimal(ABSOLUTE_DIFFERENCE + degrees)
    return result


def fahrenheit_to_kelvin(degrees):
    """Does some math and returns degrees as decimal.

    Args:
        degrees (int): Arg to be arithmetically incremented by ABSOLUTE_DIFFERENCE.
        fahrenheit_to_celsius (mixed): Arg to be arithmetically incremented by ABSOLUTE_DIFFERENCE.
        ABSOLUTE_DIFFERENCE (int): Arg to be airthmetically incremented by degrees.
    Returns:
        int: Arguments are returned as a decimal representation of kelvin temperature.
    Examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')        
    """
    return fahrenheit_to_celsius(degrees)+ABSOLUTE_DIFFERENCE
