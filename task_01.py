#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module contains functions to calculate degree measurements."""

import decimal

ABSOLUTE_DIFFERENCE = decimal.Decimal('273.15')


def fahrenheit_to_celsius(degrees):
    """Does some math and returns celcius as decimal.

    Args:
        degrees (int): Degrees in Farenheit.

    Returns:
        celsius (int, decimal): Decimal representation of Celcius Temperature.

    Examples:
        >>>fahrenheit_to_celsius(212)
        Decimal('100')
    """
    celsius = decimal.Decimal((degrees-32)*5)/9
    return celsius


def celsius_to_kelvin(degrees):
    """Does some math and returns decimal representation of kelvin.

    Args:
        degrees (int): Degrees in Celcius.
        ABSOLUTE_DIFFERENCE (int): Airthmetically incremented by degrees.

    Returns:
        kelvin (int ,decimal): Decimal representation of kelvin temperature.

    Examples:
        >>>celcius_to_kevin(100)
        Decimal('373.15')
    """
    kelvin = decimal.Decimal(ABSOLUTE_DIFFERENCE + degrees)
    return kelvin


def fahrenheit_to_kelvin(degrees):
    """Does some math and returns degrees as decimal represenation of kelvin.

    Args:
        degrees (int): Degrees in Fahrenheit.

    Returns:
        kelvin (int): Decimal representation of kelvin temperature.

    Examples:
        >>>fahrenheit_to_kelvin(212)
        Decimal('373.15')
    """
    kelvin = fahrenheit_to_celsius(degrees)+ABSOLUTE_DIFFERENCE
    return kelvin
